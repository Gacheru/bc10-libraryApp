# **Andela Cohort 10 Project**
## **Library Application**
 This is a simple Web application that helps in the running and management of a library. 
 It allows a user to do the following tasks.
       
 -[x] Signup / login.   
 -[x] View all available books.
 -[ ] Borrow any available book.
 -[ ] Track the status of a book.
      * Borrowed.
      * Available.
 -[ ] Manage and keep inventory of books through;
      * Adding of new books.
      * Deleting of books.
 -[ ] Managing the borrowing of books through;
      * Issuing fines to members that haven't returned books past their due date.
      * Receiving of borrowed books.
    
## **Installation Instructions.**
 You will be required to install virtualenv.
 
       $ pip install virtualenv
 
 Then create you own virtual env within the project repository.
 
       $ virtualenv [name]
     
 Once created use the following command to get your virtual environment to run.
 
       $ path to dir\[virtual environment name]\Scripts\activate
 
 Do the same for killing the virtual environment.
 
       $ path to dir\[virtual environment name]\Scripts\deactivate
     
 Once running you should have the following view on the command line.
 
       $ (virtual environment name) path to dir\
     
 Once done install the desired application dependancies listed below.
     
## **The Following Are The  Application Dependancies**
 
 The following is a list of required libraries that need to be installed so as to run the application successfully.
  
    $ pip install [package name]
    
-[x] Flask==0.11.1
-[x] Flask-Bootstrap==3.3.7.0
-[x] Flask-Script==2.0.5
-[x] Flask-SQLAlchemy==2.1
-[x] Flask-WTF==0.13.1
-[x] imageio==1.6
-[x] itsdangerous==0.24
-[x] Jinja2==2.8
-[x] MarkupSafe==0.23
-[x] passlib==1.6.5
-[x] SQLAlchemy==1.1.1
-[x] Werkzeug==0.11.11
-[x] WTForms==2.1   
    

 Finally once done, key in the following command to launch the application.
  
    $ (virtual environment name) path to dir\python run.py
      
 Open the link displayed to view the application.
 
      http://127.0.0.1:7000/
 