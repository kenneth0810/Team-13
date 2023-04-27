from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProfileForm(FlaskForm):
    bio = StringField("Change Bio", validators = [DataRequired()])
    submit = SubmitField("Save")