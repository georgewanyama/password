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

