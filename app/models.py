from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    fullname =db.Column(db.String(45), nullable = False)
    password = db.Column(db.String(128), nullable=False)

    emails = db.relationship('Emails', backref = 'user', lazy = 'dynamic')
    todo = db.relationship('Todo', backref = 'user', lazy = 'dynamic')
    profile = db.relationship('Profile', backref = 'user', lazy = 'dynamic')
    #emails_sent = db.relationship('Email', backref='sender', lazy='dynamic')
    #email_recipients = db.relationship('Recipient', backref='user', lazy='dynamic')

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
    

# class emails_recipients (db.Model):
#       __tablename__ = "email_recipients"
#       id = db.Column(db.Integer, primary_key=True)
#       email_id=db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True),
#       recipient_id=db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
#       def __repr__(self):
#        return f'< Recipients id {self.id} Email id: {self.email_id} Recipients: {self.recipient_id}>'

# class Emails(db.Model):
   
#    id = db.Column(db.Integer, primary_key=True)
#    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable =False)
#    recipients_id = db.Column(db.String(200), nullable = False)
  
#    subject_line = db.Column(db.String(100), nullable = False)
#    email_body = db.Column (db.String (1000))
#    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

#    sender = db.relationship("User", foreign_keys=[sender_id])
#    recipient = db.relationship("User", secondary=emails_recipients,
#                                 primaryjoin=(id == emails_recipients.email_id),
#                                 secondaryjoin=(emails_recipients.recipient_id == User.id),
#                                 backref="emails_received")
#    #primary join means between email and email recipients 
#    #secondary join means email_recipiennts and user model 
#    #backref = back reference on user model and allow access the emails received by a user using the emails_received attribute
#    #recipient = db.relationship("User", foreign_keys=[recipients_id])
#    def __repr__(self):
#       return f'< Emails {self.id} Subject: {self.subject_line} Body: {self.email_body}>'

# class Emails(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
#     username = db.Column(db.String(250), nullable=True)
#     subject = db.Column(db.String(255), nullable=False)
#     emaiil_body = db.Column(db.Text, nullable=False)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#     recipients = db.relationship('Recipient', backref='email', lazy='dynamic')

#     def __repr__(self):
#         return f'<Email {self.id} Subject: {self.subject}>'

# class Recipient(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     email_id = db.Column(db.Integer, db.ForeignKey('email.id'), nullable=False)

#     def __repr__(self):
#         return f'<Recipient {self.id}>'
   

class Emails(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable =False)
   subject_line = db.Column(db.String(25), nullable = False)
   email_body = db.Column (db.String (600))
   timestamp = db.Column(db.DateTime, default=datetime.utcnow)

   sender = db.relationship("User", foreign_keys=[sender_id])
   recipients = db.relationship("Recipient", )
   def __repr__(self):
      return f'< Emails {self.id} Subject: {self.subject_line} Body: {self.email_body}>'


# do we need to connec the relationship ? 
class Recipient(db.Model):
    email_id = db.Column(db.Integer, db.ForeignKey(Emails.id), primary_key=True, nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True, nullable=False)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=True)
    subject = db.Column(db.String(250), nullable=False)
    message = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime, nullable=False)

    sending_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiving_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def repr(self):
        return f'{self.id} : {self.subject}'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
