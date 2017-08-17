import os
import sys
import time
import matplotlib
matplotlib.use('Agg')
from User import User
from Dice import Roll
from Wounds import Wound
from Web_Temp import WebTemp
from Database import Database
import matplotlib.pyplot as plt
from Character import Character
from Appearance import Appearance
from UserHandler import UserHandler
from flask import Flask, render_template, request, jsonify, redirect, Response

uh = UserHandler()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    '''
    Landing page...
    '''
    wb = WebTemp()
    ret = wb.start
    # do work here
    ip = request.remote_addr
    db = Database('NeverforgedData')

    print("THE IP IS {}".format(ip))
    if ip in uh.user_d.keys():
        user_name = uh.user_d[ip].user
        ret = ret + '''
              <center>
              <img src='/static/images/neverforged_logo.png'><br><br>
              <span style='font-size: 12px'>
              ''' + 'Hello {}, welcome to Neverforged!'.format(user_name)

        # Get options for this user...
        ret =  ret + '</span><br><br><div class="dropdown">'
        ret = ret + '<button class="dropbtn">Choose Character to Load</button>'
        ret = ret + '<div class="dropdown-content">'
        ret =  ret + '<a href="/create_new">-Create New Character-</a>'

        # get characters to add to menu...
        # <a href="#">Link 2</a>
        chars = db.query('SELECT _id, name ' +
                         'FROM PC ' +
                         'WHERE user LIKE \'{}\''.format(uh.user_d[ip].user))
        # Add them...
        for char in chars:
            ret = ret + '<a href="/load_{}">{}</a>'.format(char[0], char[1])
        ret = ret + '</div></div></center>'

    else:
        ret = ret + '''
        <center>
            <span style="font-family: Georgia, Times, "Times New Roman", serif;">
            <img src='/static/images/neverforged_logo.png'><br><br>
            <form action="/user_check">
            <p>E-mail: <input type="text" name="email" value=""></p><br>
            Password: <input type="password" name="pword" value=""><br><br>
            <input type="submit" value="Submit">
            </span>
        </center>
        '''
    # ret + wb.end to finish it
    ret = ret + wb.end
    return ret, 200

@app.route('/user_check')
def user_check():
    '''
    Extract user name and info...
    email=ss&pword=ss
    '''
    print('checking...')
    email = request.args.get('email', None)
    print('email')
    pword = request.args.get('pword', None)
    ip = request.remote_addr
    print(ip)
    uh.add(email, pword, ip)
    print(email)
    return redirect('/')

@app.route('/create<var>', methods=['GET','POST'])
def make_char(var):
    '''
    Character Creation Stuff goes here...
    '''
    global uh
    wb = WebTemp()
    ret = wb.start
    db = Database('NeverforgedData')
    # do work here
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    # print(user)
    lst = ['S', 'D', 'F', 'C', 'I', 'W']
    trt_adds = []
    for item in lst:
        try:
            trt_adds.append(int(request.args.get(item, None)))
            # print(trt_adds)
        except:
            trt_adds.append(0)
    # print(trt_adds)
    try:
        ans = request.args.get('answer', '').replace(';',',')
    except:
        ans = ''
    try:
        filt = request.args.get('filter', '')
    except:
        filt = ' '
    try:
        name = request.args.get('name', None)
    except:
        name = ''
    try:
        cc = user.new_char
    except:
        cc = user.new_character()
        # print(type(cc))
    resp = cc.var(var, trt_adds, ans, filt, name)
    if resp[:4] == '_red':
        return redirect (resp.replace('_red', ''))
    else:
        ret = ret + resp
    # done
    ret = ret + wb.end
    return ret, 200

