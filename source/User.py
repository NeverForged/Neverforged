from Database import Database


class User(object):
    '''
    Handler for a User object
    '''

    def __init__(self, user, pword):
        '''
        '''
        self.db = Database('NeverforgedData')
        query = 'SELECT pword FROM users WHERE user = /'{}/''.format(user)
        pwact = self.dq.query(query)[0][0]
        if pword == pwact:
            self.user = user
            self.char = None
            self.npcs = {}
        else:
             raise Exception('Incorrect Password')
