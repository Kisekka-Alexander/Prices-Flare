from random import choices
from flask_wtf import Form
from wtforms import StringField, validators,PasswordField,SubmitField,SelectField
from wtforms.fields import DateField

class RegistrationForm(Form):
    username=StringField('Username',[validators.Length(min=4,max=20)])
    email=StringField('Email address',[validators.Length(min=6,max=50)])
    password=PasswordField('Password',[validators.DataRequired(),
                                       validators.EqualTo('confirm', message="Passwords must match")])
    confirm=PasswordField('Repeat password')
    submit = SubmitField('Submit')

class DashboardParamsForm(Form):
    items=SelectField('Item', choices=[('T','Tomatoes'),('C','Cabbages')])
    start_date= DateField('StartDate', format='%Y-%m-%d')
    end_date=DateField('EndDate', format='%Y-%m-%d')

class LoginForm(Form):
    username=StringField('Username',[validators.DataRequired()])
    password=PasswordField('Password',[validators.DataRequired()])