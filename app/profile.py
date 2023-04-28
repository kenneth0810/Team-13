from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class ProfileForm(FlaskForm):
    bio = StringField("Bio:", validators = [DataRequired()])
    submit = SubmitField("Save and Update")