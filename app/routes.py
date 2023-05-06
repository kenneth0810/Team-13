from flask import render_template
from flask import redirect, request, session, url_for
from flask import flash
from app import myapp_obj, db
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from datetime import datetime

from wtforms.validators import Email
#from app.reply_emails import replyEmails
from app.send_emails import sendEmails
from app.register import registerUser 
from app.models import User, Emails, Todo, Profile, Message
from app.login import LoginForm
from app.todo import TodoForm
from app.profile import BioForm, PasswordForm, DeleteForm
from app.chat import ChatForm

#Yue Ying Lee
# index page is the page user see before registering or logging in
@myapp_obj.route("/")
def index():
    return render_template('index.html' )

#Yue Ying Lee
@myapp_obj.route("/homepage")
@login_required
def homepage():
    user = current_user
    user_fullname = user.fullname
    return render_template('homepage.html', user_fullname = user_fullname)

#Yue Ying Lee
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    # create form
    form = LoginForm()
    if form.validate_on_submit():
        valid_user = User.query.filter_by(username = form.username.data).first()
        if valid_user != None:
          if valid_user.check_password(form.password.data)== True:
             login_user(valid_user)
             flash(f'Here are the input {form.username.data} and {form.password.data}')
             return redirect(url_for('homepage'))
          else :
             flash(f'Invalid password. Try again')
        else: 
             flash(f'Invalid username. Try again or register an account')  

    return render_template('login.html', form=form)

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)

#Yue Ying Lee
@myapp_obj.route("/logout", methods = ['GET', 'POST'])
@login_required
def logout():
       logout_user()
       return redirect(url_for('login'))

#Yue Ying Lee
@myapp_obj.route("/register", methods =['GET', 'POST'])
def register():
        #create registration form
        registerForm  = registerUser()
        if registerForm.validate_on_submit():
          same_Username = User.query.filter_by(username = registerForm.username.data).first()
          if same_Username == None:
            user = User(fullname = registerForm.fullname.data, username= registerForm.username.data)
            user.set_password(registerForm.password.data)
            db.session.add(user)
            db.session.commit()
            #redirect user to login page to log in with their new account
            flash(f'Here are the input {registerForm.username.data}, {registerForm.fullname.data} and {registerForm.password.data}')
            return redirect('/login')
          else :
             flash('The username is not available. Please choose another username')
        return render_template('register.html', registerForm=registerForm)


#Yue Ying Lee
@myapp_obj.route("/send_emails", methods = ['GET', 'POST'])
@login_required
def send_emails():
   send_emails_form = sendEmails()
   if send_emails_form.validate_on_submit():
    sender_id = current_user.id
    recipients_list = send_emails_form.recipients.data.split(',')
    print("recipients_list is: ")
    print(recipients_list)
    valid_recipients = [] 
    for recipient in recipients_list:
     valid_recipient =  User.query.filter_by(username = recipient.strip()).first()
     if (valid_recipient):
        recipient_username= valid_recipient.username
        flash(f' Valid recipients: {valid_recipient.username}')
        recipient_id = valid_recipient.id
        
        email = Emails (recipient_username = recipient_username, sender_username =  current_user.username, sender_id = sender_id, recipient_id = recipient_id, subject=send_emails_form.subject.data, email_body= send_emails_form.email_body.data)
        db.session.add(email)
        valid_recipients.append(valid_recipient)
    if valid_recipients:
        db.session.commit()
        flash(f'Email successfully sent to {", ".join([r.username for r in valid_recipients])}!')
        return redirect('/homepage')
    else:
     flash(f' Invalid recipients. Retype username or go back to homepage.')

   return render_template('send_emails.html', send_emails_form = send_emails_form)

'''
view emails need to modify so next time i can reply in the emails '''
#YueYingLee
@myapp_obj.route("/view_emails", methods = ['GET', 'POST'])
@login_required
def view_emails():
    emails = Emails.query.filter_by(recipient_id = current_user.id).all()
    return render_template('view_emails.html', user=current_user, emails = emails)


