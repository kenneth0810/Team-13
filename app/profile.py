from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from flask_login import current_user
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash

class BioForm(FlaskForm):
    bio = StringField("Bio:", validators = [DataRequired(), Length(max=100)], render_kw ={"placeholder":"Add your bio"})
    submit = SubmitField("Save Bio")

class PasswordForm(FlaskForm):
    old_password = PasswordField("Enter your old password", validators = [DataRequired()])
    new_password = PasswordField("Enter a new password", validators = [DataRequired(), Length (min=4, max=10)])
    confirm = PasswordField("Confirm your new password", validators=[DataRequired()])
    submit = SubmitField("Update Password")

    def validate_old_password(self, form):
        if not check_password_hash(current_user.password, form.data):
            raise ValidationError('Incorrect old password')
        if form.data == self.new_password.data:
            raise ValidationError('Old and new passwords cannot be the same')
        if self.new_password.data != self.confirm.data:
            raise ValidationError('Passwords do not match')

class DeleteForm(FlaskForm):
    password = PasswordField('Enter your password', validators=[DataRequired()])
    submit = SubmitField('Delete Account')

    def validate_password(self, form):
        if not check_password_hash(current_user.password, form.data):
            raise ValidationError('Incorrect password')
