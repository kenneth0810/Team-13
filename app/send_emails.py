from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class sendEmails(FlaskForm):
    recipients = StringField('Recipients email: ', validators = [DataRequired()],render_kw ={"placeholder":" Ex:user2@131.com"})
    subject_line = StringField('Subject:', validators=[DataRequired()],render_kw ={"placeholder":" Input your email subject"})
    email_body = TextAreaField('Body:', validators=[DataRequired()])
    submit = SubmitField('Send')