@app.route('/load_<int:char_id>')
def load(char_id):
    '''
    Load a character...
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    db = Database('NeverforgedData')
    user.char = Character(char_type='PC', sql_id=char_id, db=db)
    return redirect('/stats')

@app.route('/stats')
def stats():
    '''
    Stats Page...
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
        user.char.name
    except:
        return redirect('/')
    wb = WebTemp()
    ret = wb.start
    ret = ret + ('<center>' +
                 '<span style="font-family: Papyrus, fantasy; ' +
                 'font-size: 30px; font-variant: small-caps;"><b>' +
                 user.char.name + '</b></span></center>')
    # Traits and Skills...
    ret = ret + ('''
                 <table width="100%">
                 <tr>
                     <th width=50%><center><span style="font-family: Papyrus,
                         fantasy; font-size: 24px; font-variant: small-caps;">
                         <b>- Traits -</b></span></center></th>
                     <th width=50%><center><span style="font-family: Papyrus,
                         fantasy; font-size: 24px; font-variant: small-caps;">
                         <b>- Skills -</b></span></center></th>
                 </tr>
                 ''') # end headers for stats page
    # stats... nesting a table
    ret = ret + user.char.trait_table_start
    for i in range(3):
        j = i + 3
        al = ''
        if i == 1:
            al = 'style="background-color:#eee;"'
        ret = ret + ('<tr><td {}>{}</td>'
                     .format(al, user.char.trait_names[i]) +
                     '<td {}><div class="dropdown">'.format(al) +
                     '<b><button class="dropbtn">{}&nbsp;&nbsp;&nbsp;</button>'
                     .format(user.char.trait_values[i]) +
                     '<div class="dropdown-content">' +
                     '<a href="/trait_raise{}">Raise</a>'.format(i) +
                     '<a href="/trait_raise-{}">Lower</a>'.format(i) +
                     '</div></div></td>' +
                     '<td {}><div class="dropdown">'.format(al) +
                     '<button class="dropbtn">{}</button>'
                     .format(user.char.trait_dice[i]) +
                     '<div class="dropdown-content">' +
                     '<a href="/roll{}_">Roll</a>'.format(i) +
                     '<a href="/roll{}_a">Advantage</a>'.format(i) +
                     '<a href="/roll{}_d">Disadvantage</a>'.format(i) +
                     '</div></div></td><td></td>' +
                      '<td></td>'
                     '<td {}></td>'.format(al) +
                     '<td {}>{}</td>'
                     .format(al, user.char.trait_names[j]) +
                     '<td {}><div class="dropdown">'.format(al) +
                     '<b><button class="dropbtn">{}&nbsp;&nbsp;&nbsp;</button>'
                     .format(user.char.trait_values[j]) +
                     '<div class="dropdown-content">' +
                     '<a href="/trait_raise{}">Raise</a>'.format(j) +
                     '<a href="/trait_raise-{}">Lower</a>'.format(j) +
                     '</div></div></td>' +
                     '<td {}><div class="dropdown">'.format(al) +
                     '<button class="dropbtn">{}</button>'
                     .format(user.char.trait_dice[j]) +
                     '<div class="dropdown-content">' +
                     '<a href="/roll{}_">Roll</a>'.format(j) +
                     '<a href="/roll{}_a">Advantage</a>'.format(j) +
                     '<a href="/roll{}_d">Disadvantage</a>'.format(j) +
                     '</div></div></td><td></td></tr>')
    ret = ret + '</table><center></center>'
    ret = ret + ('<br><br><table width="100%" border="1px"><colgroup>{}</colgroup>'
                 .format(''.join(['<col style="width: 25%;">'
                                  for i in range(3)])))
    ret = ret + ('<tr><td colspan="4"><center>{}</center>'
                 .format(user.roll.show_roll) + '</td></tr>')
    for j in range(4):
        ret = ret + '<tr>'
        for i in range(4):
            img = user.roll.empty
            if user.roll.dice_location[i] == j:
                img = user.roll.dice_pic[i]
            ret = ret + '<td>{}</td>'.format(img)
        ret = ret + '</tr>'
    ret = ret + ('</table><center>{}</center>'
                 .format(user.roll.results))
    # SKILL TRAINING
    ret = ret + ('<table width=100%><colgroup>' +
                 '<col style="width:50%; text-align: center;"/>' +
                 '<col style="width:50%; text-align: center;"/><colgroup>' +
                 '<tr><td colspan="2"><span style="font-family: Papyrus, '+
                 'fantasy; font-size: 14px; font-variant' +
                 ':small-caps; text-align: center;">' +
                 '<br><br><b><center>- Skill Training - </center></b></span>')
    # Need this list in two places...
    skills = list(user.char.skills.keys())
    skills.sort()
    for i in range(3):
        al = ''
        if i == 1:
            al = 'style="background-color:#eee;"'
        ret =  ret + ('<tr><td {}><center><div class="dropdown">'.format(al) +
                      '<button class="dropbtn">{}</button>'
                      .format(user.char.training[i]) +
                      '<div class="dropdown-content">')
        for skill in skills:
            ret = ret + ('<a href="/skill_train_{}_{}">'.format(skill, i) +
                         '{}</a>'.format(skill))
        ret = ret + ('</div></div></center></td><td {}><center>'.format(al) +
                     '<div class="dropdown"><button class="dropbtn">{}'
                     .format(user.char.training_val[i]) +
                     '</button><div class="dropdown-content">' +
                     '<a href="/sktnset_1_{}">[x][&nbsp;&nbsp;]'.format(i) +
                     '[&nbsp;&nbsp;]</a>' +
                     '<a href="/sktnset_2_{}">[x][x][&nbsp;&nbsp;]</a>'
                     .format(i) +
                     '<a href="/sktnset_3_{}">[x][x][x]</a>'.format(i))
        if user.char.training_val[i] == '[x][x][x]':
            ret = ret + ('<a href="/skinc_{}"><i>Train Up!</i></a>'
                         .format(user.char.training[i]))
        ret = ret + '</div></div></center></td></tr>' # end skill train

    # - SKILLS -
    ret = ret + '</table></td><td><table width=100%>'
    levd = {}
    ind = '&nbsp;&nbsp;&nbsp;'
    for i, skill in enumerate(skills):
        al = 'style:"width=100%; padding-right:100%;"'
        if i % 2 == 1:
            al = ' style="width=100%; background-color:#eee;"'
        ret = ret + '<tr{}><td>'.format(al)
        lev = user.char.skills[skill][-1]
        try:
            level = levd[str(lev)]
        except:
            levd={'1':'Trained', '2':'Apprentice', '3':'Journeyman',
                  '4': 'Master'}
            level = levd[str(lev)]
        ret = ret + ('<div class="dropdownsk"><button class="dropbtn">{} - [{}]'
                     .format(skill, level) +
                     '</button><div class="dropdownsk-content">')
        # now the filler...
        ret = ret + ind + ('<b>Tags:</b> {}'
                           .format(user.char.skills[skill][2]))
        if len(user.char.skills[skill][3]) >= 1:
            ret = ret + ind + ('&nbsp;[Roll: {}]'
                               .format(user.char.skills[skill][3]))
        ret = ret + '<br>' + ind + ('<i>{}</i>'
                                    .format(user.char.skills[skill][4]))
        if len(user.char.skills[skill][5]) >= 1:
            ret = ret + '<br>' + ind + ('<b>Untrained:</b> {}'
                                        .format(user.char.skills[skill][5]))
        for i in range(int(lev)):  # just the levels they have
            if len(user.char.skills[skill][i + 6]) >= 1:
                ret = (ret + '<br>' +
                       ind + '<b>{}:</b> {}'
                             .format(levd[str(i + 1)],
                                     user.char.skills[skill][i + 6]))
        ret = ret + '</td></tr>'
    ret = ret + '</div></div></table></table>'

    # rule lookup...
    ret = ret + ('<center><br><br><span style="font-family: Papyrus, ' +
                 'fantasy; font-size: 24px; font-variant: small-caps;">' +
                 '<b>- Rulebook -</b></span>')
    ret = ret + user.rules.rules_show
    ret = ret + '<br><form action="/rules_filter">'
    ret = ret + ('<p>Search: <input type="text" name="filter" ' +
                 'value="{}">'.format(user.rules.filter).replace('None', '') +
                '</p><input type="submit" value="Apply">')
    ret = ret + ('<br><div class="dropdown">Table: <button class="dropbtn">{}'
                 .format(user.rules.table) +
                 '</button><div class="dropdown-content">')
    for table in user.rules.tables:
        ret = ret + '<a href="/rules_table_{}">{}</a>'.format(table, table)
    ret = ret + ('</div></div>&nbsp;&nbsp;&nbsp;&nbsp;' +
                 '<div class="dropdown">Tag: <button class="dropbtn">{}'
                 .format(user.rules.tag) +
                 '</button><div class="dropdown-content">')
    for tag in user.rules.tags:
        ret = ret + '<a href="/rules_tag_{}">{}</a>'.format(tag, tag)
    # done
    ret = ret + wb.end
    return ret, 200

