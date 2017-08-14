import codecs
import sqlite3
import string
# -*- coding: utf-8 -*-

class Database(object):
    '''
    Opens a database connection to allow for  manipulation of data.

    PARAMETERS
    filename: name of the file, ends in "*.sql"

    ATTRIBUTES
    connection: connection to the database

    METHODS
    query(query): Input some SQL code in query, get the results in a return
    '''

    def __init__(self, file_name):
        '''
        initializer, opens the database connection.
        '''
        self.name = file_name

    def query(self, query):
        '''
        Input some SQL code in query, get the results in a return
        '''
        # print(query)
        connection = sqlite3.connect('../sql/' + self.name)
        cursor = connection.cursor()
        cursor.execute(query)
        if ('INSERT' in query or 'REPLACE' in query or 'UPDATE' in query or
           'DELETE' in query):
            return connection.commit()
        else:
            return cursor.fetchall()

    def add_item(self, item, char, qt, loc=0, ct='PC'):
        '''
        Handler for adding things to inventory, since it gets complicated
        item and char are '_id' values.  qt is number being added, loc is where
        ct is PC for PC, NPC for NPC.

        this combines all items at that location, then reapplies for stack
        size...
        '''
        stack = self.query('SELECT stack FROM equipment WHERE _id={}'
                           .format(item))[0][0]
        if stack > 1:
            try:
                sqt = self.db('SELECT _id, qt FROM PC_inventory WHERE ' +
                             'item={} AND character={} AND loc={}'
                             .format(item, char, loc))[0][0]
                nqt = sum([q[1] for q in qt])
                nums = [q[0] for q in qt]
            except:
                nqt = 0
                tqt = qt + nqt
                nums = []
            i = 0
            while tqt >= stack:
                if len(nums) >= i + 1:
                    _id = nums[i]
                    self.query('UPDATE PC_inventory ' +
                               'SET qt={}'.format(tqt) +
                               'WHERE _id={}'.format(_id)
                               .format(_id, char, item, loc, tqt))
                else:
                    _id = int(self.query('SELECT _id FROM PC_inventory ' +
                                         'GROUP BY _id  ORDER BY _id '
                                         'DESC LIMIT 1')[0][0]) + 1
                    self.query('INSERT INTO PC_inventory (_id, character, ' +
                               'item, loc, worn, qt)' +
                               'VALUES ({}, {}, {}, {}, 0, {})'
                               .format(_id, char, item, loc, stack))
                i += 1
                tqt = tqt - stack
            if tqt > 0:
                if len(nums) >= i + 1:
                    _id = nums[i]
                    self.query('UPDATE PC_inventory ' +
                               'SET qt={}'.format(tqt) +
                               'WHERE _id={}'.format(_id)
                               .format(_id, char, item, loc, tqt))

                else:
                    _id = int(self.query('SELECT _id FROM PC_inventory ' +
                                         'GROUP BY _id  ORDER BY _id '
                                         'DESC LIMIT 1')[0][0]) + 1
                    self.query('INSERT INTO PC_inventory (_id, character, item, ' +
                               'loc, worn, qt)' +
                               'VALUES ({}, {}, {}, {}, 0, {})'
                               .format(_id, char, item, loc, tqt))
        else:
            while qt > 0:
                _id = int(self.query('SELECT _id FROM PC_inventory ' +
                                     'GROUP BY _id  ORDER BY _id '
                                     'DESC LIMIT 1')[0][0]) + 1
                self.query('INSERT INTO PC_inventory (_id, character, item, ' +
                           'loc, worn, qt)' +
                           'VALUES ({}, {}, {}, {}, 0, {})'
                           .format(_id, char, item, loc, 1))
                qt = qt - 1

if __name__ == '__main__':
    db = Database('neverforgedData')
    ret = db.query('''
                 SELECT * FROM hitlocation
                 ''')
    b = [a for a in ret]
    for c in b[:2]:
        print('{}'.format(c))
