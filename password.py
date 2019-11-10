from locker import User
from locker import Credentials


def create_new_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def login_user(username, password):
    """
    Function that checks whether a user exists and logs the user in
    """
    check_user = Credentials.verify_user(username, password)
    return check_user
 
 