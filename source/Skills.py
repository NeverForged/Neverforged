from Dice import Roll
from Database import Database
import matplotlib.pyplot as plt

class Skills(object):
    '''
    Handler class for the skills of a PC/NPC.
    '''

    def __init__(self, _id, char_type='PC', db=None, char=None):
        '''
        Initializer for creature skill list.
        '''
        self.db = db
        self.type = char_type
        self.id = _id
        self.skills = []
        query = ('SELECT skills.name, skills._id, t1.level ' +
                 'FROM skills ' +
                 'JOIN (SELECT skill, level FROM ' + self.type + '_skills ' +
                 '      WHERE character = ' + str(self.id) + ') AS t1 ' +
                 'ON skills._id = t1.skill')
        lst = self.db.query(query)
        lst.sort()
        self.skills = {}
        for item in lst:
            self.skills[item[1]] = (item[0], item[2])
        self.character = char

    def __repr__(self):
        '''
        Prints a list of skills that the character has and the rank in them
        '''
        length = len(self.skills)
        ret = ''
        lst = list(self.skills.keys())
        lst.sort()
        for i, skill in enumerate(lst):
            level = (str(self.skills[skill][1]).replace('1', 'trained')
                                               .replace('2', 'apprentice')
                                               .replace('3', 'journeyman')
                                               .replace('4', 'master'))
            ret = ret + '{} [{}]'.format(self.skills[skill][0], level)
            if i < length - 1:
                ret = ret + '\n'
        return ret

    def info(self, skl):
        '''
        Prints information on the skill.
        '''
        s_id = -1
        if type(skl) == int:
            s_id = skl
        else:
            s_id = self.db.query('SELECT _id FROM skills ' +
                                 'WHERE name LIKE \'%' +
                                 skl + '%\'')[0][0]
        s_id = int(s_id)  # Make sure it's an ID
        ret = ('{} [{}]'.format(self.skills[s_id][0],
                                self.skills[s_id][1])
                                .replace('1', 'trained')
                                .replace('2', 'apprentice')
                                .replace('3', 'journeyman')
                                .replace('4', 'master').title())
        ranks = ['untrained', 'trained', 'apprentice',
                 'journeyman', 'master']
        query = 'SELECT tags, description'
        for i in range(self.skills[s_id][1] + 1):
            query = query + ', ' + ranks[i]
        query = query + ' FROM skills WHERE _id = ' + str(s_id)
        for i, item in enumerate(self.db.query(query)[0]):
            ret = ret + ' \n'
            if i == 0:
                ret = ret + '(' + item + ")"
            elif i == 1:
                ret = ret + 'Description: \n' + item
            else:
                ret = ret + '\n' + ranks[i-2].title() + '\n' + item
        return ret

    def roll(self, skl):
        s_id = -1
        if type(skl) == int:
            s_id = skl
        else:
            s_id = self.db.query('SELECT _id FROM skills ' +
                                 'WHERE name LIKE \'%' +
                                 skl + '%\'')[0][0]
        s_id = int(s_id)  # Make sure it's an ID
        traits = self.db.query('SELECT roll FROM skills ' +
                               'WHERE _id = {}'.format(s_id))[0][0]
        traits = traits.split('/')
        val = 20
        usetrait = 'S'
        dice = '3d4'
        for trait in list(traits):
            idx = self.character.trait_guide.index(trait)
            if val > self.character.trait_values[idx]:
                val = self.character.trait_values[idx]
                usetrait = trait
                dice = self.character.trait_dice[idx]
        title = '{} [{}]({}) Roll:'.format(self.skills[s_id][0],
                                           str(self.skills[s_id][1])
                                           .replace('1', 'trained')
                                           .replace('2', 'apprentice')
                                           .replace('3', 'journeyman')
                                           .replace('4', 'master'),
                                           usetrait)
        roll = Roll(dice)
        roll.show(title)
        plt.show()
