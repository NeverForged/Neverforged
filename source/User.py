from Dice import Roll
from Rules import Rules
from Database import Database
from Character_Creation import CharacterCreation

class User(object):
    '''
    Handler for a User object
    '''

    def __init__(self, user, pword):
        '''
        '''
        self.db = Database('NeverforgedData')
        query = 'SELECT pword FROM users WHERE email LIKE \'{}\''.format(user)
        pwact = self.db.query(query)
        if len(pwact) >= 1:
            if pword == pwact[0][0]:
                self.user = user
                self.char = None
                self.npcs = {}
            else:
             raise Exception
        else:
            query = ('INSERT into users (email, pword) ' +
                          'VALUES (\'{}\', \'{}\')'.format(user, pword))
            self.db.query(query)
        self.user = user
        self.char = None
        self.npcs = {}
        self.roll = Roll('3d6', trait='None')
        self.roll.web_show()
        self.rules = Rules()

    def new_character(self):
        self.new_char = CharacterCreation(self.user)
        return self.new_char

    def __repr__(self):
        return self.user
