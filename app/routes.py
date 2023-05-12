from flask import render_template
from flask import redirect, request, session, url_for
from flask import flash, get_flashed_messages
from app import myapp_obj, db, socketio
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_socketio import join_room, leave_room, emit
from datetime import datetime

from wtforms.validators import Email
#from app.reply_emails import replyEmails
from app.send_emails import sendEmails
from app.register import registerUser 
from app.models import User, Emails, Todo, Profile, Message, ChatRoom
from app.login import LoginForm
from app.todo import TodoForm
from app.profile import BioForm, PasswordForm, DeleteForm
from app.chat import CreateRoomForm, JoinRoomForm, SendMessageForm

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
        todo = Todo(user = current_user, task = form.task.data, timestamp=datetime.now(), finished=False, favorite=False)
        db.session.add(todo)
        db.session.commit()
        flash('Successfully added a new task.')
        return redirect(url_for('add_todo'))

    user = current_user
    all_tasks = Todo.query.filter(Todo.user_id == current_user.id).all()
    fav_list = []
    not_fav_list = []
    for t in all_tasks:
        if t.favorite == True:
            fav_list.append(t)
        else:
            not_fav_list.append(t)
    return render_template("todo.html", form=form, fav_list=fav_list, not_fav_list=not_fav_list, user=user)

#kenneth
@myapp_obj.route("/finish-task/<int:id>", methods = ['GET', 'POST'])
@login_required
def finish_task(id):
    task = Todo.query.filter(Todo.id == id). first()
    if not task.finished:
        task.finished = True
    else:
        task.finished = False
    db.session.commit()
    return redirect(url_for('add_todo'))

#kenneth
@myapp_obj.route("/favorite-task/<int:id>", methods = ['GET', 'POST'])
@login_required
def favorite_task(id):
    task = Todo.query.filter(Todo.id == id). first()
    if not task.favorite:
        task.favorite = True
    else:
        task.favorite = False
    db.session.commit()
    return redirect(url_for('add_todo'))

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
def chatroom():
    if request.method == 'GET':
        create_form = CreateRoomForm()
        join_form = JoinRoomForm()
    else:
        create_form = CreateRoomForm(request.form)
        join_form = JoinRoomForm(request.form)

    if create_form.validate_on_submit():
        room_id = create_form.room_id.data
        chat_room = ChatRoom.query.filter_by(room_id=room_id).first()
        if chat_room:
            flash('Chat room with the same ID already exists. Please choose a different ID.', 'error')
            return redirect(url_for('chatroom'))
        else:
            chat_room = ChatRoom(room_id=room_id)
            db.session.add(chat_room)
            db.session.commit()
            return redirect(url_for('room', room_code=create_form.room_id.data))
            
    if join_form.validate_on_submit():
        valid_id = join_form.valid_room_id.data
        chat_room = ChatRoom.query.filter_by(room_id=valid_id).first()
        if chat_room:
            return redirect(url_for('room', room_code=join_form.valid_room_id.data))
        else:
            flash('Invalid chat room code. Please try again.', 'error')
            return redirect(url_for('chatroom'))

    return render_template('chat.html', create_form=create_form, join_form=join_form)

@myapp_obj.route('/chat/<room_code>/delete', methods=['POST'])
@login_required
def deletechatroom(room_code):
    chat_room = ChatRoom.query.filter_by(room_id=room_code).first()
    if chat_room:
        db.session.delete(chat_room)
        db.session.commit()
        flash('Chat room has been deleted', 'success')
    return redirect(url_for('chatroom'))

@myapp_obj.route('/room/<string:room_code>')
@login_required
def room(room_code):
    return render_template('room.html', room_code=room_code)

@socketio.on('message')
def handle_message(message):
    emit('message', {'name': current_user.fullname, 'message': message}, broadcast=True)

@socketio.on('join')
def handle_join(data):
    join_room(data['room'])
    emit('join_message', {'name': current_user.fullname, 'message': ' has entered the room.'}, room=data['room'])

@socketio.on('leave')
def handle_leave(data):
    leave_room(['room'])
    emit('leave_message', {'name': current_user.fullname, 'message': ' has left the room.'}, room=data['room'])