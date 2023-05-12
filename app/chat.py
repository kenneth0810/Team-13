from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length

class CreateRoomForm(FlaskForm):
    room_id = StringField('Create Room Code', validators=[DataRequired(), Length(min=5, max=5)])
    submit = SubmitField('Create Chat Room')

class JoinRoomForm(FlaskForm):
    valid_room_id = StringField('Enter Room Code', validators=[DataRequired(), Length(min=5, max=5)])
    submit = SubmitField('Join Chat Room')

class SendMessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=5000)])
    sender_id = HiddenField('Sender ID', validators=[DataRequired()])
    chat_room_id = HiddenField('Chat Room ID', validators=[DataRequired()])
    submit = SubmitField('Send')