from flask import Flask,render_template, request, redirect, flash, session,send_from_directory
from flask.helpers import url_for
from flask_mysqldb import MySQL
from MySQLdb.cursors import DictCursor
from dotenv import load_dotenv
import os, json, datetime
from flask_bootstrap import Bootstrap
from Forms import RegistrationForm, LoginForm, DashboardParamsForm, AddMarketForm, AddItemForm
from werkzeug.security import generate_password_hash, check_password_hash

import pandas as pd
import seaborn as sns
from io import BytesIO
import base64

import matplotlib.pyplot as plt
import nbformat
from nbclient import NotebookClient

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
# app.config['MYSQL_PORT'] = 3308

app.config['SECRET_KEY'] = 'secret key'
Bootstrap(app)
 
mysql = MySQL(app)

try:
    mysql.connection.ping()
except Exception as e:
    print(f"Error connecting to MySQL: {e}")



@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

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
       password=generate_password_hash(form.password.data, method='pbkdf2:sha256')

       cursor = mysql.connection.cursor(DictCursor)
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

        cursor = mysql.connection.cursor(DictCursor)
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
    #executing query
    cursor = mysql.connection.cursor(DictCursor)
    cursor.execute("SELECT FORMAT((@row_number:=@row_number + 1),0) AS row_num, A.full_name name,A.phone_number contact, A.location ,B.market, C.item_name  FROM tbl_subscribers A LEFT JOIN tbl_markets B on A.market=B.id left join tbl_items C ON A.item=C.id ,(SELECT @row_number:=0) AS temp where A.active=1")
    #fetching all records from database
    data=cursor.fetchall()
    #returning back to subscriber.html with all records from MySQL which are stored in variable data
    return render_template("subscribers.html",data=data)

@app.route('/markets',methods=['GET','POST'])
def market():

    if 'loggedin' in session:

        cursor = mysql.connection.cursor(DictCursor)
        cursor.execute("SELECT *,FORMAT((@row_number:=@row_number + 1),0) AS row_num  FROM tbl_markets,(SELECT @row_number:=0) AS temp")
        data=cursor.fetchall()
        return render_template("markets.html",markets=data)

    return redirect(url_for('login'))

@app.route('/items',methods=['GET','POST'])
def item():

    if 'loggedin' in session:

        cursor = mysql.connection.cursor(DictCursor)
        cursor.execute("SELECT * FROM tbl_items")
        data=cursor.fetchall()
        return render_template("items.html",items=data)

    return redirect(url_for('login'))
    


@app.route('/users',methods=['GET','POST'])
def user():
    
    if 'loggedin' in session:

        cursor = mysql.connection.cursor(DictCursor)
        cursor.execute("SELECT * FROM tbl_users")
        users=cursor.fetchall()
        return render_template("users.html",users=users)   

    return redirect(url_for('login'))


@app.route('/dashboard',methods=['GET','POST'])
def dashboard():

    if 'loggedin' in session:
        form=DashboardParamsForm(request.form)
        start_date=form.start_date.data if form.start_date.data else '2020-01-01'
        end_date=form.end_date.data if form.end_date.data else '2099-12-31'
        selected_item = form.item.data if form.item.data else ""

        # DB CONNECTION
        cursor = mysql.connection.cursor(DictCursor)
        cursor.execute("SELECT item_name item,price,DATE_FORMAT(date, '%%Y-%%m') as date FROM tbl_prices A left join tbl_items B on A.item=B.id  where ((A.item=%s) or %s='') and DATE(date) between %s and %s",(selected_item,selected_item,start_date,end_date))
        data = cursor.fetchall()
        data = pd.DataFrame(data)

        # Specify the file path for the CSV file
        csv_file_path = 'output.csv'

        # Save the DataFrame to a CSV file
        data.to_csv(csv_file_path, index=False)

        # Load the notebook
        with open('visualization_notebook.ipynb') as notebook_file:
            notebook = nbformat.read(notebook_file, as_version=4)

        client = NotebookClient(notebook, timeout=600, kernel_name='python3')
        client.execute()


                            # x = data['date']
                            # y = data['price']
                            # scatter_plot = sns.scatterplot(x=x,y=y, hue='item', data=data)
                            # line_plot = sns.lineplot(data=data, x="date",y="price", hue="item", style="item", markers=True, dashes=False)

                            # scatter_plot_img = BytesIO()
                            # scatter_plot.get_figure().savefig(scatter_plot_img, format='jpg')
                            # scatter_plot_img.seek(0)

                            # line_plot_img = BytesIO()
                            # line_plot.get_figure().savefig(line_plot_img, format='png')
                            # line_plot_img.seek(0)

                            # line_plot_url = base64.b64encode(line_plot_img.getvalue()).decode()
                            # scatter_plot_url = base64.b64encode(scatter_plot_img.getvalue()).decode()




    
        ############### For analysing price trend one item within a selected period ####################

        cursor.execute("SELECT REPLACE(FORMAT(AVG(price),0),',','') as price,DATE(date) as date FROM `tbl_prices` where item=%s and DATE(date) between %s and %s group by DATE(date)",(selected_item,start_date,end_date))
        prices=cursor.fetchall()
        
        dates_labels=[]
        price_labels=[]
        for price in prices:
            price_labels.append(price.get("price"))
        for date in prices:
            dates_labels.append(date.get("date"))

        ############### For analysing price trend of one item with different markets within a selected period ####################

        cursor.execute("select REPLACE(FORMAT(AVG(price),0),',','') as price, B.market from tbl_prices A left join tbl_markets B ON A.market=B.id where item=%s and DATE(date) between %s and %s group by B.market ",(selected_item,start_date,end_date))
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
        labels=json.dumps(dates_labels, default = defaultconverter),
        y=json.dumps(marketprice),
        x=json.dumps(market_label),
        count=json.dumps(count_label),
        item=json.dumps(item_label), form=form, state=itemlist
        )
    
    return redirect(url_for('login'))