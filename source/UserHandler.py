from User import User
from Database import Database

class UserHandler(object):
    '''
    Stores user objects in a dictionary by ip.
    '''
    def __init__(self):
        self.db = Database('NeverforgedData')
        self.user_d = {}

    def add(self, email, pword, ip):
            user = User(email, pword)
            self.user_d[ip] = user
            print(self.user_d.keys())