@ app.route('/rules_tag_<tag>')
def set_rules_tag(tag):
    '''
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    user.rules.tag = tag
    user.rules.update()
    return redirect('/stats')

@app.route('/rules_table_<table>')
def set_rules_table(table):
    '''
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    user.rules.table = table
    user.rules.tag  = '-All-'
    user.rules.update()
    return redirect('/stats')

@app.route('/traits')
def red_rect():
    return redirect('/stats')

@app.route('/rules_filter')
def get_rules_filter():
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    filt = request.args.get('filter', '')
    user.rules.filter = filt
    user.rules.update()
    return redirect('/stats')

@app.route('/skinc_<skill>')
def increase_skill(skill):
    '''
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    sk_id = user.char.db.query('SELECT _id FROM skills WHERE name=\'{}\''
                               .format(skill))[0][0]
    level = int(user.char.db.query('SELECT level FROM PC_skills ' +
                                   'WHERE character={} '.format(user.char.id) +
                                  'AND skill={}'.format(sk_id))[0][0])
    if level <= 3:
        user.char.db.query('UPDATE PC_skills SET level={} '.format(level + 1) +
                           'WHERE character={} AND skill={}'
                           .format(user.char.id, sk_id))
    idx = user.char.training.index(skill)
    user.char.training[idx] = '-pick a skill to train-'
    user.char.training_val[idx] = '[&nbsp;&nbsp;][&nbsp;&nbsp;][&nbsp;&nbsp;]'
    return redirect('/stats')

@app.route('/skill_train_<var>')
def set_skill_training(var):
    '''
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    lst = var.split('_')
    user.char.training[int(lst[1])] = lst[0]
    user.char.training_val[int(lst[1])] = ('[&nbsp;&nbsp;][&nbsp;&nbsp;]'+
                                           '[&nbsp;&nbsp;]')
    return redirect('/stats')

