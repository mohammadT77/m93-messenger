from .settings import manager
from .models import User, Message

def login():
    username = input("Username: ")
    password = input("Password: ")

    for user in manager.read_all(User):
        if user.username.lower() == username.lower():
            if user.check_password(password):
                print(f'Welcome {user.first_name}')
                User.CURRENT_USER = user
                return
    print("Username or Password is invalid")


def register():
    username = input("Username: ")
    firstname = input("Firstname: ")
    lastname = input("Lastname: ")
    password = input("Password: ")

    user = User(username, firstname, lastname, password)
    manager.create(user)
    print(f"Welcome {user.first_name}!")
    User.CURRENT_USER = user

def logout():
    User.CURRENT_USER = None
    print('Bye Bye!')

def create_new_message():
    if not User.CURRENT_USER:
        print("Login first!")
        return

    receiver_username = input("To: @")
    subject = input('Subject: ')
    content = input('Content: ')
    send_confirm = input("Do you want to send? (yes/NO)")
    
    sender = User.CURRENT_USER
    receiver = User.get_user_by_username(receiver_username)
    if not receiver:
        print("the receiver is not found")
        return
    
    status = 'SENT' if send_confirm.lower() in ('yes', 'y') else 'DRAFT'
    msg = Message(subject, content, sender._id, receiver._id, status)
    manager.create(msg)
    
    print("\nThe message status:", status)
        

def inbox():
    if not User.CURRENT_USER:
        print("Login first!")
        return
    
    

def sent():
    pass

def draft():
    pass