'''reply email 
from original email page, click reply 
pops to reply email template: 
to: origial sender email 
subject: RE: original subject 
message: show original email body 

textbox: to enter reply 
'''




# #Yue Ying Lee
# @myapp_obj.route('/reply_email/<int:email_id>', methods=['GET','POST'])
# @login_required
# def reply_emails():
#     reply_emails_form = replyEmails() 
# def reply(message_id):
#     message = Emails.query.get_or_404(message_id)
#     task = Todo.query.filter(Todo.id == id).first()
#     form = ReplyForm()
#     if form.validate_on_submit():
#         recipient = User.query.filter_by(email=form.recipient.data).first()
#         if not recipient:
#             flash('Invalid recipient email address.')
#             return redirect(url_for('reply', message_id=message_id))
#         elif not form.body.data.strip():
#             flash('Message body cannot be empty.')
#             return redirect(url_for('reply', message_id=message_id))
#         reply = Emails(
#             sender_id=current_user.id,
#             recipient_id=recipient.id,
#             subject=form.subject.data,
#             email_body=form.body.data,
#             parent_id=message_id
#         )
#         db.session.add(reply)
#         db.session.commit()
#         flash('Your reply has been sent.')
#         return redirect(url_for('thread', message_id=message_id))

#     return render_template('reply_emails.html', reply_emails_form = reply_emails_form)

'''@myapp_obj.route("/reply_email/<int:email_id>", methods=["GET", "POST"])
@login_required
def reply_email(email_id):
    email = Emails.query.get(email_id)
    if not email:
        flash("Invalid email ID.")
        return redirect("/inbox")
    if email.recipient_id != current_user.id:
        flash("You are not authorized to reply to this email.")
        return redirect("/inbox")

    reply_form = sendEmails()
    if reply_form.validate_on_submit():
        sender_id = current_user.id
        recipient_id = email.sender_id
        subject = "RE: " + email.subject
        email_body = reply_form.email_body.data

        reply_email = Emails(
            recipient_id=recipient_id,
            sender_id=sender_id,
            subject=subject,
            email_body=email_body,
            parent_email_id=email.id,
        )
        db.session.add(reply_email)
        db.session.commit()

        flash("Reply sent successfully!")
        return redirect("/inbox")

    reply_form.email_body.data = f"\n\n\n---- Original Message ----\n{email.email_body}"
    return render_template("send_emails.html", send_emails_form=reply_form)
'''

#kenneth
@myapp_obj.route("/todo", methods = ['GET', 'POST'])
@login_required
def add_todo():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(user = current_user, task = form.task.data, timestamp=datetime.now())
        db.session.add(todo)
        db.session.commit()
        flash('Successfully added a new task.')
        return redirect(url_for('add_todo'))

    user = current_user
    all_tasks = Todo.query.all()
    task_list = [] #a list to append all exisiting tasks for current user to be passed into the html file
    for t in all_tasks:
        if t.user_id == user.id:
            task_list.append(t)
    return render_template("todo.html", form=form, tasks=task_list, user=user)

#kenneth
@myapp_obj.route('/delete-task/<int:id>', methods=['GET','POST'])
@login_required
def delete_task(id):
    task = Todo.query.filter(Todo.id == id).first()
    if task:
        db.session.delete(task) 
        db.session.commit()
        flash('Task deleted')
    else:
        flash('There is no task to be deleted.')
    return redirect(url_for('add_todo'))

