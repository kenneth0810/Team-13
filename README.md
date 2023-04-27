# CMPE131-Team 13 project
- Yue Ying Lee (@YueYingLee)
- Kenneth Nguyen (@kenneth0810)
- Ruben Martinez-Martinez (@Ruben725)
- Johnny Nguyen (@johnny-txt)

# Instructions on how to set up Python database
1. Navigate to the project folder
2. Run `flask shell`
3. Copy paste the code block below
```
from app import db
from app.models import User, Emails
db.create_all()

user1 = User(fullname='user1', username='user1@131.com')
user1.set_password('user1pass')


user2 = User(fullname='user2', username='user2@131.com')
user2.set_password('user2pass')

db.session.add(user1)
db.session.add(user2)
db.session.commit()

exit()

```