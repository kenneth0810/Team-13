## Functional Requirements 

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

## Non-functional requirement
1.  The website is only expected to work on Google Chrome. 
2.  The website has UI interactive interface (for using elements from bootstrap). 

## Use Cases 

**1. Use case name: Register an email account**

**Pre condition:**

- The user has prepared their full name, username, and password they want to use. 
- The user has not registered for an account on the website before with the username.

**Trigger:** The user selects the “Register new email account”option. 

**Primary Sequence:**
1. The system prompts the user to enter their full name, username, and password. 
2. The user enters their full name, username, and password following the guidelines. 
3. The system shows the availability of the username to the user.
4. The system reenters their password for confirmation.
5. The system checks for any missing field of information of the user. The user will be prompted to continue to enter if there is any missing field.  
6. The user clicks the “Register” option to register an email account. 
7. The system displays a message to indicate the user has successfully registered for an account. 
8. The user will be automatically redirected to log in page on the website. 

**Primary Postconditions:**
- The user has successfully registered an account on the website and has access to the features of the website. 
- The website’s database saves the user’s account information. 

**Alternate Sequence #1:** 
The user enters a username that has already been registered on the website.
- The system displays an error message indicating the username has been registered to a user already. 
- The system prompts the user to enter a different username or to quit the registration page to log in instead. 
- The user either enter a different username or quit to log in instead. 

**Alternate Sequence #2:**
The user enters confirmation passwords wrongly.
- The system displays an error message indicating the confirmation password does not match. 
- The system prompts the user to reenter the confirmation password. 
- The user renters the confirmation password. 

**2. Use case name: Login/Logout**

**Pre condition:**
- The user already registered an account on this website. 
- The user has prepared the username and password of their account.

**Trigger:**
- The user clicks the “Login ” option.

**Primary Sequence:**
1. The system prompts the user to enter their username and password. 
2. The user enters their username and password. 
3. The system checks if there is any missing field. 
4. The user will be prompted to continue to enter if there is any missing field.  
5. The user clicks on “Login” button. 
6. The system checks if the username and password entered are correct.
7. The user will be automatically redirected to their profile page when the information are correct.
8. The user clicks on "Log out" button. 
9. The system logs out the user from their email account.

**Primary Postconditions:**
- The system has verified the information of the user and gives access to the user. 
- The user has been successfully logged into their account and has access to the features of the website. 
- The user has been successfully logged out their account. 

**Alternate Sequence:** The user enters the wrong password or username. 
- The system displays an error message indicating an unsuccessful login request to the user.  
- The system prompts users to reenter the username or password or register instead.  
- The user either reenter their username or password or choose to register. 

**3. Use case name: Send emails**

**Pre condition:**
- The user is logged in to their email account. 
- The user has prepared the contents of the email and know who they want to send to. 
- The user is on the homepage of the website. 

**Trigger:** The user selects the “Send an email” option on the menu bar. 

**Primary Sequence:**
1. The user is redirected to the drafting email window. 
2. The system prompts the user to enter the recipients’ username(email address), subject line, and the content of the email. 
3. The user enters the emails body and the username (email address) they want to send to with an option of sending to one or multiple recipients. 
4. The system checks if the recipients’ usernames are entered correctly. 
5. The user clicks on “Send” button to send email.
6. The system prompts the user to confirm sending the email.
7. The user confirms sending the email.
8. The system sends the email to the recipients. 
9. The system displays a confirmation message indicating the success of sending emails. 
10. The user is redirected to the homepage.

**Primary Postconditions:**
- The user successfully sends the emails to the recipients they chose. 
- The system has a record of the user’s sent emails. 
- The recipients received the emails. 

**Alternate Sequence #1:** The user entered invalid recipients’ usernames (email address). 
- The system displays an error message indicating the recipient entered does not exist. 
- The system prompts the user to re-enter the recipients’ usernames.
- The user either reenters the recipients’ usernames or quits the sending email function. 

**Alternate Sequence #2:** The user did not enter the subject line, usernames, or email content.
- The system displays an error message and prompts users to enter information on the missing field or quit the sending email function. 
- The user will enter the information of the missing field or quits the drafting email window. 

**4. Use case name: Send chat messages**

**Pre condition:**
- The user is logged into their account.
- The user is on the chat message page.

