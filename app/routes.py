from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from app.register import registerUser 


@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    name = 'Carlos'
    books = [ {'author': 'authorname1',
                'book':'bookname1'},
             {'author': 'authorname2',
              'book': 'bookname2'}]
    return render_template('hello.html',name=name, books=books)

@myapp_obj.route("/hello")
@login_required
def hello():
    return "Hello World!"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    # create form
    form = LoginForm()
    # if form inputs are valid
    if form.validate_on_submit():
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
        flash(f'Here are the input {form.username.data} and {form.password.data}')
        return redirect('/')
    return render_template('login.html', form=form)

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)

@myapp_obj.route("/register", methods =['GET', 'POST'])
def register():
        #create registration form
        registerForm  = registerUser()
        if registerUser.validate_on_submit():
          same_Username = User.query.filter_by(username = accountForm.username.data).first()
          if same_Username == None:
            user = User(registerForm.fullname.data, registerForm.username.data, registerForm.password.data)
            db.session.add(user)
            db.session.commit()
            #redirect user to login page to log in with their new account
            flash(f'Here are the input {registerForm.username.data}, {registerForm.fullname.data} and {registerForm.password.data}')
            return redirect('/login')
          else :
              flash('The username is not available. Please choose another username')
        return render_template('register.html', registerForm=registerForm)
