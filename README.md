# CMPE131-Team 13 project

## Table of Contents 
 - [Introduction](#introduction)
 - [List of features/function and who implemented them](#list-of-featuresfunction-and-who-implemented-them)
 - [Instructions on running the project](#instructions-on-running-the-project)
 - [Credits](#credits)

## Introduction 
In this project, we created a website which acts as an email client. Every user will have access to our features of
sending emails, sending chats, and make a todo list once they created an account on our website. 

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
1. First, download the following technologies on the Linux Terminal if you do not have it in your computer
```
sudo apt install python3 (download this first)
pip3 install flask 
pip3 install flask-login
pip3 install flask-sqlachemy
pip3 install flask-wtf
pip3 install git 

2. Clone this project repository into folder of your choice using the following command
```
    git clone https://github.com/kenneth0810/Team-13.git
    
3. Move to the Team-13 directory with this command(assumption of you are currently in the home directory): 
```
   cd Team-13
```
    
4. Set up a database
 a. Run `flask shell`
 b. Copy and paste the code block below
```
from app import db
from app.models import User, Emails, Todo, Profile, Message
db.create_all()
exit()

5. Run the project with the following command: 
```
python3 run.py


## Credits: 
- Yue Ying Lee (@YueYingLee)
- Kenneth Nguyen (@kenneth0810)
- Ruben Martinez-Martinez (@Ruben725)
- Johnny Nguyen (@johnny-txt)