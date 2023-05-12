from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class NoteForm(FlaskForm):
    name = StringField("Note Name", validators = [DataRequired(), Length(max=30)], render_kw ={"placeholder":"Enter a name for your note (Max: 30 characters)"})
    submit = SubmitField("Create Note")