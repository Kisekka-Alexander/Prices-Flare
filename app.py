from flask import Flask,render_template, request, redirect, flash, session
from flask.helpers import url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os, json, datetime
from flask_bootstrap import Bootstrap
from Forms import RegistrationForm, LoginForm, DashboardParamsForm, AddMarketForm, AddItemForm
from werkzeug.security import generate_password_hash, check_password_hash

import pandas as pd
import seaborn as sns
from io import BytesIO
import base64


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Leo@2567'
app.config['MYSQL_DB'] = 'price_flare'
# app.config['MYSQL_PORT'] = 3308

app.config['SECRET_KEY'] = 'secret key'
Bootstrap(app)
 
mysql = MySQL(app)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

def defaultconverter(o):
  if isinstance(o, datetime.date):
      return o.__str__()

@app.route('/users/add', methods = ['POST', 'GET'])
def register():
   form=RegistrationForm(request.form)
   if request.method=='POST' and form.validate():
       username= form.username.data
       email=form.email.data   
       password=generate_password_hash(form.password.data, method='sha256')

       cursor = mysql.connection.cursor()
       cursor.execute(''' INSERT INTO tbl_users VALUES(Null,%s,%s,%s)''',(username,email,password))
       mysql.connection.commit()
       cursor.close()
       return redirect(url_for('user'))
   return render_template("register.html",form=form)


@app.route('/add/market', methods = ['POST', 'GET'])
def addmarket():
   form=AddMarketForm(request.form)
   if request.method=='POST' and form.validate():
       market= form.marketname.data
       code=form.marketcode.data

       cursor = mysql.connection.cursor()
       cursor.execute(''' INSERT INTO tbl_markets VALUES(Null,%s,%s)''',(code,market))
       mysql.connection.commit()
       cursor.close()
       return redirect(url_for('market'))
   return render_template("add_market.html",form=form)

@app.route('/add/item', methods = ['POST', 'GET'])
def additem():
   form=AddItemForm(request.form)
   if request.method=='POST' and form.validate():
       item= form.itemname.data
       code=form.itemcode.data
       unitofmeasure=form.unitofmeasure.data

       cursor = mysql.connection.cursor()
       cursor.execute(''' INSERT INTO tbl_items VALUES(Null,%s,%s,%s)''',(code,item,unitofmeasure))
       mysql.connection.commit()
       cursor.close()
       return redirect(url_for('item'))
   return render_template("add_item.html",form=form)

