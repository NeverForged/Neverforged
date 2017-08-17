from collections import defaultdict


class Combat(object):
    '''
    '''

    def __init__(self, char):
        '''
        '''
        self.char = char

    def wounds(self):
        '''
        Display wound table...
        '''
        ret = "<table width=100%>"
        ret = ret + ('<colspace>'
                     '<col width=60%>' +
                     '<col width=8% style="text-align: center;">' +
                     '<col width=30% style="text-align: right;">')
        ret = ret + ('<tr><td colspan="3"><div style="font-family: Papyrus, '+
                     'fantasy; font-size: 14px; font-variant' +
                     ':small-caps; text-align: center; float: center;">' +
                     ' - Wounds -</div></td></tr>')
        wnds = ['Minor', 'Light', 'Moderate', 'Serious', 'Critical']
        fort = float(self.char.trait_values[2])
        thr = [int(fort/16.0), int(fort/8.0), int(fort/4.0), int(fort/2.0),
               int(fort)]
        thrm = ['F &divide; 16', 'F &divide; 8', 'F &divide; 4',
                'F &divide; 2', '&nbsp;&nbsp;&nbsp;&nbsp;F']
        spcs = ['', '', '', '', '']
        # spcs = ['&nbsp;'*15, '&nbsp;'*15, '&nbsp;'*14, '&nbsp;'*15, '&nbsp;'*15]
        inj = self.char.wounds.injuries
        for i, wnd in enumerate(wnds):
            j = 1 + i
            al = ''
            if i % 2 == 1:
                al = ' style="background-color:#eee;"'
            ret = ret + '<tr><td {}>'.format(al) + inj[-(j)]
            ret = ret + '</td><td {}>'.format(al)  # cal col
            ret = ret + ('- <b>{}</b> - <br><div style="font-size: 75%;">'
                         .format(thr[i]) +
                        '<i>{}'.format(thrm[i]))
            ret = ret + '</div></i></td><td {}>'.format(al)  # cal col
            ret = ret + ('<div class="dropdown" style="float: right;">' +
                         '<button class="dropbtn-wd">' +
                         '<b>{}</b>'.format(spcs[i]+wnd))
            # print(self.char.wounds.wounds, self.char.wounds.stun, j)
            if self.char.wounds.wounds[-j] == 1:
                ret = ret + ' [x]'
            elif self.char.wounds.stun[-j] == 1:
                ret = ret + ' [s]'
            else:
                ret = ret + ' [&nbsp;&nbsp;]'
            # close the dropdown box and add options...
            ret = ret + '</button><div class="dropdown-contentwd">'
            # the options... need for each location a wound/stun, also a heal
            loc = ['torso high right', 'torso high left',
                   'torso low right', 'right arm', 'right leg',
                   'torso center', 'head', 'left leg', 'left arm',
                   'torso low left']
            ret = ret + ('<a href="/heal_dmg_{}">[&nbsp;&nbsp;] (Healing)</a>'
                        .format(6 - i))
            for k in range(10):
                ret = ret + ('<a href="/apply_dmg_{}_{}_{}_{}">'
                             .format(thr[i], k,
                                     self.char.trait_values[2], 0) +
                             '{}: [x]</a>'
                             .format(k))
            ret = ret + ('<a href="/apply_dmg_{}_{}_{}_{}">'
                             .format(thr[i], 0,
                                     self.char.trait_values[2], 1) +
                             '[s] Stun </a>')
            ret = ret + '</div></div></td></tr>'
            # add location picture...
        ret = ret + ('<tr><td colspan="3"><div style="font-family: '+
                     'Papyrus, fantasy; font-size: 14px; font-variant' +
                     ':small-caps; text-align: center; float: center;">-Hit' +
                     ' Locations -</div></td></tr>')
        ret = ret + ('<tr><td colspan="3">' +
                     '<img src="/static/images/armor_loc.png" ' +
                     'alt="Hit Locations: Last digit of roll determines ' +
                     'location struck." ' +
                     'title="Hit Locations: Last digit of roll  ' +
                     'determines location struck." width=100%></td></tr>')
        ret = ret + '</table>'
        return ret

    def weapons(self):
        '''
        '''
        ind = '&nbsp;&nbsp;&nbsp;'
        ret = '<table width=100%>'  # open weapon/main tables
        # Weapons
        ret = ret + ('<tr><td colspan="2"><div style="font-family: '+
                     'Papyrus, fantasy; font-size: 14px; font-variant' +
                     ':small-caps; text-align: center; float: center;">' +
                     '- Weapons & Shields -</div></td></tr>')
        weapons = self.char.db.query('SELECT * FROM equipment ' +
                                      'WHERE tags LIKE \'%weapon%\' '
                                      'AND _id IN '
                                        '(SELECT item ' +
                                        'FROM PC_inventory ' +
                                        'WHERE character={} '
                                        .format(self.char.id) +
                                        'AND loc IN ' +
                                        '(SELECT slot ' +
                                            'FROM inventory_slots ' +
                                            'WHERE name LIKE \'-%\' OR ' +
                                            'name LIKE \'Back\' OR ' +
                                            'name LIKE \'%Shoulder\'))')
        qt = self.char.db.query('SELECT item, qt, loc ' +
                                '    FROM PC_inventory ' +
                                '    WHERE character={} '
                                .format(self.char.id) +
                                '    AND loc IN ' +
                                '       (SELECT slot ' +
                                '        FROM inventory_slots ' +
                                '        WHERE name LIKE \'-%\' OR ' +
                                '        name LIKE \'Back\' OR ' +
                                '        name LIKE \'%Shoulder\' )')
        # Attack skill...
        try:
            level = self.char.skills['Attack'][-1]
        except:
            level = 0
        try:
            blevel = self.char.skills['Bow'][-1]
        except:
            blevel = 0
        lst_dmg = ['L', 'M', 'H', 'LM', 'LH', 'MH', 'LMH']
        # weapon loop

        for i, weapon in enumerate(weapons):
            al = ''
            if i % 2 == 1:
                al = ' style="background-color:#eee;"'
            the_props = weapon[3]
            the_props = the_props.replace('balanced', 'balanced, heavy, light')
            # find weapon properties...
            props = self.char.db.query('SELECT name, description ' +
                                       'FROM equipment_properties ' +
                                       'WHERE {}'
                                       .format(' OR '.join(['Name LIKE \'{}\''
                                                            .format(a) for a
                                                            in the_props
                                                            .split(', ')])))
            try:
                props.sort()
            except:
                pass
            # set damage/max damage
            if 'bow' in weapon[3]:
                dmg = blevel
                dmax = len(lst_dmg) - 1
            else:
                dmg = level
                dmax = 0
            try:
                for prop in props:
                    if '+1' in prop[1]:
                        dmax += 1
                    if prop[0] == 'balanced':
                        dmax -= 2
            except:
                pass
            if dmax >= len(lst_dmg) - 1:
                dmax = len(lst_dmg) - 1
            if dmax <= dmg:
                dmg = dmax

            ret = ret + '<tr><td {}>'.format(al)  # start weapon column 1
            ret = ret + ('<div class="dropdown" style="min-width: 100%;">' +
                         '<button class="dropbtn-wa" style="min-width 100%;">')
            ret = ret + ('<b><span style="float: left;">{}</b></span>'
                         .format(weapon[1]))
            ret = ret + ('<div style="font-size: 75%; float: right;' +
                         'max-width: 100%;"><i>{}'
                         .format(weapon[3]) + '</i></div>')
            if 'arrow' in weapon[3]:
                for thing in qt:
                    if thing[0] == weapon[0]:
                        wloc = thing[2]
                        ret = ret + '<br><span style="float: right; font-size: 75%;">'
                        ret = ret + '\<b>|</b>/ '*int(thing[1])
                        ret = ret + '</span>'
            else:
                ret = ret + '<br><span style="float: right; font-size: 75%;">'
                ret = ret + 'Damage: {}'.format(lst_dmg[dmg])
                ret = ret + ' (Max {})'.format(lst_dmg[dmax])
            ret = ret + '</button><div class="dropdown-content">'
            for prop in props:
                ret = ret + "<b>{}</b></br>".format(prop[0])
                ret = ret + ind + ('<i>{}</i><br>'
                                   .format(prop[1])
                                   .replace('Passive:',
                                            '&nbsp&nbsp;&nbsp;Passive:')
                                   .replace('Active:',
                                            '<br>&nbsp&nbsp;&nbsp;Active:'))
                if 'arrow' in weapon[3]:
                    for thing in qt:
                        done = 0
                        if thing[0] == weapon[0] and done == 0:
                            done = 1
                            ret = ret + ('<a href="/com_del_1item_{}_{}">'
                                         .format(weapon[0], thing[2]) +
                                         '<center><i><b>- Loose One -' +
                                         '</i></b></center></a>')
            ret = ret + '</div></div></td></tr>'  # end weapons

        # Armor
        ret = ret + ('<tr><td colspan="2"><div style="font-family: '+
                     'Papyrus, fantasy; font-size: 14px; font-variant' +
                     ':small-caps; text-align: center; float: center;">' +
                     '- Armor -</div></td></tr>')
        qarmor = self.char.db.query('SELECT * FROM equipment ' +
                                      'WHERE tags LIKE \'%armor%\' '
                                      'AND _id IN '
                                        '(SELECT item ' +
                                        'FROM PC_inventory ' +
                                        'WHERE character={} '
                                        .format(self.char.id) +
                                        'AND worn=1)')
        armor = defaultdict(lambda: [0, 0, 0])
        properties = defaultdict(list)
        arm_names = defaultdict(list)
        base_armor = defaultdict(int)
        locs = ['head', 'torso', 'rarm', 'larm', 'lleg', 'rleg']
        names = ['Head', 'Torso', 'Right Arm', 'Left Arm',
                 'Left Leg', 'Right Leg' ]
        # these based on
        # https://www.quora.com/
        # Whats-the-weight-distribution-in-the-average-human-body
        # and http://www.sciencemag.org/news/2011/07/
        # heavy-armor-gave-knights-workout
        enc_lst = [0.1, 0.5, 0.05, 0.05, 0.2, 0.2]
        encumbrance = 0.0
        for q in qarmor:
            for i, loc in enumerate(locs):
                if loc in q[13]:
                    armor[loc][0] = armor[loc][0] + int(q[10])
                    armor[loc][1] = armor[loc][1] + int(q[11])
                    armor[loc][2] = armor[loc][2] + int(q[12])
                    try:
                        properties[loc] = list(set(properties[loc] +
                                                    q[3].split(', ')))
                    except:
                        properties[loc] = list(set(properties[loc].append(q[3])))
                    if 'light armor' in q[3]:
                        if base_armor[loc] <= 1:
                            base_armor[loc] = 1
                            encumbrance = encumbrance + 1.0*enc_lst[i]
                    elif 'medium armor' in q[3]:
                        if base_armor[loc] <= 2:
                            base_armor[loc] = 2
                            encumbrance = encumbrance + 2.0*enc_lst[i]
                    elif 'heavy armor' in q[3]:
                        if base_armor[loc] <= 3:
                            base_armor[loc] = 3
                            encumbrance = encumbrance + 3.0*enc_lst[i]
                    elif 'full armor' in q[3]:
                        if base_armor[loc] <= 4:
                            base_armor[loc] = 4
                            encumbrance = encumbrance + 4.0*enc_lst[i]
                    arm_names[loc].append(q[1])
        j = 0
        for i, loc in enumerate(locs):
            al = ''
            if (base_armor[loc] >= 1):
                j += 1
                if i % 2 == 1:
                    al = ' style="background-color:#eee;"'
                ret = ret + '<tr><td {}>'.format(al)
                ret = ret + ('<div class="dropdown" style="min-width: 100%;">' +
                             '<button class="dropbtn-wa" style="min-width 100%;">')
                ret = ret + ('<b><span style="float: left;">{}</b></span>'
                             .format(names[i]))
                ret = ret + ('<div style="float: right;' +
                             'max-width: 100%;"><i>Armor ')
                if int(base_armor[loc] + armor[loc][0] - 1) >= 0:
                    ret = ret + ('{}'.format(lst_dmg[int(base_armor[loc] +
                                            armor[loc][0]) - 1]))
                else:
                    ret = ret + '-None-'
                if int(base_armor[loc] + armor[loc][1] - 1) >= 0:
                    ret = ret + (', {} vs Arrows'.format(lst_dmg[base_armor[loc] +
                                                                armor[loc][1] -
                                                                 1]))
                if int(base_armor[loc] + armor[loc][2] - 1) >= 0:
                    ret = ret + (', {} vs Blades'.format(lst_dmg[base_armor[loc] +
                                                                armor[loc][2] -
                                                                 1]))
                ret = ret + '</i></div><br><span style="float: left; font-size: 75%;">'
                ret = ret + '<i>{}<i></span>'.format(', '.join(arm_names[loc]))

                # find armor properties...
                props = self.char.db.query('SELECT name, description ' +
                                           'FROM equipment_properties ' +
                                           'WHERE {}'
                                           .format(' OR '.join(['Name LIKE \'{}\''
                                                                .format(a) for a
                                                                in properties[loc]
                                                                ])))
                ret = ret + '</button><div class="dropdown-content">'
                for prop in props:
                    ret = ret + "<b>{}</b></br>".format(prop[0])
                    ret = ret + ind + ('<i>{}</i><br>'
                                       .format(prop[1])
                                       .replace('Active:',
                                                '<br>&nbsp;&nbsp;&nbsp;Active:'))
                ret = ret + '</div></div></td></tr>'  # end Armor table
        askill = self.char.skills['Armor'][-1]
        print(encumbrance, askill)
        encumbrance = encumbrance - askill
        print(encumbrance)
        if encumbrance <= 0:
            encumbrance = 0.0
        ret = ret + ('<tr><td><span style="text-align: center; ' +
                      'float: center;"><i>Armor ' +
                      'Encumbrance: {} ({:.2f})'.format(int(encumbrance),
                                                    encumbrance) +
                      '</span></td></tr>')
        ret = ret + '</table>'  # close full table
        return ret
