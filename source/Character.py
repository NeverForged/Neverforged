# _*_ coding:utf-8 _*_

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
        self.set_dice()
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
        self.backgrounds = list(self.db.query(query)[0])
        tnames = ['Strength', 'Dexterity', 'Fortitude',
                  'Charisma', 'Intelligence', 'Willpower']
        self.trait_names = []
        for nm in tnames:
            self.trait_names.append('<span style="font-family: Papyrus, '+
                                    'fantasy; font-size: 14px; font-variant' +
                                    ':small-caps; text-align: left;">' +
                                    '<b>{}'.format(nm) +
                                    '</b></span>&nbsp;&nbsp;&nbsp;')

        self.trait_table_start = ('<tr><td width="50%"> ' +
                         '<table><colgroup> ' +
                         '<col style="width:20%; text-align: left;"/>' +
                         '<col style="width:10%; text-align: center; ' +
                         'font-weight: bold"/>' +
                         '<col style="width:18%; text-align: center; "/>' +
                         '<col style="width 2.25%;"/>' +
                         '<col style="width: 0.5%; background:black;"/>' +
                         '<col style="width:2.25%;"/>' +
                         '<col style="width:20%; text-align: left;"/>' +
                         '<col style="width:10%; text-align: center; ' +
                         'font-weight: bold"/>' +
                         '<col style="width:16%; text-align: center;"/>' +
                         '</colgroup><tr><th></th><th></th><th></th>' +
                         '<th></th><th></th><th></th><th></th></tr>')
        skill_nums = self.db.query('SELECT skill, level FROM PC_skills '
                                   'WHERE character={}'.format(self.id))
        self.skills = {}
        for sk in skill_nums:
            skill_info = self.db.query('SELECT * FROM skills WHERE _id={}'
                                        .format(sk[0]))[0]
            self.skills[skill_info[1]] = list(skill_info)
            self.skills[skill_info[1]].append(sk[1])
        self.training = ['-pick a skill to train-', '-pick a skill to train-',
                         ' -pick a skill to train-']
        self.training_val = ['[&nbsp;&nbsp;][&nbsp;&nbsp;][&nbsp;&nbsp;]',
                             '[&nbsp;&nbsp;][&nbsp;&nbsp;][&nbsp;&nbsp;]',
                             '[&nbsp;&nbsp;][&nbsp;&nbsp;][&nbsp;&nbsp;]']


    def save(self):
        '''
        Saves the character...
        '''
        cols = []
        vals = []
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
        vals = vals + ['\'{}\''.format(a) for a in self.backgrounds]
        if '|' in self.wounds.wounds:
            self.wounds.wounds = [0,0,0,0,0,0]
        if '|' in self.wounds.stun:
            self.wounds.stun = [0,0,0,0,0,0]
        vals.append(''.join(str(a) for a in self.wounds.wounds))
        vals.append(''.join(str(a) for a in self.wounds.stun))
        vals.append('\'' + '|'.join(str(a) for a in self.wounds.injuries) +
                    '\'')
        query = 'UPDATE {} '.format(self.type)
        query = query + 'SET {} = {}'.format(cols[0], vals[0])
        for i in range(1, len(cols) - 1):
            query = query + ', {} = {}'.format(cols[i], vals[i])
        query = query + ' WHERE _id = {}'.format(self.id)
        self.db.query(query)

    def set_dice(self):
        '''
        Sets the dice conventions...
        '''
        for trait in self.trait_values:
            try:
                self.trait_dice.append(self.trait_dice_dict[trait])
            except:
                # we need to make the dictionary
                self.trait_dice_dict = {8:'3d4', 9:'1d6+2d4', 10:'2d6+1d4',
                                        11:'3d6', 12:'1d8+2d6', 13:'2d8+1d6',
                                        14:'3d8', 15:'1d10+2d8', 16:'2d10+1d8',
                                        17:'3d10', 18:'1d12+2d10',
                                        19:'2d12+1d10', 20:'3d12'}
                self.trait_dice.append(self.trait_dice_dict[trait])


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