**Trigger:**
- The user clicks the "Chat" button.

**Primary Sequence:**
1. The user clicks on the chat button on the chat message page to see all their chats.
2. The user clicks on the "start a group chat" button.
3. The system prompts the user to enter multiple existing usernames(email addresses) and clicks "start chat."
4. The user see a chat box appear with a text entry at the bottom of the page.
5. The user input any text they want in the text entry box.
6. The user clicks the "send" arrow to successfully send their message to the group chat.

**Primary Postconditions:**
- The user(sender) will see that their text shown in the chat history log of the chat page.
- The user and the recipients in the group chat will see the new messages sent by the user in the chat history log of the chat page. 

**Alternate Sequence #1:** The user enters nothing in the text box.
- The system shows errors and not allow the user to send a message.
- The system prompts the user to enter message or quit the chat.

**Alternate Sequence #2:** The user enters an invalid username(email address). 
- The system displays an error message that indicates the entered username does not exist and prompts the user to reenter a valid recipient username.
- The user either reenters a valid recipient email to add to the group chat or create a group chat without adding anybody else.

**5. Use case name: Delete Chat Messages**

**Pre condition:** 
- The user is logged into their account.
- The user is on the chat window and the message exists.

**Trigger:** 
- The user right clicks on the chat message and click on “Delete” button.

**Primary Sequence:**
1. The system prompts the user with a confirmation dialog box, asking their confirmation on deleting the message or cancel.
2. The user clicks "Yes" to confirm the deletion. 
3. The system removes the message from the chat conversation.

**Primary Postconditions:**
- The user (sender & receipient) see that the specified message has disappeared from the chat window. 
- The website’s database has remove the user’s chat history of the specific message. 

**Alternate Sequence #1:** The user attempts to delete a message from the recipient.
- The system does not pop out the delete button to delete the message.

**Alternate Sequence #2:** The user clicks the “No” option from the confirmation dialog box.
- The system exit out of the delete confirmation dialog box.
- The user see the message remains in the chat window.

**6. Use case name: Add a TODO component**

**Pre-condition:**
- The user must be logged in. 
- The user is on their TODO page.

**Trigger:**
- The user selects the “Add” option.

**Primary Sequence:**
1. The system prompts user to enter a task to do.
2. The user can enter in text to add to do component to their todo list.
3. The user confirms and adds the task into the todo list.
4. The system saves and updates the user’s inputs in the todo list. 

**Primary Postconditions:**
- A new TODO task is created and saved in the user’s account.
- The user will automatically be redirected to the the TODO page to see all tasks.

**Alternate Sequence #1:** The user entered nothing in the TODO list.
- The system does not save the todo list.
- The system prompts for something to be entered into the text box.

**7. Use case name: Edit User Profile**

**Pre-condition:** 
- The user must be logged in.
- The user is on their profile page.

**Trigger:** 
- The user selects the “Edit profile” option on the user profile page.

**Primary Sequence:**
1. The system displays a window showing all the information (such as full name, password, and biography).
2. The user adds, deletes, or modifies their profile information.
3. The user confirms to finish editing their profile.
4. The system updates and saves all the information edited by the user.

**Primary Postconditions:** 
- The user’s profile information is updated and saved.

**Alternate Sequence:** The user does not modify anything.
- System does not save or update the profile information.
 
**8. Use case name:  Delete account**

**Pre condition:**
- The user has a registered account. 
- The user is on the user profile page.

**Trigger:** The user select the “Delete account” option under the user profile page.

**Primary Sequence:**
1. The system prompts the user to enter password of their account before deleting.
2. The user will input their password to verify their account ownership.
3. The system verifies the user account ownership.
4. The user will see a confirmation popup to confirm if they want to permanently delete the account.
5. The user clicks confirm to delete the account. 
6. The system displays a message indicating the account is permanently deleted.

**Primary Postconditions:**
- The user will be taken back to the Login page. 
- The system removes the user’s account from database.  

**Alternate Sequence #1:** The user enters a wrong password during the verification message.
- The system displays a error message to indicate unsuccessful request to delete account and prompts the user to reenter or cancel the process. 
- The user either reenter the password or choose to cancel the process. 

**Alternate Sequence #2:** The user clicks “No” to cancel the confirmation to delete the account.
- The user is redirected to their profile page.
