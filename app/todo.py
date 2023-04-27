from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    task = StringField("Create Task", validators = [DataRequired()])
    submit = SubmitField("Add Task")