from .settings import manager
from .models import User

def login():
    username = input("Username: ")
    password = input("Password: ")

    for user in manager.read_all(User):
        if user.username.lower() == username.lower():
            if user.check_password(password):
                print(f'Welcome {user.firstname}')
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
    print(f"Welcome {user.firstname}!")
    User.CURRENT_USER = user

def logout():
    pass

def create_new_message():
    pass

def inbox():
    print('Current user:',User.CURRENT_USER)

def sent():
    pass

def draft():
    pass