import sys
import time
from Dice import Roll
from Wounds import Wound
from Skills import Skills
from Database import Database
import matplotlib.pyplot as plt
from Appearance import Appearance



class Character(object):
    '''
    This is a handler class for Character and Creature objects to store the
    various values associated with a character/creature.

    PARAMETERS
    name: Name of character
    char_type: PC for player object, NPC for non-player character object

    ATTRIBUTES
    name: Name
    type: PC or NPC
    db: database
    skills: Skills class describing skills of char.
    wounds: A Wound object
    id: character id
    type: PC or NPC

    METHODS
    create_new: makes a new chaacter from console.
    save: updates the database
    '''

    def __init__(self, char_type='PC', sql_id=None, db=None):
        '''
        Initializer for Character object.
        '''
        self.type = char_type
        self.id = sql_id
        self.db = db
        self.name = self.db.query('SELECT name FROM ' + self.type +
                                  ' WHERE _id = ' +str(self.id))[0][0]
        self.skills = Skills(self.id, self.type, self.db, self)
        self.trait_guide = ['S', 'D', 'F', 'C', 'I', 'W']
        self.trait_values = self.db.query('SELECT s, d, f, c, i, w ' +
                                          'FROM {}'.format(self.type) + ' ' +
                                          'WHERE _id = {}'.format(self.id))[0]
        self.trait_dice = []
        for val in self.trait_values:
            self.trait_dice.append(self.db.query('SELECT dice ' +
                                                 'FROM trait_dice ' +
                                                 'WHERE _id = {}'.format(val))
                                                 [0][0])
        # Wounds
        wnds = self.db.query('SELECT wounds, stun, injuries ' +
                             'FROM {}'.format(self.type) + ' ' +
                             'WHERE _id = {}'.format(self.id))[0]
        self.wounds = Wound(lst_wounds=list(wnds[0]),
                            lst_injuries=wnds[2].split('|'),
                            lst_stun=list(wnds[1]))
        # Backgrounds
        query = 'SELECT ' + ','.join(['q{}'.format(a) for a in range(1, 15)])
        query = query + ' FROM {} WHERE _id = {}'.format(self.type, self.id)
        self.background = list(self.db.query(query)[0])

    def save(self):
        '''
        Saves the character...
        '''
        # cols
        cols.append('s')
        cols.append('d')
        cols.append('f')
        cols.append('c')
        cols.append('i')
        cols.append('w')
        cols = cols + ['q{}'.format(a) for a in range(1, 16)]
        cols.append('wounds')
        cols.append('stun')
        cols.append('injuries')
        # vals
        vals = [str(a) for a in self.trait_values]
        vals = vals + [a for a in self.backgrounds]
        vals.append(''.join(str(a) for a in self.wounds))
        vals.append(''.join(str(a) for a in self.stun))
        vals.append('|'.join(str(a) for a in self.injuries))
        query = 'UPDATE {} '.format(self.type)
        query = query + 'SET {} = {}'.format(cols[0], vals[0])
        for i in range(1, len(cols) - 1):
            query = query + ', {} = {}'.format(cols[i], vals[i])
        query = query + ' WHERE _id = {}'.format(self.id)
        self.db.query(query)

if __name__ == '__main__':
    db = Database('NeverforgedData')
    if len(sys.argv) > 1:
        char = Character('PC', int(sys.argv[1]), db)
    else:
        char = Character('PC', None, db)
    fig, ax = plt.subplots(1, figsize=(6, 6))
    app = Appearance(char, char.db, ax)
    app.draw_char()
    app.show()
