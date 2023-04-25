from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname =db.Column(db.String(10), nullable = False)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<user {self.id}: {self.username}>''

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
