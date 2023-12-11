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


class AddMarketForm(Form):
    marketname=StringField('Market')
    marketcode=StringField('Code')
    submit = SubmitField('Submit')

class AddItemForm(Form):
    itemname=StringField('Item')
    itemcode=StringField('Code')
    unitofmeasure=StringField('Unit Of Measure')
    submit = SubmitField('Submit')

class LoginForm(Form):
    username=StringField('Username',[validators.DataRequired()])
    password=PasswordField('Password',[validators.DataRequired()])

class DashboardParamsForm(Form):
    start_date= DateField('StartDate', format='%Y-%m-%d')
    end_date=DateField('EndDate', format='%Y-%m-%d')
    item = SelectField(u'Select Item', coerce=int)