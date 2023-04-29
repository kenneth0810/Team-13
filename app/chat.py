from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ChatForm(FlaskForm):
    recipient_name = StringField('Recipient', validators=[DataRequired()])
    username = StringField('Username')
    subject = StringField('Subject', validators=[DataRequired(), Length (min=1, max = 100)])
    message = TextAreaField('Message', validators=[DataRequired(), Length (min = 1, max = 5000)])
    submit = SubmitField('Send')