@app.route('/sktnset_<var>')
def skill_box(var):
    '''
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    if lst[0] == '1':
        user.char.training_val[int(lst[1])] = '[x][&nbsp;&nbsp;][&nbsp;&nbsp;]'
    elif lst[0] == '2':
        user.char.training_val[int(lst[1])] = '[x][x][&nbsp;&nbsp;]'
    elif lst[0] == '3':
        user.char.training_val[int(lst[1])] = '[x][x][x]'
    return redirect('/stats')

@app.route('/roll<var>')
def roll(var):
    '''
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    trts = ['Strength', 'Dexterity', 'Fortitude',
            'Charisma', 'Intelligence', 'Willpower']
    lst = var.split('_')
    user.roll = Roll(user.char.trait_dice[int(lst[0])], lst[1],
                     trts[int(lst[0])])
    user.roll.web_show()
    return redirect('/stats')

@app.route('/reroll<var>')
def rereoll(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    if lst[0] == 'e':
        user.roll.explode(int(lst[1]))
    else:
        user.roll.reroll(int(lst[1]))
    user.roll.web_show()
    return redirect('/stats')

@app.route('/trait_raise<var>')
def t_raise(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    tr = int(var)
    vals = []  #left in tuple format, must correct
    up = 1
    if tr <= 0:
        tr = -1*tr
        up = -1
    for i, val in enumerate(user.char.trait_values):
        if i == tr:
            vals.append(val + up)
        else:
            vals.append(val)
    user.char.trait_values = vals
    user.char.save()
    char_id = user.char.id
    db = user.char.db
    user.char = Character(char_type='PC', sql_id=char_id, db=db)
    return redirect('/stats')

@app.route('/appearance-background')
def app_bg():
    '''
    Appearance and Background pages
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
        user.char.name
    except:
        return redirect('/')
    user.char.app.show()
    wb = WebTemp()
    ret = wb.start
    ret = ret + ('<center>' +
                 '<span style="font-family: Papyrus, fantasy; ' +
                 'font-size: 30px; font-variant: small-caps;"><b>' +
                 user.char.name + '</b></span></center>')
    # Traits and Skills...
    ret = ret + ('''
                 <table width="100%">
                 <colgroup><col style="width:50><col style="width:50%;">
                 </colgroup>
                 <tr>
                     <th width=50%><center><span style="font-family: Papyrus,
                         fantasy; font-size: 24px; font-variant: small-caps;">
                         <b>- Attributes -</b></span></center></th>
                     <th width=50%><center><span style="font-family: Papyrus,
                         fantasy; font-size: 24px; font-variant: small-caps;">
                         <b>- Appearance -</b></span></center></th>
                 </tr>
                 ''') # end headers for stats page
    # List of things that can be set...
    ret = ret + '</table>{}'.format(user.char.appearance_selectors())
    ret = ret + '{}'.format(user.char.appearance_webshow())
    # Background editing...
    ret = ret + '''
                <table width=100%>
                <tr>
                    <th><center><span style="font-family: Papyrus,
                        fantasy; font-size: 24px; font-variant: small-caps;">
                        <b>- Background -</b></span></center></th>
                </tr>
                '''
    ret = ret + user.char.background_selector()
    # done
    ret = ret + wb.end
    return ret, 200

@app.route('/set_app_<var>')
def set_appear(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('=')
    query = ('UPDATE PC SET {}='.format(lst[0]) +
                       '\'{}\' WHERE _id={}'.format(lst[1], user.char.id))
    user.char.db.query(query)
    if lst[0][:3] != 'app':
        user.char.app.update_body()
    if lst[0] == 'pheno' or lst[0][:3] == 'app':
        user.char.app.update_items()
    user.char.app.draw_char()
    return redirect('/appearance-background')

@app.route('/update_bg_ans<int:var>')
def update_bg(var):
    '''
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    ans = [request.args.get('answer{}'.format(a), ' ') for a in range(1,16)]
    user.char.db.query('UPDATE PC SET {}'
                       .format(','.join(['q{}=\'{}\''.format(i + 1, a) for
                                         i, a in enumerate(ans)])) +
                       ' WHERE _id={}'.format(user.char.id))
    return redirect('/appearance-background')

@app.route('/equipment-inventory')
def eq_iv():
    '''
    Equipment-Iventory-Store Page
    todo list:
            equip
            store
            split
            (combine = automatic)
    '''

    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
        user.char.name
    except:
        return redirect('/')
    user.char.equip.update_items()
    user.char.app.show()
    wb = WebTemp()
    ret = wb.start

    ret = ret + ('<center>' +
                 '<span style="font-family: Papyrus, fantasy; ' +
                 'font-size: 30px; font-variant: small-caps;"><b>' +
                 user.char.name + '</b></span></center>')
    ret = ret + '{}'.format(user.char.appearance_webshow_2())
    # Traits and Skills...
    ret = ret + '''
                 <table width="50%">
                 <tr>
                     <th width=100%><center><span style="font-family: Papyrus,
                         fantasy; font-size: 24px; font-variant: small-caps;">
                         <b>- Equipment -</b></span></center></th>
                 </tr>
                 ''' # end headers for stats page
    ret = ret + '<tr><td>'
    ret = ret + user.char.equip.display_equipment()
    ret = ret + '</td></tr></table>'
    # Inventory and Store
    ret = ret + ('''
                 <table width="100%">
                 <colgroup><col style="width:50><col style="width:50%;">
                 </colgroup>
                 <tr>
                     <th width=50%><center><span style="font-family: Papyrus,
                         fantasy; font-size: 24px; font-variant: small-caps;">
                         <b>- Add & Purchase Items -</b></span></center></th>
                     <th width=50%><center><span style="font-family: Papyrus,
                         fantasy; font-size: 24px; font-variant: small-caps;">
                         <b>- Inventory -</b></span></center></th>
                 </tr>
                 ''')
    ret = ret + '<tr><td>'
    ret = ret + user.char.equip.display_store()
    ret = ret + '</td><td>'
    ret = ret + user.char.equip.display_inventory()
    # DONE
    ret = ret + wb.end
    return ret, 200

@app.route('/equip_item_<var>')
def equip(var):
    '''
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
        user.char.name
    except:
        return redirect('/')
    print(var)
    lst = var.split('_')
    print(lst)
    user.char.equip.equip_item_slot(lst[0], lst[1])
    user.char.app.update_items()
    user.char.app.draw_char()
    user.char.app.show()
    return redirect('/equipment-inventory')

@app.route('/store_filter')
def get_store_filter():
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    filt = request.args.get('filter', '')
    user.char.equip.filter = filt
    return redirect('/equipment-inventory')

@app.route('/store_tags_<var>')
def set_store_tags(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    user.char.equip.tags = var
    return redirect('/equipment-inventory')

@app.route('/store_prop_<var>')
def set_store_prop(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    user.char.equip.prop = var
    return redirect('/equipment-inventory')

@app.route('/additem_<var>')
def additem(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    user.db.add_item(int(lst[0]), user.char.id, int(lst[1]))
    return redirect('/equipment-inventory')

@app.route('/buyitem_<var>')
def buyitem(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    user.char.equip.buy_item(int(lst[0]), int(lst[1]), int(lst[2]))
    return redirect('/equipment-inventory')

@app.route('/del_1item_<var>')
def del_1item(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    user.char.equip.delete_1item(lst[0], lst[1])
    return redirect('/equipment-inventory')

@app.route('/com_del_1item_<var>')
def del_1item_com(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    user.char.equip.delete_1item(lst[0], lst[1])
    return redirect('/combat')

@app.route('/del_allitem_<var>')
def del_allitem(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    user.char.equip.delete_allitem(lst[0], lst[1], lst[2])
    return redirect('/equipment-inventory')

@app.route('/split_item_<var>')
def split_item(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    print(lst)
    user.char.equip.split_stack(lst[0], lst[1], lst[2])
    return redirect('/equipment-inventory')

@app.route('/moveitem_<var>')
def moveitem(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    print(lst)
    user.char.equip.move_item(lst[0], lst[1], lst[2], lst[3])
    return redirect('/equipment-inventory')

@app.route('/sell_item_<var>')
def sell_item(var):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst =  var.split('_')
    user.char.equip.sell_item(lst[0], lst[1], lst[2])
    return redirect('/equipment-inventory')

@ app.route('/combat')
def combat():
    # make sure valid user...
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
        user.char.name
    except:
        return redirect('/')
    wb = WebTemp()
    ret = wb.start
    ret = ret + ('<center>' +
                 '<span style="font-family: Papyrus, fantasy; ' +
                 'font-size: 30px; font-variant: small-caps;"><b>' +
                 user.char.name + '</b></span></center>')
    # Traits and Skills...
    ret = ret + ('''
                 <table width="100%">
                 <tr>
                     <th width=50%><center><span style="font-family: Papyrus,
                         fantasy; font-size: 24px; font-variant: small-caps;">
                         <b>- Armor & Weapons -</b></span></center></th>
                     <th width=50%><center><span style="font-family: Papyrus,
                         fantasy; font-size: 24px; font-variant: small-caps;">
                         <b>- Wounds & Hit Locations -</b></span></center></th>
                 </tr>
                 ''') # end headers for stats page

    ret = ret + '</div></div></td></tr>'
    ret = ret + '<tr><td>' + user.char.combat.weapons()
    ret = ret + '</td><td>' + user.char.combat.wounds()
    ret = ret + '</td></tr></table>'  # end table
    # DONE
    ret = ret + wb.end
    return ret, 200

@app.route('/apply_dmg_<var>')
def apply_damage(var):
    '''
    '''
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    lst = var.split('_')
    a = False;
    if lst[3] == '1':
        a = True
    user.char.wounds = user.char.wounds + Wound().make(int(lst[0]),
                                                        int(lst[1]),
                                                        int(lst[2]), a)
    return redirect('/combat')

@app.route('/heal_dmg_<int:level>')
def heal_dmg(level):
    ip = request.remote_addr
    try:
        user = uh.user_d[ip]
    except:
        return redirect('/')
    user.char.wounds.heal(level)
    return redirect('/combat')

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(host='0.0.0.0', port=8888, threaded=True, debug=True)
