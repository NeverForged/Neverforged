from Database import Database

class Rules(object):
    '''
    handler for Rules-Lookup
    '''

    def __init__(self):
        self.filter = ''
        self.db = Database('NeverforgedData')
        self.tables = ['rules', 'skills']
        self.table = 'rules'
        self.tags = ['-All-'] + self.get_taglist(self.table)
        self.tag = '-All-'
        self.rules_show = self.get_rules()


    def get_taglist(self, table):
        '''
        Given a table, it finds all possible tags and returns them in a sorted
        list...
        '''
        q = self.db.query('SELECT tags FROM {} '.format(table))
        tags = set()
        for item in q:
            temp = item[0].split(',')
            tags.update(t for t in temp)
        taglst = list(tags)
        taglst.sort()
        return taglst

    def get_rules(self):
        '''
        '''
        if self.tag == '-All-':
            query = self.db.query('SELECT * FROM {} '.format(self.table) +
                                  'WHERE name LIKE \'%{}%\' '
                                  .format(self.filter))
        else:
            query = self.db.query('SELECT * FROM {} '.format(self.table) +
                                  'WHERE name LIKE \'%{}%\' '
                                  .format(self.filter) +
                                  'AND tags LIKE \'%{}%\''
                                  .format(self.tag))
        self.rules = {}
        ret = '<table width=100%>'
        ind = "&nbsp;&nbsp;&nbsp;"
        if self.table == 'rules':
            for item in query:
                self.rules[item[1]] = [item[2], item[3]]
            rules = list(self.rules.keys())
            rules.sort()
            for i, rule in enumerate(rules):
                al = 'style:"width=100%; padding-right:100%;"'
                if i % 2 == 1:
                    al = ' style="width=100%; background-color:#eee;"'
                ret = ret + '<tr{}><td>'.format(al)
                ret = ret + ('<div class="dropdownsk">' +
                             '<button class="dropbtn"><center>{} [{}]</center>'
                             .format(rule, self.rules[rule][0]) +
                             '</button><div class="dropdownsk-content">')
                ret = ret + ind + ('<b>Tags:</b> {}<br>'
                                   .format(self.rules[rule][0]))
                ret = ret + ind + ('<i>{}</i>'.format(self.rules[rule][1]))
                ret = ret + '</div></div></td></tr>'
        elif self.table == 'skills':
            for item in query:
                # tags, roll, desc, unt, tr, app, jo, mst
                self.rules[item[1]] = [item[2], item[3], item[4], item[5],
                                       item[6], item[7], item[8], item[9]]
            rules = list(self.rules.keys())
            rules.sort()
            for i, rule in enumerate(rules):
                al = 'style:"width=100%; padding-right:100%;"'
                if i % 2 == 1:
                    al = ' style="width=100%; background-color:#eee;"'
                ret = ret + '<tr{}><td>'.format(al)
                ret = ret + ('<div class="dropdownsk">' +
                             '<button class="dropbtn"><center>{} [{}]</center>'
                             .format(rule, self.rules[rule][0]) +
                             '</button><div class="dropdownsk-content">')
                ret = ret + ind + ('<b>Tags:</b> {}'
                                   .format(self.rules[rule][0]))
                if len(self.rules[rule][1]) >= 1:
                    ret = ret + ' [{}]'.format(self.rules[rule][1])
                ret = ret + '<br>'
                ret = ret + ind + ('<i>{}</i><br>'.format(self.rules[rule][2]))
                lst = ['Untrained:', 'Trained:', 'Apprentice:',
                       'Journeyman:', 'Master:']
                for j in range(5):
                    if len(self.rules[rule][j + 3]) >= 1:
                        ret = ret + ind + ('<b>{}</b> {}<br>'
                                           .format(lst[j],
                                                   self.rules[rule][j + 3]))
                ret = ret + '</div></div></td></tr>'
        return ret

    def update(self):
        self.tags = ['-All-'] + self.get_taglist(self.table)
        self.rules_show = self.get_rules()
