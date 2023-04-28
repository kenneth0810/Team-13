from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class BioForm(FlaskForm):
    bio = StringField("Bio:", validators = [DataRequired()])
    submit = SubmitField("Save and Update")

class PasswordForm(FlaskForm):
    old_password = PasswordField("Enter your old password", validators = [DataRequired()])
    new_password = PasswordField("Enter a new password", validators = [DataRequired()])
    submit = SubmitField("Update Password")