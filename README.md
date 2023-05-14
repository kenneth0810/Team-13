# CMPE131-Team 13 project

## Table of Contents 
 - [Introduction](#introduction)
 - [List of features/function and who implemented them](#list-of-featuresfunction-and-who-implemented-them)
 - [Instructions on running the project](#instructions-on-running-the-project)
 - [Credits](#credits)

## Introduction 
In this project, we created a website **EMTOCHA**, which acts as an email client (**EM**) while having special features of making a todo list (**TO**) and sending chat messages (**CHA**) by joining chat rooms that they are interested in. Every user will have access to these features once they created an account on our website. 

![Alt text] (static/131_logo.jpg?raw=true)

## List of features/functions and who implemented them 
1. Register an email account (Yue Ying)
2. Login/Logout (Yue Ying)
3. Send emails (Yue Ying)
4. Sort emails (Ruben)
5. Search emails (Ruben)
6. Send chat messages (Johnny)
7. Delete chat messages (Johnny)
8. Add TO DO component (Kenneth)
9. Delete TO DO component (Kenneth)
10. Edit user profile (Kenneth)
11. Search chat messages (Johnny)
12. Delete account (Ruben)

## Instructions on running the project
1. Make a folder with the name of your choice and navigate to that folder. 

2. Before activating virtual environment, download these technologies on the Linux Terminal if you do not have it in your computer. 
- Note: If you do not want to use virtual environment, only perform step 1, step2, skip to step 5 and perform steps from 5 to 9 only. 
```
sudo apt install python3
apt install python3-pip
apt install python3.10-venv
apt-get install git
```

3. Create a virtual environment by using the following command to ensure that the required packages are installed locally and independently of other projects on your computer. This helps avoid version conflicts and makes it easier to manage project dependencies. (myenv is the name of the virtual environment)
```
python3 -m venv myenv
```

4. Activate the virtual environment
- On MacOs or Unix, run: ```source myenv/bin/activate```
- On Windows, run: ```myenv\Scripts\activate.bat```

5. Install the necessary packages: 
```
pip3 install flask
pip3 install flask_sqlalchemy
pip3 install flask_login
pip3 install flask_socketio
pip3 install flask_wtf
```
6.  Clone this project repository into folder of your choice using the following command
```
    git clone https://github.com/kenneth0810/Team-13.git
```

7. Move to the Team-13 directory with this command(assumption of you are currently in your choice of folder): 
```
   cd Team-13
```
    
8. Set up a database

 a. Run `flask shell`

 b. Copy and paste the code block below

```
from app import db
from app.models import User, Emails, Note, Todo, Profile, ChatRoom
db.create_all()
exit()
```

9. Run the project with the following command and explore our features!
- Note: You will see a website link such as ```http://127.0.0.1:5000```
When you are testing our chat features with two users, make sure you use two different browser/tab (One of them being incognito window or Microsoft edge and the other in Google Chrome)
```
python3 run.py
```
10. Once you are done exploring our website, deactivate the virtual environment: 
```deactivate ```
## Credits: 
- Yue Ying Lee (@YueYingLee)
- Kenneth Nguyen (@kenneth0810)
- Ruben Martinez-Martinez (@Ruben725)
- Johnny Nguyen (@johnny-txt)

