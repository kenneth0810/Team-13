from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FieldList
from wtforms.validators import DataRequired, Length, ValidationError

class AtLeastOneRecipient(object):
    def __call__(self, form, field):
        if not any(field.entries):
            raise ValidationError('At least one recipient is required.')

class ChatForm(FlaskForm):
    recipient_name = FieldList(StringField('Recipient'), min_entries=5, validators=[AtLeastOneRecipient()])
    username = StringField('Username')
    subject = StringField('Subject', validators=[DataRequired(), Length(min=1, max=100)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=1, max=5000)])
    submit = SubmitField('Send')