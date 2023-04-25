from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class registerForm(FlaskForm):
 fullname = StringField('Full Name', validators = [DataRequired(), Length (min = 4, max = 10)])
 username = StringField('Username',validators =[DataRequired(), Length (min = 6, max = 15)])
 password = PasswordField('New password', validators = [DataRequired(), Length (min=4, max =10),EqualTo('confirm', message='Passwords must match')])
 confirm = PasswordField ('Confirm password')
 submit = SubmitField ("Register") 
