from Database import Database

class CharacterCreation(object):
    '''
    Holder for Char-Creation object
    '''
    def __init__(self, user):
        self.user = user
        self.campaign = 0
        self.bg_qs = ['','','','','','','','','','','','','','','','']
        self.bg_act = ['','','']
        self.trts = [8, 8, 8, 8 , 8, 8]
        self.trta = [0, 0, 0, 0, 0, 0]
        self.db = Database('NeverforgedData')
        print('CC initiated')

    def var(self, var, trt_adds, ans, filt, name):
        ind = '&nbsp;&nbsp;&nbsp;'
        ret = ''
        if var == '_new':
            self.campaign = -1
            return '_red/create_cam:0'
        elif var[:5] == '_cam:':
            ret = ret + ('<center>' +
                         '<span style="font-family: Papyrus, fantasy; ' +
                         'font-size: 30px; font-variant: small-caps;"><b>')
            ret = ret + 'campaign' + '</b></span>'
            ret =  ret + '<br><br><div class="dropdown">'
            ret = ret + '<button class="dropbtn">Choose a campaign</button>'
            ret = ret + '<div class="dropdown-content">'
            cams = self.db.query('SELECT _id, campaign ' +
                                 'FROM campaign')
            for cam in cams:
                ret = ret + ('<a href="create_cam:{}">{}</a>'
                             .format(cam[0], cam[1]))
            ret = ret + '</div></div><br><br>'
            ret =  ret + ('<span style="font-family: Georgia, Times,'+
                          ' "Times New Roman", serif;">')
            query = ('SELECT campaign, Location, Description ' +
                    'FROM campaign WHERE _id={}'.format(var[5:]))
            info = self.db.query(query)
            ret = ret + ('<br><b>{}</b> (<i>{}</i>)'
                         .format(info[0][0], info[0][1]))
            ret = ret + ('<br><br></center><i>{}</i><br><br><br>'
                         .format(info[0][2]))
            ret = ret +  ('<center><b><a href="/create_cam_conf{}">'
                           .format(var[5:]) +
                          '<b>**Click to choose {}**</b></a></center>'
                          .format(info[0][0]))
        elif var[:9] == '_cam_conf':
            self.campaign = int(var[9:])
            return '_red/create_resetbg'
        elif var == '_resetbg':
            self.bg_qs = ['','','','','','','','','','','','','','','','']
            return '_red/create_question1'
        elif var[:9] == '_question':
            ret = ret + ('<center>' +
                         '<span style="font-family: Papyrus, fantasy; ' +
                         'font-size: 30px; font-variant: small-caps;">' +
                         '<b>Background Questions</b></span>')
            questions = self.db.query('SELECT question FROM ccquestions')
            questions.append(self.db.query('SELECT CCQuestion ' +
                                           'FROM campaign ' +
                                           'WHERE _id={}'
                                           .format(self.campaign))[0])
            ret = ret + '<br><br><div class="dropdown">'
            ret = ret + '<button class="dropbtn">Select a Question</button>'
            ret = ret + '<div class="dropdown-content">'
            for i, q in enumerate(questions):
                ret = ret + ('<a href="create_question{}">{}</a>'
                             .format(i+1, q[0]))
            ret = ret + '</div></div><br><br></center>'
            # question text and input
            ret =  ret + ('<span style="font-family: Georgia, Times,'+
                          ' "Times New Roman", serif;">')
            if int(var[9:]) <= 14:
                quest = self.db.query('SELECT question, explanation ' +
                                      'FROM ccquestions ' +
                                      'WHERE _id={}'.format(var[9:]))[0]
            else:
                quest = self.db.query('SELECT CCQuestion, CCExplanation '+
                                      ' FROM campaign' +
                                      ' WHERE _id={}'.format(self.campaign))[0]
            ret = ret + ('<b>{}</b><br><i>{}</i><br><br>'
                         .format(quest[0], quest[1]))
            # add a textbox and answer space...
            ret = ret + ('<center><form action="/create_ans{}">'
                         .format(var[9:]) +
                         '<p><textarea name="answer" rows="10" cols="90">' +
                         '{}</textarea></p>'.format(self.bg_qs[int(var[9:])]) +
                         '<br><input type="submit" ' +
                         'value="Save Answer"><center>')
            ret = ret + ('<br><br><br><center><a href="/create_backgrounds">' +
                         '<b>**Click to move on to Backgrounds**</b>' +
                         '</a><br><br><br>' +
                         '<center><a href="/create_cam:{}">'
                         .format(self.campaign) +
                         '<b>**Return to Campaign**</b></a>')
        if var[:4] == '_ans':
            self.bg_qs[int(var[4:])] = ans
            if int(var[4:]) <= 14:
                return '_redcreate_question{}'.format(int(var[4:]) + 1)
            else:
                return '_red/create_backgrounds'
        if var[:12] == '_backgrounds':
            ret = ret + ('<center>' +
                         '<span style="font-family: Papyrus, fantasy; ' +
                         'font-size: 30px; font-variant: small-caps;">' +
                         '<b>Backgrounds</b></span>')
            ret = ret + '<form action="/create_backgrounds">'
            ret = ret + ('<p>Search: <input type="text" name="filter" ' +
                         'value="{}">'.format(filt).replace('None', '') +
                        '</p><input type="submit" value="Apply"><center>')
            # center tag here down...
            print('Filter = {}'.format(filt))
            if filt == None:
                filt=''
                print('Filter = {}'.format(filt))
            try:  # Nationality
                nat = self.db.query('SELECT name FROM backgrounds ' +
                               'WHERE _id={}'.format(self.bg_act[0]))[0][0]
                ret = ret + ('<br><br><a href="create_bg_0_-1">' +
                             '** Change Nationality: {} **</a>'.format(nat))
            except:
                ret = ret + '<br><br><div class="dropdown">'
                ret = ret + ('<button class="dropbtn">' +
                             'Select a Nationality</button>')
                ret = ret + '<div class="dropdown-content">'
                nats = self.db.query('SELECT _id, name FROM backgrounds ' +
                                'WHERE tags LIKE \'Nationality\' AND ' +
                                '(name LIKE \'%{}%\' OR '.format(filt) +
                                'description LIKE \'{}\')'.format(filt))
                for nat in nats:
                    ret = ret + ('<a href="\create_bg_0_{}">'.format(nat[0]) +
                                 '{}</a>'.format(nat[1]))
                ret = ret + '</div></div>'
            try:  # Progfession
                nat = self.db.query('SELECT name FROM backgrounds ' +
                               'WHERE _id={}'.format(self.bg_act[1]))[0][0]
                ret = ret + ('<br><br><a href="create_bg_1_-1">' +
                             '** Change Profession: {} **</a>'.format(nat))
            except:
                ret = ret + '<br><br><div class="dropdown">'
                ret = ret + ('<button class="dropbtn">' +
                             'Select a Profession</button>')
                ret = ret + '<div class="dropdown-content">'
                nats = self.db.query('SELECT _id, name FROM backgrounds ' +
                                'WHERE (tags LIKE \'Profession\') AND ' +
                                '(name LIKE \'%{}%\' OR '.format(filt) +
                                'description LIKE \'{}\') '.format(filt) +
                                'AND (nation LIKE \'s-1e\' OR ' +
                                'nation LIKE \'%s{}e%\')'
                                .format(self.bg_act[0]))
                for nat in nats:
                    ret = ret + ('<a href="\create_bg_1_{}">'.format(nat[0]) +
                                 '{}</a>'.format(nat[1]))
                ret = ret + '</div></div>'
            try:
                sprk = self.db.query('SELECT name FROM backgrounds ' +
                                'WHERE _id={}'.format(self.bg_act[2]))[0][0]
                ret = ret + ('<br><br><a href="create_bg_2_-1">' +
                             '** Change Divine Spark: {} **</a>'.format(sprk))
            except:
                ret = ret + '<br><br><div class="dropdown">'
                ret = ret + ('<button class="dropbtn">' +
                             'Select a Divine Spark</button>')
                ret = ret + '<div class="dropdown-content">'
                nats = self.db.query('SELECT _id, name FROM backgrounds ' +
                                'WHERE (tags LIKE \'Spark\') AND ' +
                                '(name LIKE \'%{}%\' OR '.format(filt) +
                                'description LIKE \'{}\') '.format(filt) +
                                'AND (nation LIKE \'s-1e\' OR ' +
                                'nation LIKE \'%s{}e%\')'
                                .format(self.bg_act[0]))
                for nat in nats:
                    ret = ret + ('<a href="\create_bg_2_{}">'.format(nat[0]) +
                                 '{}</a>'.format(nat[1]))
                ret = ret + '</div></div>'
            ret = ret + self.print_bgs()
            # okay, now for the links...
            if (len(str(self.bg_act[0])) >= 1 and
                len(str(self.bg_act[1])) >= 1 and
                len(str(self.bg_act[2])) >= 1):
                ret = ret + ('<br><br><br><b><center>' +
                             '<a href="/create_abs">{}</a>'
                             .format('** Assign Character Traits **') +
                                     '</center>')
            ret = ret + ('<br><br><br><b><center>' +
                         '<a href="/create_question1">{}</a>'
                         .format('** Return to Questions **') + '</center>')
        if var[:4] == '_bg_':  # _bg_#_##
            if int(var[6:]) < 0:
                self.bg_act[int(var[4])] = ''
                return '_red/create_backgrounds'
            else:
                self.bg_act[int(var[4])] = int(var[6:])
                return '_red/create_backgrounds{}'.format(int(var[6:]))
        if var[:4] == '_abs':
            self.trta = trt_adds
            # add bg abilities...
            base = 8*6
            print(sum(self.trts))
            if sum(self.trts) - base == 0:
                # need to add bg abilitiy boosts...
                for bg in self.bg_act:
                    bg_ab = self.db.query('SELECT abilities ' +
                                          'FROM backgrounds ' +
                                          'WHERE _id={}'.format(bg))[0][0]
                    print(bg_ab)
                    self.trts = self.add_to_trait(bg_ab, self.trts)
            print(sum(self.trts))
            # add points...
            lst = ['S', 'D', 'F', 'C', 'I', 'W']
            for ab in lst:
                try:
                    for i in range(int(trt_adds)):
                        self.trta = self.add_to_trait(ab, self.trta)
                except:
                    pass
            # check points remaining
            for i, t in enumerate(self.trta):
                if t >= 6:
                    self.trta[i] = 5
                if t <= -1:
                    self.trta[i] = 0
            points = 15 - sum(self.trta)
            ret = ret + ('<center>' +
                         '<span style="font-family: Papyrus, fantasy; ' +
                         'font-size: 30px; font-variant: small-caps;">' +
                         '<b>Assign Traits</b></span>')
            ret = ret + '<br><br><b>Points Remaining: {}</b>'.format(points)
            ret = ret + '<br><i>Assign Points below.</i>'
            spc = ind + ' | ' + ind
            ret = ret + '<br><br><form action="/create_abs"><b><i>'
            ret = ret + ('<p>Strength {} '
                         .format(self.trts[0] + self.trta[0]) +
                         '<input type="text" name="S" value="{}" size="1">'
                         .format(self.trta[0]))
            ret = ret + spc
            ret = ret + ('Charisma {} '.format(self.trts[3] + self.trta[3]) +
                         '<input type="text" name="C" value="{}" size="1">'
                         .format(self.trta[3]) + '</p>')
            ret = ret + '<br>'
            ret = ret + ('<p>Dexterity {} '
                         .format(self.trts[1] + self.trta[1]) +
                         '<input type="text" name="D" value="{}" size="1">'
                         .format(self.trta[1]))
            ret = ret + spc
            ret = ret + ('Intelligence {} '
                         .format(self.trts[4] + self.trta[4]) +
                         '<input type="text" name="I" value="{}" size="1">'
                         .format(self.trta[4]) + '</p>')
            ret = ret + '<br>'
            ret = ret + ('<p>Fortitude {} '
                         .format(self.trts[2] + self.trta[2]) +
                         '<input type="text" name="F" value="{}" size="1">'
                         .format(self.trta[2]))
            ret = ret + spc
            ret = ret + ('Willpower {} '
                         .format(self.trts[5] + self.trta[5]) +
                         '<input type="text" name="W" value="{}" size="1">'
                         .format(self.trta[5]) + '</p>')
            ret = ret + '<br><br>'
            ret = ret + '<input type="submit" value="Submit">'
            if points < 0:
                ret = ret + '<br><br><b><i><span style="color: red">'
                ret = ret + 'Character Invalid; You may only spend 15 points!'
                ret = ret + '</span></i></b>'
            ret = ret + ('<br><br><br><b><center>' +
                         '<a href="/create_backgrounds">{}</a>'
                         .format('** Return to Backgrounds **') + '</center>')
            if points == 0:
                ret = ret + ('<br><br><br><b><center>' +
                             '<a href="/create_fin">{}</a>'
                             .format('** Create Character **') + '</center>')
        if var == '_fin':
            ret = ret + ('<center>' +
                         '<span style="font-family: Papyrus, fantasy; ' +
                         'font-size: 30px; font-variant: small-caps;">' +
                         '<b>Finalize Character</b></span>')
            ret = ret + ('<br><i>Edit character name below, this is how ' +
                         ' it will be displayed</i>')
            ret = ret + '<br><br><form action="/create_final"><b><i>'
            ret = ret + ('<input type="text" name="name" value="{}" size="30">'
                        .format(self.bg_qs[14]))
            ret = ret + '<input type="submit" value="Finalize">'
            ret = ret + '<br><br>'
            ret = ret + '<b>TRAITS</b></b></br>'
            ret = ret + ('Strength {}'.format(self.trts[0] + self.trta[0]) +
                          ind +'|' + ind + 'Charisma {}<br>'
                         .format(self.trts[3] + self.trta[3]))
            ret = ret + ('Dexterity {}'.format(self.trts[1] + self.trta[1]) +
                          ind +'|' + ind + 'Intelligence {}<br>'
                         .format(self.trts[4] + self.trta[4]))
            ret = ret + ('Fortitude {}'.format(self.trts[2] + self.trta[2]) +
                          ind +'|' + ind + 'Willpower {}<br>'
                         .format(self.trts[5] + self.trta[5]))
            ret = ret + '</br></br></center>'
            ret = ret + self.print_bgs()
            ret = ret + ('<br><br><br><b><center>' +
                         '<a href="/create_question1">{}</a>'
                         .format('** Return to Questions **') + '</center>')
            ret = ret + ('<br><br><br><b><center>' +
                         '<a href="/create_backgrounds">{}</a>'
                         .format('** Return to Backgrounds **') + '</center>')
            ret = ret + ('<br><br><br><b><center>' +
                         '<a href="/create_abs">{}</a>'
                         .format('** Return to Character Traits **') +
                                 '</center>')
        if var == '_final':
            self.name = name
            # find the char id...
            char_id = int(self.db.query('SELECT _id FROM PC GROUP BY _id '
                                        'ORDER BY _id DESC')[0][0]) + 1
            # now to insert a character....
            # INSERT INTO table_name (column1, column2, column3, ...)
            # VALUES (value1, value2, value3, ...)
            cols = []
            vals = []
            cols.append('_id')
            vals.append(char_id)
            cols.append('name')
            vals.append('\'' + self.name + '\'')
            cols.append('user')
            vals.append('\'' + self.user + '\'')
            cols = cols + ['q{}'.format(a) for a in range(1, 16)]
            vals = vals + ['\'{}\''.format(a) for a in self.bg_qs[1:]]
            cols = cols + ['s', 'd', 'f', 'c', 'i', 'w']
            vals = vals + [self.trts[i] + self.trta[i] for i in range(6)]
            cols = cols + ['bg_n', 'bg_p', 'bg_s']
            vals = vals + self.bg_act
            cols.append('campaign')
            vals.append(self.campaign)
            print(vals)
            queryitems = []
            queryskill = []
            qt = []
            langs = []
            for bg in self.bg_act:
                langs.append(self.db.query('SELECT lang_p ' +
                                           'FROM backgrounds WHERE _id=' +
                                           '{}'.format(bg))[0][0])
                langs.append(self.db.query('SELECT lang_e ' +
                                           'FROM backgrounds WHERE _id=' +
                                           '{}'.format(bg))[0][0])
                for i in range(1, 6):  # items...
                    queryitems.append('SELECT item_{}'.format(i) +
                                      ' FROM backgrounds WHERE _id=' +
                                      '{}'.format(bg))
                    if i < 5:
                        qt.append(1)
                    else:
                        qt.append(self.db.query('SELECT qt FROM backgrounds ' +
                                                'WHERE _id={}'
                                                .format(bg))[0][0])
                for i in range(1, 9):
                    queryskill.append('SELECT skill_{}'.format(i) +
                                      ' FROM backgrounds WHERE _id=' +
                                      '{}'.format(bg))
            queryit = ' UNION ALL '.join(queryitems)
            querysk = ' UNION ALL '.join(queryskill)
            items = self.db.query(queryit)
            skills = self.db.query(querysk)
            # now do it...
            # Character
            query = ('INSERT into PC ({}) '
                    .format(', '.join(str(c) for c in cols)) +
                     'VALUES ({})'.format(', '.join(str(v) for v in vals)))
            print(query)
            self.db.query(query)
            # Languages first...
            _id = int(self.db.query('SELECT _id FROM PC_skills ' +
                                    'GROUP BY _id ORDER BY _id ' +
                                    'DESC LIMIT 1')[0][0])
            print(langs)
            for lang in langs:
                if len(str(lang)) >= 1:
                    _id += 1
                    self.db.query('INSERT INTO PC_skills (_id, character, '+
                                  'skill, level) ' +
                                  'VALUES ({}, {}, {}, 1)'
                                  .format(_id, char_id, lang))
            # now actual skills...
            sk1 = [skill[0] for skill in skills]
            sk2 = list(set(sk1))
            for sk in sk2:
                sk1.pop(sk1.index(sk))
            for i, sk in enumerate(sk2):
                _id = int(self.db.query('SELECT _id FROM PC_skills ' +
                                        'GROUP BY _id ORDER BY _id ' +
                                        'DESC LIMIT 1')[0][0]) + 1
                lev = 1
                if sk in langs: # mastery/literacy
                    lev = int((self.trts[4] + self.trta[4])/4)
                    self.db.query('UPDATE PC_skills ' +
                                  'SET level={} '.format(lev) +
                                  'WHERE character={} '.format(char_id) +
                                  'AND skill={}'.format(sk))
                else:
                    if sk in sk1: # x2 = apprentice level at start
                        lev = 2
                    self.db.query('INSERT INTO PC_skills (_id, character, '+
                                  'skill, level) ' +
                                  'VALUES ({}, {}, {}, 1)'
                                  .format(_id, char_id, sk, lev))
            # item time...
            for i, it in enumerate(items):
                stack = self.db.query('SELECT stack FROM equipment WHERE _id={}'
                                   .format(it[0]))[0][0]
                if qt[i] == 1:
                    self.db.add_item(it[0], char_id, qt[i]*stack, 0)
                else:
                    self.db.add_item(it[0], char_id, qt[i], 0)
            return '_red/'
        # return value.
        return ret

    def add_to_trait(self, trait, trts):
        if trait == 'S':
            trts[0] += 1
        elif trait == 'D':
            trts[1] += 1
        elif trait == 'F':
            trts[2] += 1
        elif trait == 'C':
            trts[3] += 1
        elif trait == 'I':
            trts[4] += 1
        elif trait == 'W':
            trts[5] += 1
        return trts

    def print_bgs(self):
        ind = '&nbsp;&nbsp;&nbsp;'
        ret = ''
        for bg in self.bg_act:
            if len(str(bg)) >= 1:
                ret = ret + "</center></center>"
                # Display Last Background pickd...
                dis = self.db.query('SELECT name, tags, description, ' +
                                'abilities, ' +
                                'lang_p, lang_e ' +
                                'FROM backgrounds ' +
                                'WHERE _id={}'.format(bg))[0]
                ret = ret + '<br><br><b>{}</b> [{}]'.format(dis[0], dis[1])
                ret = ret + '<br><i>{}</i><br>'.format(dis[2])
                abil = (str(dis[3]).replace('S','Strength')
                                   .replace('D', 'Dexterity')
                                   .replace('F', 'Fortitude')
                                   .replace('C', 'Charisma')
                                   .replace('I', 'Intelligence')
                                   .replace('W', 'Willpower'))
                ret = ret + ind + ('<b>Ability:</b> <i>{}</i><br>'
                                   .format(abil))
                querylst = []
                for i in range(1, 9):
                    querylst.append('SELECT skills.name FROM skills '+
                                    'JOIN (SELECT skill_{}'.format(i) +
                                    ' FROM backgrounds WHERE _id=' +
                                    '{}'.format(bg) +
                                    ') as t ON t.skill_{} = skills._id'
                                    .format(i))
                query = ' UNION '.join(querylst) + ' ORDER BY skills.name'
                skills = self.db.query(query)
                ret = ret + ind + ('<b>Skills:</b> <i>{}</i><br>'
                                    .format(', '.join([a[0] for a
                                                       in skills])))
                if len(str(dis[4])) + len(str(dis[5])) >= 1:  # languages
                    if (self.db.query('SELECT tags FROM backgrounds ' +
                                      'WHERE _id={}'.format(bg))[0][0]
                                       == 'Spark'):
                        ret = ret + ind + ('<b>Divine Spark:</b> <i>')
                    else:
                        ret = ret + ind + ('<b>Languages:</b> <i>')
                    lst = []
                    if len(str(dis[4])) >= 1:
                        lst.append(self.db.query('SELECT name ' +
                                                 'FROM skills ' +
                                                 'WHERE _id={}'
                                                 .format(dis[4]))[0][0])
                    if len(str(dis[5])) >= 1:
                        lst.append(self.db.query('SELECT name ' +
                                                 'FROM skills ' +
                                                 'WHERE _id={}'
                                                 .format(dis[5]))[0][0])
                    ret = ret + ', '.join(lst) + '</i></br>'
                    # enf languages
                querylst=[]
                for i in range(1, 6):  # items...
                    querylst.append('SELECT equipment.name ' +
                                    'FROM equipment '+
                                    'JOIN (SELECT item_{}'.format(i) +
                                    ' FROM backgrounds WHERE _id=' +
                                    '{}'.format(bg) +
                                    ') as t ON t.item_{} = equipment._id'
                                    .format(i))
                query = ' UNION ALL '.join(querylst)
                items = self.db.query(query)
                ret = ret + ind +  ('<b>Starting Gear:</b> <i>{}</i>'
                                    .format(', '.join([a[0] for a
                                                       in items])))
                ret = ret + ' (x {})'.format(self.db.query('SELECT qt ' +
                                                           'FROM ' +
                                                           'backgrounds ' +
                                                           'WHERE _id={}'
                                                           .format(bg))
                                                           [0][0])
        return ret
