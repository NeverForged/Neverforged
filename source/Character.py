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
        if self.id is None:
            self.create_new()
        else:
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

    def create_new(self):
        '''
        Character creater script.
        '''
        campaign = 0
        pick = 'n'
        while pick != 'y':
            print('\n'*30)
            cams = self.db.query('SELECT _id, Campaign FROM campaign')
            print('Choose a campaign...')
            for cam in cams:
                print('{:>3} - {}'.format(cam[0], cam[1]))
            try:
                campaign = int(input('\n' + 'Pick campaign by number: '))
                cinfo = self.db.query('SELECT Campaign, Description ' +
                                      'FROM campaign ' +
                                      'WHERE _id = {}'.format(campaign))[0]
                print('{} \n   {}'.format(cinfo[0], cinfo[1]))
                pick = input('\n' + 'Select {} as campaign?'.format(cinfo[0]))
            except:
                input(type(campaign))
        # Background questions...
        answers = []
        for i in range(1, 15):
            print('\n'*30)
            print(self.db.query('SELECT question FROM ccquestions ' +
                                'WHERE _id = ' + str(i))[0][0]
                                .replace('\u2019', "'"))
            print('   '),
            print(self.db.query('SELECT explanation FROM ccquestions ' +
                                'WHERE _id = ' + str(i))[0][0]
                                .replace('\u2019', "'"))
            time.sleep(0.2)
            answers.append(input('').replace("'", "\'"))
        print('\n'*30)
        print(self.db.query('SELECT CCQuestion FROM campaign '
                            'WHERE _id = {}'.format(campaign))[0][0]
                            .replace('\u2019', "'"))
        print('   '),
        print(self.db.query('SELECT CCExplanation FROM campaign '
                            'WHERE _id = {}'.format(campaign))[0][0]
                            .replace('\u2019', "'"))
        answers.append(input('').replace("'", "\'"))

        # Background(s)
        lst = ['Nationality', 'Profession', 'Spark']
        bg_lst = []
        lst_a = []
        for item in lst:
            pick = 'n'
            while pick != 'y':
                print('\n'*30)
                print(item)
                try:
                    query = ('SELECT name FROM backgrounds ' +
                             'WHERE tags LIKE \'' + item + '\'')
                    if item == 'Profession':
                        query = (query + ' AND nation LIKE \'%s' +
                                 str(bg_lst[0]) +'e%\'')
                        print(query)
                    choice = input('Options: \n   ' +
                                   '\n   '.join([a[0] for a in
                                                 self.db.query(query)]) +
                                   '\nType One: ')
                    print('\n\n')
                    # Name
                    name = (self.db.query('SELECT name FROM backgrounds ' +
                                          'WHERE name LIKE \'%' + choice +
                                          '%\' AND ' + 'tags LIKE \'' +
                                          item + '\'')[0][0]
                                          .replace('\u2019', "'")
                                          .replace('\u201c', "'"))
                    print(name)
                    # Background Description
                    print(self.db.query('SELECT description FROM backgrounds' +
                                        ' WHERE name LIKE \'%' + choice +
                                        '%\' AND ' + 'tags LIKE \'' + item +
                                        '\'')[0][0].replace('\u2019', "'")
                                        .replace('\u201c', "'")
                                        .replace('\u201d', "'"))
                    # skills...
                    print()
                    print('   SKILLS:', end=' '),
                    for sk in range(1, 8):
                        squery = ('SELECT skills.name ' +
                                  'FROM skills ' +
                                  'JOIN (SELECT backgrounds.skill_{0} ' +
                                  '     FROM backgrounds ' +
                                  '     WHERE name LIKE  \'%{1}%\' AND ' +
                                  '     tags LIKE \'{2}\') t1 ' +
                                  'ON skills._id = t1.skill_{0}').format(sk,
                                                                         choice,
                                                                         item)
                        print(self.db.query(squery)[0][0], end=', ')
                    # ability
                    query = ('SELECT abilities FROM backgrounds ' +
                             'WHERE name LIKE \'%{0}%\''.format(choice) +
                             'AND tags LIKE \'' + item +'\'')
                    ab = self.db.query(query)[0][0]
                    ab = ab.replace('S', 'Strength').replace('D', 'Dexterity')
                    ab = ab.replace('F', 'Fortitude').replace('C', 'Charisma')
                    ab = ab.replace('I', 'Intelligence')
                    ab = ab.replace('W', 'Willpower')
                    print('\n   ABILITY: {}'.format(ab))
                    print('\n\n')
                    pick = input('Pick {} as your {}? '.format(name, item))[0]
                    pick = pick.lower()
                    if pick == 'y':
                        bg_lst.append(self.db.query('SELECT _id FROM ' +
                                                    'backgrounds ' +
                                                    'WHERE name LIKE \'%' +
                                                    choice + '%\'' +
                                                    'AND tags LIKE \'' +
                                                    item +'\'')[0][0])
                        # add ability score mod...
                        query = ('SELECT abilities FROM backgrounds ' +
                                 'WHERE name LIKE \'%{0}%\''.format(choice) +
                                 'AND tags LIKE \'' + item +'\'')
                        lst_a.append(self.db.query(query)[0][0])
                except:
                    input('              - Error, press ANY key to continue -')

        # Traits...
        points = 15
        lst_abs = [8, 8, 8, 8, 8, 8]
        lst_absa = [0, 0, 0, 0, 0, 0]
        lst_i = ['S', 'D', 'F', 'C', 'I', 'W']
        for item in lst_a:
            lst_absa[lst_i.index(item)] = lst_absa[lst_i.index(item)] + 1
        while points >= 1:
            print('\n'*30)
            print('-----------------Traits------------------')
            a, b = (lst_abs[0] + lst_absa[0], lst_abs[3] + lst_absa[3])
            print('  (S)trength: {:2}   |       (C)harisma: {:2}'.format(a, b))
            a, b = (lst_abs[1] + lst_absa[1], lst_abs[4] + lst_absa[4])
            print(' (D)exterity: {:2}   |   (I)ntelligence: {:2}'.format(a, b))
            a, b = (lst_abs[2] + lst_absa[2], lst_abs[5] + lst_absa[5])
            print(' (F)ortitude: {:2}   |      (W)illpower: {:2}'.format(a, b))
            print('\nYou have {} points remaining.'.format(points))
            ans = input('Type first letter to increase: ')
            ans = ans.upper()
            try:
                if lst_abs[lst_i.index(ans)] <= 12:
                    lst_abs[lst_i.index(ans)] = 1 + lst_abs[lst_i.index(ans)]
                    points -= 1
                else:
                    print('\nInvalid Entry: {}'.format(ans))
            except:
                print('\nInvalid Entry: {}'.format(ans))

        print('\n'*30)
        name_in = input('Simple form of {}\'s name: '.format(answers[-2]))
        # Okay, save the stuff...

        # make a Wound...
        wound = Wound()

        # Character...
        cols = ['_id']
        [cols.append('q{}'.format(a)) for a in range(1, 16)]
        cols.append('s')
        cols.append('d')
        cols.append('f')
        cols.append('c')
        cols.append('i')
        cols.append('w')
        cols.append('bg_n')
        cols.append('bg_p')
        cols.append('bg_s')
        cols.append('wounds')
        cols.append('stun')
        cols.append('injuries')
        cols.append('campaign')
        self.id = len(self.db.query('SELECT * FROM '  + self.type))
        vals = [self.id]
        [vals.append(ans) for ans in answers]
        for i in range(6):
            vals.append(lst_abs[i] + lst_absa[i])
        for item in bg_lst:
            vals.append(item)
        vals.append(''.join(str(a) for a in wound.wounds))
        vals.append(''.join(str(a) for a in wound.stun))
        vals.append('|||||')
        vals.append(campaign)
        query = ('INSERT into ' + self.type + ' ' +
                 '(name, {})'.format(', '.join(cols)) + ' ' +
                 'VALUES ' +
                 '(\'{}\', \'{}\');'.format(name_in, '\', \''.join(str(a)
                                                                   for a in
                                                                   vals)))
        self.db.query(query)

        # save skills
        lst_skills = []
        lst_langs = []
        for item in bg_lst:
            squery = ('SELECT skill_1, skill_2, skill_3, skill_4, skill_5, ' +
                      'skill_6, skill_7, skill_8, lang_p, lang_e ' +
                      'FROM backgrounds ' +
                      'WHERE _id LIKE {}'.format(str(item)))
            for i, skl in enumerate(list(self.db.query(squery)[0])):
                if type(skl) == int:
                    if i <= 8:
                        lst_skills.append(skl)
                    else:
                        lst_langs.append(skl)
        lst_lit = []
        for item in lst_langs:
            if item in lst_skills:
                lst_lit.append(item)
        lst_skills = lst_skills + lst_langs
        lst_skills.sort()
        # print(lst_skills)
        for skl in lst_skills:
            # _id for database
            sk_id = len(self.db.query('SELECT * FROM ' +
                             self.type + '_skills'))
            lvl = 1
            if skl in lst_lit:
                lvl = int((lst_abs[4] + lst_absa[4])/4)
            # check if already there...
            #try: # increase to 2 or lit level if already in there...
                # print('Start...')
            qry = ('SELECT _id ' +
                   'FROM ' + self.type + '_skills ' +
                   'WHERE character={}'.format(self.id) +
                   ' AND skill={}'.format(skl))
            skill = self.db.query(qry)
            if len(skill) > 0:
                if lvl == 1: # update... to apprentice
                    lvl = 2
                query = ('UPDATE {}_skills '.format(self.type) +
                         'SET level = {} '.format(lvl) +
                         'WHERE skill = {} AND character = {}'
                         .format(skl, self.id))
            else:
                query = ('INSERT into {}_skills'.format(self.type) +
                         '(_id, skill, character, level)' +
                         'VALUES ({}, {}, {}, {})'.format(sk_id, skl,
                                                          self.id, lvl))
            self.db.query(query)

        # Inventory...
        pc = self.type
        ch = self.id
        for bg in bg_lst:
            for i in range(1, 6):
                # get item...
                query = ('SELECT item_{}'.format(i) + ' '
                         'FROM backgrounds ' +
                         'WHERE _id = {}'.format(bg))
                itm = int(self.db.query(query)[0][0])
                qt = int(self.db.query('SELECT qt FROM equipment ' +
                                       'WHERE _id = {}'.format(itm))
                                       [0][0])
                if i == 5:  # get assigned qt...
                    qt = qt * int(self.db.query('SELECT qt '
                                                'FROM backgrounds ' +
                                                'WHERE _id={}'.format(bg))
                                                [0][0])
                exist = self.db.query('SELECT qt ' +
                                      'FROM {}_inventory '.format(pc) +
                                      'WHERE character = {} '.format(ch) +
                                      'AND item = {}'.format(itm))
                stack = int(self.db.query('SELECT stack '
                                          'FROM equipment ' +
                                          'WHERE _id = {}'.format(itm))
                                          [0][0])
                print(exist)
                if len(exist) >=  1 and int(exist[0][0]) >= 1:
                    print("...got 1")
                    amnt  = int(exist[0][0]) + qt
                    print(amnt)
                    for i in range(int(amnt/stack)):  # add stacks
                        query = ('INSERT into {}_inventory'.format(pc) +
                                 '(character, item, loc, worn, qt)' +
                                 'VALUES ({}, {}, 0, 0, {})'.format(ch,
                                                                    itm,
                                                                    stack))
                        if i > 0:
                            amnt = amnt - stack
                            print(amnt)
                            self.db.query(query)
                    # set the old value to the new...
                    self.db.query('UPDATE {}_inventory '.format(pc) +
                                  'SET qt = {} '.format(amnt) +
                                  'WHERE character = {} '.format(ch) +
                                  'AND item = {} '.format(itm) +
                                  'AND qt  = {}'.format(int(exist[0][0])))
                else:
                    amnt = qt
                    for i in range(int(amnt/stack)):  # add stacks
                        query = ('INSERT into {}_inventory'.format(pc) +
                                 '(character, item, loc, worn, qt)' +
                                 'VALUES ({}, {}, 0, 0, {})'.format(ch,
                                                                    itm,
                                                                    stack))
                        if i > 0:
                            amnt = amnt - stack
                            self.db.query(query)
                    self.db.query('INSERT into {}_inventory'.format(pc) +
                                  '(character, item, loc, worn, qt)' +
                                  'VALUES ({}, {}, 0, 0, {})'.format(ch,
                                                                     itm,
                                                                     amnt))

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
