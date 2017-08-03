from Database import Database


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
             raise Exception('Incorrect Password')
        else:
            query = ('INSERT into users (email, pword) ' +
                          'VALUES (\'{}\', \'{}\')'.format(user, pword))
            self.db.query(query)
            self.user = user
            self.char = None
            self.npcs = {}
