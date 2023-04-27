from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class registerUser(FlaskForm):
 fullname = StringField('Full Name', validators = [DataRequired(), Length (min = 4, max = 10)])
 username = StringField('Username',validators =[DataRequired(), Length (min = 6, max = 15)])
 password = PasswordField('New password', validators = [DataRequired(), Length (min=4, max =10)])
 confirm = PasswordField (label='Confirm password', validators = [DataRequired(), EqualTo('password', message='Passwords must match')])
 submit = SubmitField ("Register") 
