from Dice import Roll
from collections import defaultdict


class Equipment(object):
    '''
    Handler for Equipment, since this is a fairly intensive part
    of any game.  Manages Inventory and Equiped Items.
    '''

    def __init__(self, char):
        '''
        Initializer...
        '''
        self.char = char
        self.char_id = char.id
        self.char_s = char.trait_values[0]
        self.db = char.db
        self.update_items()
        self.filter = ''
        self.prop = 'Any'
        self.tags = 'Any'

    def update_items(self):
        '''
        '''
        self.equipment = self.db.query('SELECT item, loc '
                                       'FROM PC_inventory ' +
                                       'WHERE character={} '
                                       .format(self.char_id) +
                                       'AND worn=\'1\'')
        self.inventory = self.db.query('SELECT item, loc, qt '
                                       'FROM PC_inventory ' +
                                       'WHERE character={} '
                                       .format(self.char_id) +
                                       'AND worn=\'0\' ' +
                                       'AND loc > \'0\'')
        self.unsorted = self.db.query('SELECT item, loc, qt '
                                      'FROM PC_inventory ' +
                                      'WHERE character={} '
                                      .format(self.char_id) +
                                       'AND worn=\'0\' ' +
                                       'AND loc=\'0\'')
        self.item_nums = ([a[0] for a in self.inventory] +
                          [a[0] for a in self.unsorted])
        query = ('SELECT _id, slots FROM equipment WHERE {}'
                 .format(' OR '.join(['_id={}'.format(a) for
                         a in self.item_nums])))
        # dictionary of lists of item ids that can go in a slot.
        self.item_locations = defaultdict(list)
        for a in self.db.query(query):
            # (id, slots)
            slots = (a[1].replace('es','|').replace('s','')
                         .replace('e','').split('|'))
            for slot in slots:
                self.item_locations[slot].append(a[0])

    def display_equipment(self):
        '''
        '''
        ret = '<table width=100%>'
        # colspace
        ret = ret + ('<colspace>' +
                     '<col width=40% ' +
                     'style="text-align: right;">' +
                     '<col width=60% ' +
                     'style="text-align: center;">' +
                     '</colspace>')
        # now to make the table...
        slots = self.db.query('SELECT * from inventory_slots')
        # dictionary of equipped...
        eqed = {}
        for item in self.equipment:
            eqed[item[1]] = item[0]
        for i, slot in enumerate(slots):
            al = ''
            if i % 2 == 1:
                al = ' style="background-color:#eee;"'
            # alternate gray...
            ret = ret + '<tr><td {}>'.format(al)
            # name of slot
            ret = ret + ('<i><div style="text-align:right;"> ' +
                         '{}:</i></div></td>'.format(slot[2]))
            try:
                name = self.db.query('SELECT name ' +
                                     'FROM equipment ' +
                                     'WHERE _id={}'
                                     .format(eqed[slot[1]]))[0][0]
                check = 1
            except:
                name = '[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]'
                check = 0
            name = ('<div style="text-align:center;">{}<div>'
                    .format(name))
            # label of item in slot...
            ret = ret + ('<td><div class="dropdown">' +
                         '<button class="dropbtn">{}</button>'
                         .format(name) +
                         '<div class="dropdown-content">')
            if check == 1:
                ret = ret + ('<a href="equip_{}_{}">'
                             .format('X', slot[1]) +
                             '-clear-</a>')
            for item in self.item_locations[str(slot[1])]:
                it_nm = self.db.query('SELECT name ' +
                                      'FROM equipment ' +
                                      'WHERE _id = {}'
                                      .format(item))[0][0]
                ret = ret + ('<a href="equip_{}_{}">'
                             .format(item, slot[1]) +
                             '{}</a>'.format(it_nm))

            ret = ret + '</div></div></td></tr>'

        ret = ret + "</table>"
        return ret

    def display_inventory(self):
        '''
        '''
        ret = '<table width=100%>'
        # get all containers worn...
        query = ('SELECT equipment._id, container, pc.loc, equipment.name ' +
                 'FROM equipment ' +
                 'JOIN (SELECT * FROM PC_inventory ' +
                 '      WHERE character={} AND worn=1) as pc '
                 .format(self.char_id) +
                 'ON equipment._id = pc.item '
                 'WHERE container > 0')
        self.containers = self.db.query(query)
        query = ('SELECT * FROM equipment ' +
                 'JOIN (SELECT * FROM PC_inventory WHERE character  = {} '
                 .format(self.char_id) + 'AND worn=0) as pc ' +
                 'ON pc.item = equipment._id ')
        items = {}
        for item in self.db.query(query):
            items[int(item[0])] = item

        query = ('SELECT pc.loc, SUM(equipment.wt * pc.qt) ' +
                 'FROM equipment ' +
                 'JOIN (SELECT * FROM PC_inventory WHERE character  = {} '
                 .format(self.char_id) + 'AND worn=0) as pc ' +
                 'ON pc.item = equipment._id ' +
                 'GROUP BY pc.loc ' +
                 'ORDER BY pc.loc ')
        enc = defaultdict(float)
        for q in self.db.query(query):
            enc[int(q[0])] = q[1]
        for container in self.containers:
            name = self.db.query('SELECT name FROM equipment WHERE _id={}'
                                 .format(container[0]))[0][0]
            lname = self.db.query('SELECT name FROM inventory_slots WHERE slot={}'
                                 .format(container[2]))[0][0]
            weight = enc[int(container[2])]
            encumb = int(weight/(self.char_s * container[1]))
            disp = '[Wt. {:.2f}]'.format(weight)
            if encumb >= 1:
                disp = '<i>Encumbrance {}!</i> &nbsp;'.format(encumb) + disp
            ret = ret + ('<tr><td style="color: #ffffff; ' +
                         ' background-color: #101010; text-align: left;">' +
                         '<b>{}</b> ({})'.format(name, lname) +
                         '<div style="float: right;">{}</div>'.format(disp))
            # find the items in there...
            stored = self.db.query('SELECT item, qt FROM PC_inventory ' +
                                   'WHERE character={} AND loc={}'
                                   .format(self.char_id, container[2]))
            for i, st in enumerate(stored):
                try:
                    ret = ret + self.item_display_inv(i, items[int(st[0])], st[1],
                                                  container[2])
                except:
                    pass
        # unsorted things...
        ret = ret + ('<tr><td style="color: #ffffff; ' +
                     ' background-color: #101010; text-align: left;">' +
                     '<b>Unsorted Items</b></td></tr>')
        stored = self.db.query('SELECT item, qt FROM PC_inventory ' +
                               'WHERE character={} AND loc=0'
                               .format(self.char_id))
        for i, st in enumerate(stored):
            ret = ret + self.item_display_inv(i, items[int(st[0])], st[1], 0)
        return ret

    def item_display_inv(self, i, item, qt, loc):
        '''
        Returns a string with all the drop-down code for an item.
        '''
        ind = '&nbsp;&nbsp;&nbsp;'
        al = ''
        if i % 2 == 1:
            al = 'style="background-color:#eee;"'
        ret = '<tr><td {}>'.format(al)
        ret = ret + ('<div class="dropdownsk" style="min-width: 100%;">' + ind +
                     '<button class="dropbtn" style="min-width 100%;">{}'
                     .format(item[1]))
        if qt > 1:
            ret = ret + ' (x{})'.format(qt)
        ret = ret + '</button>'
        ret = ret + ('<div style="float: right; ' +
                     ' max-width: 100%;">Wt. {:.2f} lbs.'
                     .format(float(qt) * float(item[7])))
        ret = ret + '<div class="dropdownsk-content">'
        # item is displayed...now the fun stuff.
        # tags
        ret = ret + ind + ind + '<b>[{}]</b><br>'.format(item[2])
        if item[3] != 0:
            ret = ret + ind + ind + '<i>({})</i><br>'.format(item[3])
        ret = ret + ind + ind + '<i>{}</i><br><br>'.format(item[8])
        if int(qt) == 1:
            ret = ret + ('<a href="/del_allitem_{}_{}_{}"><center>- Delete {} -'
                         .format(item[0], loc, qt, item[1]) + '</center></a>')
        else:
            ret = ret + ('<a href="/del_1item_{}_{}"><center>- Delete 1 {} -'
                         .format(item[0], loc, item[1]) + '</center></a>')
            ret = ret + ('<a href="/del_allitem_{}_{}_{}"><center>'
                         .format(item[0], loc, qt) +
                         '- Delete all {}s -</center></a>'.format(item[1]))
            ret = ret + ('<a href="/split_item_{}_{}_{}">'.format(item[0], qt, loc) +
                         '<center>- Split Stack -</center></a>')
        for cont in self.containers:
            if int(loc) != int(cont[2]):
                locname = self.db.query('SELECT name FROM inventory_slots ' +
                                        'WHERE slot={}'.format(cont[2]))[0][0]
                ret = ret + ('<a href="/moveitem_{}_{}_{}_{}">'
                            .format(item[0], qt, loc, cont[2]) +
                            '<center> - Move to {} ({}) -</center></a>'
                            .format(cont[3], locname))
        ret = ret + ('<a href="/sell_item_{}_{}_{}"><center>- Sell {} -'
                     .format(item[0], qt, loc, item[1]) + '</a></center>')
        return ret + '</div></div></td></tr>'

    def display_store(self):
        '''
        '''
        ret = '<table width=100%>'
        # calculate wealth...
        query = ('SELECT SUM(PC_inventory.qt*cash.cost) ' +
                 'FROM PC_inventory '
                 'JOIN(SELECT _id, cost FROM equipment ' +
                 '     WHERE tags LIKE \'%money%\') as cash ' +
                 'ON cash._id = PC_inventory.item ' +
                 'WHERE PC_inventory.character={}'
                 .format(self.char_id))
        self.wealth = self.db.query(query)[0][0] # money character has
        ret = ret + ('<tr><td colspan="2"><center>' +
                     '<i>Wealth &nbsp;&nbsp;' +
                     '<span style="color: #b87333;"><b>{}'
                     .format(self.wealth) +
                     '&nbsp;pence</b></i></span>' +
                     '</center></td></tr>')
        ret = ret + '<tr><td colspan="2">'
        ret = ret + '<form action="/store_filter">'
        ret = ret + ('Name: <input type="text" name="filter" ' +
                     'value="{}">'
                     .format(self.filter) +
                     '<input type="submit" value="Apply">')
        ret = ret + '&nbsp;&nbsp; Tags: '
        ret = ret + ('<div class="dropdown">' +
                     '<button class="dropbtn">{}</button>'
                     .format(self.tags) +
                     '<div class="dropdown-content">')
        # all tags given the other filters
        tags = self.db.query('SELECT tags ' +
                              'FROM equipment ' +
                              'WHERE name LIKE \'%{}%\' '
                              .format(self.filter) +
                              'AND properties like \'%{}%\' '
                              .format(self.prop.replace('Any','')) +
                              'GROUP BY tags ' +
                              'ORDER BY tags')
        ret = ret + '<a href="/store_tags_Any">Any</a>'
        taglst = []
        for tag in tags:
            try:
                for t in tag[0].split(', '):
                    taglst.append(t)
            except:
                taglst.append(tag[0])
        taglst = list(set(taglst))
        taglst.sort()
        for tag in taglst:
            ret = ret + ('<a href="/store_tags_{}">{}</a>'
                         .format(tag, tag))
        ret = ret + '</div></div>&nbsp; Properties: '
        ret = ret + ('<div class="dropdown">' +
                     '<button class="dropbtn">{}</button>'
                     .format(self.prop) +
                     '<div class="dropdown-content">')
        # all properties given the other filters
        props = self.db.query('SELECT properties ' +
                              'FROM equipment ' +
                              'WHERE name LIKE \'%{}%\' '
                              .format(self.filter) +
                              'AND tags like \'%{}%\' '
                              .format(self.tags.replace('Any','')) +
                              'GROUP BY properties ' +
                              'ORDER BY properties')
        ret = ret + '<a href="/store_prop_{}">Any</a>'
        properties = []
        for prop in props:
            try:
                for pro in prop[0].split(', '):
                    properties.append(pro)
            except:
                if prop[0] != 0:
                    properties.append(prop[0])
        properties = list(set(properties))
        properties.sort()
        for prop in properties:
            ret = ret + ('<a href="/store_prop_{}">{}</a>'
                         .format(prop, prop))
        ret = ret + '</div></div></td></tr>'
        ret = ret + '<tr><td><b>&nbsp;&nbsp;&nbsp;&nbsp;Item</b>'
        ret = ret + ('<span style="float: right; ' +
                     'color: #b87333;"><b>Cost</b></i></span>')
        # Actual item listings now...
        items = self.db.query('SELECT * ' +
                              'FROM equipment ' +
                              'WHERE name LIKE \'%{}%\' '
                              .format(self.filter) +
                              'AND tags like \'%{}%\' '
                              .format(self.tags.replace('Any','')) +
                              'AND properties like \'%{}%\' '
                              .format(self.prop.replace('Any','')) +
                              'GROUP BY name ' +
                              'ORDER BY name')
        for i, item in enumerate(items):
            ind = '&nbsp;&nbsp;&nbsp;'
            al = ''
            if i % 2 == 1:
                al = 'style="background-color:#eee;"'
            ret = ret + '<tr><td {}>'.format(al)
            # Item(props) [tags] - (x qt)
            disp = item[1]
            # if item[3] != 0:  # has properties
            #     disp = disp +'({})'.format(item[3])
            # disp = disp + '[{}]'.format(item[2])
            if item[6] != 1:
                disp = disp + ' - (x {})'.format(item[6])
            ret = ret + ('<div class="dropdownsk" style="min-width: 100%;">' +
                         '<button class="dropbtn" style="min-width 100%;">{}'
                         .format(disp) +
                         '</button><div style="float: right; ' +
                         ' max-width: 100%; color: #b87333;"><b><i>&nbsp;{}'
                         .format(item[4]) +
                         ' pence</b></i></div>' +
                         '<div class="dropdownsk-content">')
            ret = ret + ind + '<b>[{}]</b><br>'.format(item[2])
            if item[3] != 0:  # has properties
             ret = ret + ind + '<i>({})</i><br>'.format(item[3])
            if item[6] != 1:
                ret = ret + ind + ('<b>Quantity:</b> {}<br>'
                                   .format(item[6]))
            ret = ret + ind + ('<b>Weight:</b> {} lbs.<br>'
                               .format(item[7]))
            ret = ret + '<br>' + ind + ('<i>{}</i><br><br>'
                                        .format(item[8]))
            ret = ret + ('<center><a href="/additem_{}_{}">'
                         .format(item[0], item[6]) +
                         '- click to ADD {} {} to Inventory -</a>'
                         .format(item[6], item[1]) + '</center>')
            if item[4] <= self.wealth:
                ret = ret + ('<center><a href="/buyitem_{}_{}_{}">'
                             .format(item[0], item[6], item[4]) +
                             '- click to BUY {} {} for {} pence -</a>'
                             .format(item[6], item[1], item[4]) +
                              '</center>')
            ret = ret + '</div></div></td></tr>'
        return ret + '</table>'


    def equip_item_slot(self, item_id, slot):
        '''
        Equips item with id 'item_id' in slot 'slot'
        and removes any item in said slot from that slot...
        pass item_id = 'X' to just clear the slot
        '''
        # remove all items from that slot
        self.db.query('UPDATE PC_inventory ' +
                      'SET loc=0, worn=0 ' +
                      'WHERE character={} AND loc={}'
                      .format(self.char_id, slot))
        # now replace the item in the slot...
        if item_id == 'X':
            pass
        else:
            self.db.query('UPDATE PC_inventory ' +
                          'SET loc={}, worn=1 '.format(slot) +
                          'WHERE character={} '
                          .format(self.char_id) +
                          'AND item={}'.format(item_id))


    def give_change(self, new_wealth):
        '''
        '''
        # get table_id of all money... and order by qt...
        ids = self.db.query('SELECT PC_inventory._id, PC_inventory.loc, ' +
                            'PC_inventory.qt FROM PC_inventory ' +
                            'JOIN (SELECT _id FROM equipment WHERE '+
                            '      tags like \'%money%\') as cash ' +
                            'ON PC_inventory.item = cash._id ' +
                            'WHERE character={} '.format(self.char_id) +
                            'GROUP BY PC_inventory.qt ' +
                            'ORDER BY PC_inventory.qt')
        # delete them all..
        for ID in ids:
            query = ('DELETE FROM PC_inventory WHERE _id=\'{}\''.format(ID[0]))
            self.db.query(query)
        print(self.db.query('SELECT PC_inventory._id, PC_inventory.loc, ' +
                            'PC_inventory.qt FROM PC_inventory ' +
                            'JOIN (SELECT _id FROM equipment WHERE '+
                            '      tags like \'%money%\') as cash ' +
                            'ON PC_inventory.item = cash._id ' +
                            'WHERE character={} '.format(self.char_id) +
                            'GROUP BY PC_inventory.qt ' +
                            'ORDER BY PC_inventory.qt'))
        # remove cosst from wealth
        self.wealth = new_wealth
        # add money back based on cost...
        money = self.db.query('SELECT cost, _id FROM equipment ' +
                              'WHERE tags LIKE \'%money%\' ' +
                              'GROUP BY cost ' +
                              'ORDER BY cost DESC')

        for coin in money:
            print(coin)
            add_coins = int(self.wealth / coin[0])
            print(add_coins)
            if add_coins >= 1:
                self.db.add_item(coin[1], self.char_id, add_coins, ids[0][1])
            # pence will divide evenly, so this should work out fine...
            self.wealth = self.wealth - add_coins*coin[0]


    def buy_item(self, item_id, item_qt, cost):
        '''
        '''
        self.give_change(self.wealth - cost)
        self.db.add_item(item_id, self.char_id, item_qt, 0)

    def delete_1item(self, item, loc):
        '''
        Delete a single item from that location
        '''
        query = self.db.query('SELECT _id, qt FROM PC_inventory ' +
                              'WHERE item={} AND character={} AND loc={} '
                              .format(item, self.char_id, loc))[0]
        if int(query[1]) >= 2:
             self.db.query('UPDATE PC_inventory SET qt={} '
                           .format(int(query[1]) - 1) + 'WHERE _id=\'{}\' '
                           .format(query[0]))
        else:
            self.db.query('DELETE FROM PC_inventory WHERE _id=\'{}\''
                          .format(query[0]))

    def delete_allitem(self, item, loc, qt):
        query = ('DELETE FROM PC_inventory WHERE _id IN ' +
                      '(SELECT _id FROM PC_inventory ' +
                      ' WHERE item={} AND character={} AND loc={} LIMIT 1)'
                      .format(item, self.char_id, loc))
        print(query)
        self.db.query(query)

    def split_stack(self, item, qt, loc):
        '''
        '''
        inv_id = self.db.query('SELECT _id FROM PC_inventory ' +
                               'WHERE item={} AND qt={} AND loc={}'
                               .format(item, qt, loc))[0][0]
        qt_1 = int(float(qt)/2.0)
        qt_2 = int(qt) - qt_1
        self.db.query('UPDATE PC_inventory SET qt={} WHERE _id={}'
                      .format(qt_1, inv_id))
        new_id = self.db.query('SELECT _id FROM PC_inventory ' +
                               'GROUP BY _id ORDER BY _id DESC')[0][0] + 1
        self.db.query('INSERT INTO PC_inventory ' +
                      '(_id, character, item, loc, worn, qt) ' +
                      'VALUES({},{},{},{},1,{})'
                      .format(new_id, self.char_id, item, loc, qt_2))


    def move_item(self, item, qt, loc, newloc):
        '''
        '''
        inv_id = self.db.query('SELECT _id FROM PC_inventory ' +
                               'WHERE item={} AND qt={} AND loc={}'
                               .format(item, qt, loc))[0][0]
        self.db.query('UPDATE PC_inventory SET loc={} '.format(newloc) +
                      'WHERE _id={}'.format(inv_id))

    def sell_item(self, itm_id, qt, loc):
        '''
        Sells the item, which requires:
        -getting the item cost & type
        -determing the sale price (and rolling the barter check)
        -deleting the item
        -giving the player the money


       Untrained 5*L % of the value of the goods, with an upper limit of 80%.
            treasure have an upper limit of 100%.
       Trained:e= 5*H% when selling. Treasure
                maximum of 110% of actual value.
       Apprentice: Receive 5*LH%. Treasure
                maximum of 120% of actual value.
       Journeyman: Receive 5*MH%. Treasure
                maximum of 130% of actual value.
       Master: Receive 5*LMH%. Treasure
                maximum of 140% of actual value.
        '''
        # cost and type
        value = self.db.query('SELECT cost, tags FROM equipment ' +
                              'WHERE _id={}'.format(itm_id))[0]
        # Barter Time!
        # lowest of Charisma/Intelligence
        lst = [4, '']
        if self.char.trait_values[5] < self.char.trait_values[4]:
            lst = [5, '']  # Int is lower
        trts = ['Strength', 'Dexterity', 'Fortitude',
                'Charisma', 'Intelligence', 'Willpower']
        self.char.roll = Roll(self.char.trait_dice[int(lst[0])], lst[1],
                         trts[int(lst[0])])
        self.char.roll.web_show()
        # percentage based on roll and skill... barter is 79
        try:
            lev = self.char.skill[79][-1]
        except:
            lev = 0
        if lev == 0:
            per = 0.05 * self.char.roll.L
            mt = 1
        elif lev == 1:
            per = 0.05 * self.char.roll.H
            mt = 1.1
        elif lev == 2:
            per = 0.05 * self.char.roll.LH
            mt = 1.2
        elif lev == 3:
            per = 0.05 * self.char.roll.MH
            mt = 1.3
        elif lev == 4:
            per = 0.05 * self.char.roll.LMH
            mt = 1.4

        # get amount to give...
        if 'treasure' in value[1]:
            if per >= mt:
                per = mt
        elif 'money' in value:
            per = 1.0  # can't sell money....
        else:
            if per >= 0.8:
                per = 0.8
        profit = int(float(value[0]) * float(qt) * per)
        self.delete_allitem(itm_id, loc, qt)
        self.give_change(self.wealth + profit)
