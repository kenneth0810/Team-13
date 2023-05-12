from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class sendEmails(FlaskForm):
    recipients = StringField('Recipients email: ', validators = [DataRequired()],render_kw ={"placeholder":" Ex: user2@131.com (use , to separate multiple recipients)"})
    subject = StringField('Subject:', validators=[DataRequired()],render_kw ={"placeholder":" Subject"})
    email_body = TextAreaField('Body:', validators=[DataRequired()], render_kw ={"placeholder":"Input text"})
    submit = SubmitField('Send')
