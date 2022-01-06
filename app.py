from flask import Flask,render_template, request
from flask.helpers import url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os, json, datetime
from flask_wtf import Form
from wtforms import StringField, validators,PasswordField,SubmitField
from flask_bootstrap import Bootstrap
from passlib.hash import sha256_crypt
from Forms import RegistrationForm, DashboardParamsForm
# from MySQLdb import escape_string as thwwart

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'us-cdbr-east-04.cleardb.com'
app.config['MYSQL_USER'] = 'b376dadf004332'
app.config['MYSQL_PASSWORD'] = '85e2d67e'
app.config['MYSQL_DB'] = 'heroku_5443e697ebea265'
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

@app.route('/register', methods = ['POST', 'GET'])
def register():
   form=RegistrationForm(request.form)
   if request.method=='POST' and form.validate():
       username= form.username.data
       email=form.email.data
       password= sha256_crypt.encrypt((str(form.password.data)))

       cursor = mysql.connection.cursor()
       cursor.execute(''' INSERT INTO tbl_users VALUES(%s,%s,%s,%s)''',(username,email,password,""))
       mysql.connection.commit()
       cursor.close()
       return f"Done!!"
   return render_template("register.html",form=form)   

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
    #creating variable for connection
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #executing query
    cursor.execute("SELECT *,FORMAT((@row_number:=@row_number + 1),0) AS row_num  FROM tbl_markets,(SELECT @row_number:=0) AS temp")
    #fetching all records from database
    data=cursor.fetchall()
    #returning back to subscriber.html with all records from MySQL which are stored in variable data
    return render_template("markets.html",markets=data)

@app.route('/items',methods=['GET','POST'])
def item():
    #creating variable for connection
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #executing query
    cursor.execute("SELECT *,FORMAT((@row_number:=@row_number + 1),0) AS row_num  FROM tbl_items,(SELECT @row_number:=0) AS temp")
    #fetching all records from database
    data=cursor.fetchall()
    #returning back to subscriber.html with all records from MySQL which are stored in variable data
    return render_template("items.html",items=data)

@app.route('/',methods=['GET','POST'])
def dashboard():
    form=DashboardParamsForm(request.form)
    startdate=form.start_date.data
    enddate=form.end_date.data
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT REPLACE(FORMAT(AVG(price),0),',','') as price,DATE(date) as date FROM `tbl_prices` where DATE(date) between %s and %s group by date",(startdate,enddate))
    prices=cursor.fetchall()
    
    dates_labels=[]
    price_labels=[]
    for price in prices:
           price_labels.append(price.get("price"))
    for date in prices:
           dates_labels.append(date.get("date"))

    ################ For Checks ##################
    cursor.execute("SELECT COUNT(a.item)count,b.item FROM tbl_prices a left join tbl_items b on a.Item=b.ID where iscomplete=1  GROUP by b.Item")
    checks=cursor.fetchall()
    count_label=[]
    item_label=[]
    for item in checks:
           item_label.append(item.get("item"))
    for count in checks:
           count_label.append(count.get("count"))


    return render_template("dashboard.html", 
    values=json.dumps(price_labels), 
    labels=json.dumps(dates_labels, default = defaultconverter),
    y=json.dumps(price_labels),
    x=json.dumps(dates_labels, default = defaultconverter),
    count=json.dumps(count_label),
    item=json.dumps(item_label), form=form)
    