@app.route('/login', methods=['POST','GET'])
def login():
    form=LoginForm(request.form)
    if request.method=='POST' and form.validate():
        username = form.username.data
        password = form.password.data

        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT COUNT(username) count, username, password FROM tbl_users where username=%s",[username])
        users=cursor.fetchall()
        for user in users:
           dbpassword=user.get("password")
           dbcount=user.get("count")
           dbuser=user.get("username")
           

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database

        if dbcount==0 or not check_password_hash(dbpassword, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

        session['loggedin'] = True
        session['username'] = dbuser
        return redirect(url_for('dashboard'))
       
    # if the above check passes, then we know the user has the right credentials
    return render_template("login.html",form=form) 

@app.route('/subscribers',methods=['GET','POST'])
def subscriber():
    #creating variable for connection
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #executing query
    cursor.execute("SELECT FORMAT((@row_number:=@row_number + 1),0) AS row_num, A.FirstName name,a.PhoneNumber contact, a.Location location,B.Market market, c.Item item  FROM tbl_subscribers A LEFT JOIN tbl_markets B on A.Market=B.ID left join tbl_items C ON A.Item=C.ID ,(SELECT @row_number:=0) AS temp where A.Active=1")
    #fetching all records from database
    data=cursor.fetchall()
    #returning back to subscriber.html with all records from MySQL which are stored in variable data
    return render_template("subscribers.html",data=data)

@app.route('/markets',methods=['GET','POST'])
def market():

    if 'loggedin' in session:
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT *,FORMAT((@row_number:=@row_number + 1),0) AS row_num  FROM tbl_markets,(SELECT @row_number:=0) AS temp")
        data=cursor.fetchall()
        return render_template("markets.html",markets=data)

    return redirect(url_for('login'))

@app.route('/items',methods=['GET','POST'])
def item():

    if 'loggedin' in session:
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_items")
        data=cursor.fetchall()
        return render_template("items.html",items=data)

    return redirect(url_for('login'))
    


@app.route('/users',methods=['GET','POST'])
def user():
    
    if 'loggedin' in session:
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_users")
        users=cursor.fetchall()
        return render_template("users.html",users=users)   

    return redirect(url_for('login'))


@app.route('/dashboard',methods=['GET','POST'])
def dashboard():

    if 'loggedin' in session:
        form=DashboardParamsForm(request.form)
        startdate=form.start_date.data if form.start_date.data else '2020-01-01'
        enddate=form.end_date.data if form.end_date.data else '2099-12-31'
        selecteditem = form.item.data if form.item.data else 1
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        ############### Create a Seaborn Plot ####################
        cursor.execute("SELECT item,price,date(date) date FROM tbl_prices  where item=%s and DATE(date) between %s and %s",(selecteditem,startdate,enddate))
        data = cursor.fetchall()
        data = pd.DataFrame(data)
        x = data['date']
        y = data['price']
        plot = sns.scatterplot(x=x,y=y, hue='item', data=data)

        # Save the plot to a bytesIO object
        img = BytesIO()
        plot.get_figure().savefig(img, format='png')
        img.seek(0)

        # Embed the plot in the HTML Template
        plot_url = base64.b64encode(img.getvalue()).decode()


        ############### For analysing price trend one item within a selected period ####################

        cursor.execute("SELECT REPLACE(FORMAT(AVG(price),0),',','') as price,DATE(date) as date FROM `tbl_prices` where item=%s and DATE(date) between %s and %s group by DATE(date)",(selecteditem,startdate,enddate))
        prices=cursor.fetchall()
        
        dates_labels=[]
        price_labels=[]
        for price in prices:
            price_labels.append(price.get("price"))
        for date in prices:
            dates_labels.append(date.get("date"))

        ############### For analysing price trend of one item with different markets within a selected period ####################

        cursor.execute("select REPLACE(FORMAT(AVG(price),0),',','') as price, B.market_name from tbl_prices A left join tbl_markets B ON A.market=B.id where item=%s and DATE(date) between %s and %s group by B.market_name ",(selecteditem,startdate,enddate))
        marketprices=cursor.fetchall()
        
        market_label=[]
        marketprice=[]
        for price in marketprices:
            marketprice.append(price.get("price"))
        for market in marketprices:
            market_label.append(market.get("market_name"))       

        ################ For Number of Checks per item ##################
        cursor.execute("SELECT COUNT(a.item)count,b.item_name FROM tbl_prices a left join tbl_items b on a.item=b.id GROUP by b.item_name")
        checks=cursor.fetchall()
        count_label=[]
        item_label=[]
        for item in checks:
            item_label.append(item.get("item_name"))
        for count in checks:
            count_label.append(count.get("count"))

        ################# Get Item List Into Dropdown #########################
        cursor.execute("select id, item_name from tbl_items")
        itemlist=cursor.fetchall()
        form.item.choices = [(item.get("id"), item.get("item_name")) for item in itemlist]


        return render_template("dashboard.html", 
        values=json.dumps(price_labels), 
        labels=json.dumps(dates_labels, default = defaultconverter),
        y=json.dumps(marketprice),
        x=json.dumps(market_label),
        count=json.dumps(count_label),
        item=json.dumps(item_label), form=form, state=itemlist, plot_url=plot_url)
    
    return redirect(url_for('login'))