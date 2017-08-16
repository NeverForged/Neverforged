


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
            print(self.char.wounds.wounds, self.char.wounds.stun, j)
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
            ret = ret + ('<a href="/heal_dmg_{}">-[&nbsp;&nbsp;] {} Healing -</a>'
                        .format(6 - i, wnd))
            for k in range(10):
                ret = ret + ('<a href="/apply_dmg_{}_{}_{}_{}">'
                             .format(thr[i], k,
                                     self.char.trait_values[2], 0) +
                             '{}: [x] - {}</a>'
                             .format(k, loc[k]))
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
        ret = ret + ('<colspace>'
                     '<col width=50% style="text-align: left;">' +
                     '<col width=50% style="text-align: right;">')
        # Weapons
        ret = ret + ('<tr><td colspan="2"><div style="font-family: '+
                     'Papyrus, fantasy; font-size: 14px; font-variant' +
                     ':small-caps; text-align: center; float: center;">' +
                     '- Weapons & Shields -</div></td></tr>')
        weapons = self.char.db.query('SELECT * FROM equipment ' +
                                      'WHERE tags LIKE \'%weapon%\' '
                                      'AND _id IN '
                                      '   (SELECT item ' +
                                      '    FROM PC_inventory ' +
                                      '    WHERE character={} '
                                      .format(self.char.id)
                                      '    AND loc IN '
                                      '       (SELECT slot ' +
                                      '        FROM inventory_slots ' +
                                      '        WHERE name LIKE \'-%\' OR ' +
                                      '        name LIKE \'Back\' OR ' +
                                      '        name LIKE \'%Shoulder\' ))')
        for i, weapon in enumerate(weapons):
            al = ''
            if i % 2 == 1:
                al = ' style="background-color:#eee;"'
            ret = ret + '<tr><div class="dropdownsk"><button class="dropbtnsk">'
            ret = ret + '<td {}>'.format(al)  # start weapon column 1
            ret = ret + '<b>{}</b>'.format(weapon[1])
            ret = ret + '</td><td {}>'.format(al)  # start weapon column 2
            ret = ret + '<div style="font-size: 75%>{}</div>'.format(weapon[1])
            ret = ret + '</button>'
            ret = ret + '</div></div></td></tr>'
        # Armor
        ret = ret + ('<tr><td colspan="2"><div style="font-family: '+
                     'Papyrus, fantasy; font-size: 14px; font-variant' +
                     ':small-caps; text-align: center; float: center;">' +
                     '- Armor -</div></td></tr>')
        ret = ret + '</table>'  # close full table
        return ret