#kenneth
@myapp_obj.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    bio_form = BioForm()
    if bio_form.validate_on_submit() and request.method == "POST":
        #if a current bio exists and a new bio is submitted, delete the current bio and replace it with the new bio
        curr_bio = Profile.query.filter_by(user=current_user).first()
        if curr_bio:
            db.session.delete(curr_bio)
        new_bio = Profile(user=current_user, bio=bio_form.bio.data)
        db.session.add(new_bio)
        db.session.commit()
        flash('Successfully updated a new bio.')
        return redirect(url_for('profile'))
    else:
        #if nothing is submitted, the bio form will be empty, so assign the form.bio to the current bio
        curr_bio = Profile.query.filter_by(user=current_user).first()
        if curr_bio:
            bio_form.bio.data = curr_bio.bio
    
    pw_form = PasswordForm()
    if pw_form.validate_on_submit() and request.method == "POST":
        user = current_user
        if user.check_password(pw_form.old_password.data):
            if not user.check_password(pw_form.new_password.data):
                user.set_password(pw_form.new_password.data)
                db.session.commit()
                flash('Successfully updated password.')
                return redirect(url_for('profile'))
    
    #find all items associated with the current_user and delete them
    delete_form = DeleteForm()
    if delete_form.validate_on_submit() and request.method == "POST":
        user = current_user
        if user.check_password(delete_form.password.data):
            deleteTodo = Todo.query.filter_by(user=current_user).all()
            for item in deleteTodo:
                delete_task(item.id)

            b = Profile.query.filter_by(user=current_user).first()
            if b:
                delete_bio(b.user_id)

            m = Message.query.filter_by(username=current_user.username).all()
            for message in m:
                db.session.delete(message)
                db.session.commit()

            e = Emails.query.filter_by(sender_id=current_user.id).all()
            for emails in e:
                db.session.delete(emails)
                db.session.commit()

            db.session.delete(user)
            db.session.commit()
            logout_user
            flash('Successfully deleted account.')
            return redirect(url_for('login'))
        else:
            flash('wrong password!')
    return render_template('profile.html', bform=bio_form, pform=pw_form, user=current_user, dform=delete_form)

#kenneth
@myapp_obj.route('/delete-bio/<int:id>', methods=['GET','POST'])
@login_required
def delete_bio(id):
    b = Profile.query.filter(Profile.user_id == id).first()
    if b:
        db.session.delete(b) 
        db.session.commit()
        flash('Successfully deleted bio')
    else:
        flash('There is no bio to be deleted.')
    return redirect(url_for('profile'))
    
@myapp_obj.route('/chat', methods=['GET', 'POST'])
@login_required
def start_chat():
    form = ChatForm()
    if form.validate_on_submit():
        recipients = []
        for recipient_name in form.recipient_name.data:
            recipient = User.query.filter_by(username=recipient_name).first()
            if recipient is None:
                continue
            recipients.append(recipient)
        if not recipients:
            flash('At least one recipient must be entered.')
        else:
            dateAndTime = datetime.now()
            for recipient in recipients:
                message = Message(
                    username=current_user.username,
                    subject=form.subject.data,
                    message=form.message.data,
                    sending_user=current_user.id, 
                    receiving_user=recipient.id,
                    timestamp=dateAndTime
                )
                db.session.add(message)
            db.session.commit()
            flash('Message sent successfully!')
            return redirect(url_for('start_chat'))
    messages = Message.query.filter_by(receiving_user=current_user.id).all()
    return render_template('chat.html', user=current_user, form=form, messages=messages)

@myapp_obj.route('/chat/<int:id>', methods=['POST'])
@login_required
def delete_chat(id):
    message = Message.query.filter(Message.id == id, Message.receiving_user == current_user.id).first()
    if message:
        db.session.delete(message)
        db.session.commit()
        flash('Chat deleted', category='success')
        return redirect(url_for('start_chat'))
    else:
        flash('There is no chat to be deleted')
        return redirect(url_for('start_chat'))
    
@myapp_obj.route('/chat/search', methods=['POST'])
def search_messages():
    search_type = request.form.get('search_type')
    search_term = request.form.get('search_term')
    messages = Message.query.filter_by(receiving_user=current_user.id).all()
    if search_type == 'from_user':
        messages = [msg for msg in messages if search_term.lower() in msg.username.lower()]
    elif search_type == 'subject':
        messages = [msg for msg in messages if search_term.lower() in msg.subject.lower()]
    elif search_type == 'message':
        messages = [msg for msg in messages if search_term.lower() in msg.message.lower()]
    return render_template('chat.html', form=ChatForm(), messages=messages)