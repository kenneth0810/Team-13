from app import db
from datetime import datetime
from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    fullname =db.Column(db.String(45), nullable = False)
    password = db.Column(db.String(128), nullable=False)
  
    sent_emails = db.relationship('Emails', backref='sender', foreign_keys='Emails.sender_id', lazy = 'dynamic')
    received_emails = db.relationship('Emails', backref='recipient', foreign_keys='Emails.recipient_id', lazy = 'dynamic')

    note = db.relationship('Note', backref = 'user', lazy = 'dynamic')
    todo = db.relationship('Todo', backref = 'user', lazy = 'dynamic')
    profile = db.relationship('Profile', backref = 'user', lazy = 'dynamic')   

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        print("self.password is: ")
        print(self.password)
        print("input password is: ")
        print(password)
        return check_password_hash(self.password, password)

    def __repr__(self): #for debugging process
        return f'<user {self.id}: {self.username}, {self.fullname}>'
    

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject= db.Column(db.String(1000), nullable=False)
    email_body = db.Column(db.String(5000), nullable = False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    sender_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    sender_username=db.Column(db.String(1000), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_username= db.Column(db.String(1000), nullable=False)

    def __repr__(self): #for debugging process
        return f'<emails {self.id}: {self.subject}, {self.message}>'
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    timestamp = db.Column(db.DateTime, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    task = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, nullable=False)
    finished = db.Column(db.Boolean, nullable=False)
    favorite = db.Column(db.Boolean, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class ChatRoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.String(50), unique=True, nullable=False)
    users = db.Column(db.String)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))