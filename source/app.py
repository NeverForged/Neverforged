import os
import sys
import time
import matplotlib
matplotlib.use('Agg')
from User import User
from Web_Temp import WebTemp
from Database import Database
import matplotlib.pyplot as plt
from Appearance import Appearance
from UserHandler import UserHandler
from flask import Flask, render_template, request, jsonify, redirect



uh = UserHandler()
campaign = 0
bg_questions = ['','','','','','','','','','','','','','','','']
bg_actual = ['','','']

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
    email = request.args.get('email', None)
    pword = request.args.get('pword', None)
    ip = request.remote_addr
    uh.add(email, pword, ip)
    return redirect('/')

@app.route('/create<var>')
def make_char(var):
    '''
    Character Creation Stuff goes here...
    '''
    global campaign
    global bg_questions
    global bg_actual
    ind = '&nbsp;&nbsp;&nbsp;'
    wb = WebTemp()
    ret = wb.start
    db = Database('NeverforgedData')
    # do work here
    if var == '_new':
        campaign = -1
        return redirect('/create_cam:0')
    elif var[:5] == '_cam:':
        ret = ret + ('<center>' +
                     '<span style="font-family: Papyrus, fantasy; ' +
                     'font-size: 30px; font-variant: small-caps;"><b>')
        ret = ret + 'Campaign' + '</b></span>'
        ret =  ret + '<br><br><div class="dropdown">'
        ret = ret + '<button class="dropbtn">Choose a Campaign</button>'
        ret = ret + '<div class="dropdown-content">'
        cams = db.query('SELECT _id, Campaign FROM campaign')
        for cam in cams:
            ret = ret + '<a href="create_cam:{}">{}</a>'.format(cam[0], cam[1])
        ret = ret + '</div></div><br><br>'
        ret =  ret + ('<span style="font-family: Georgia, Times,'+
                      ' "Times New Roman", serif;">')
        query = ('SELECT Campaign, Location, Description ' +
                'FROM campaign WHERE _id={}'.format(var[5:]))
        print(query)
        info = db.query(query)
        ret = ret + '<br><b>{}</b> (<i>{}</i>)'.format(info[0][0], info[0][1])
        ret = ret + '<br><br></center><i>{}</i><br><br><br>'.format(info[0][2])
        ret = ret +  ('<center><a href="/create_cam_conf{}">'.format(var[5:]) +
                      '**Click to choose {}**</a></center>'.format(info[0][0]))
    elif var[:9] == '_cam_conf':
        campaign = int(var[9:])
        return redirect('/create_resetbg')
    elif var == '_resetbg':
        bg_questions = ['','','','','','','','','','','','','','','','']
        return redirect('/create_question1')
    elif var[:9] == '_question':
        ret = ret + ('<center>' +
                     '<span style="font-family: Papyrus, fantasy; ' +
                     'font-size: 30px; font-variant: small-caps;">' +
                     '<b>Background Questions</b></span>')
        questions = db.query('SELECT question FROM ccquestions')
        print(campaign)
        questions.append(db.query('SELECT CCQuestion FROM campaign ' +
                                  'WHERE _id={}'.format(campaign))[0])
        ret = ret + '<br><br><div class="dropdown">'
        ret = ret + '<button class="dropbtn">Select a Question</button>'
        ret = ret + '<div class="dropdown-content">'
        for i, q in enumerate(questions):
            ret = ret + '<a href="create_question{}">{}</a>'.format(i+1, q[0])
        ret = ret + '</div></div><br><br></center>'
        # question text and input
        ret =  ret + ('<span style="font-family: Georgia, Times,'+
                      ' "Times New Roman", serif;">')
        if int(var[9:]) <= 14:
            quest = db.query('SELECT question, explanation FROM ccquestions ' +
                             'WHERE _id={}'.format(var[9:]))[0]
        else:
            quest = db.query('SELECT CCQuestion, CCExplanation FROM campaigns'
                             ' WHERE _id={}'.format(campaign))[0]
        ret = ret + '<b>{}</b><br><i>{}</i><br><br>'.format(quest[0], quest[1])
        # add a textbox and answer space...
        ret = ret + ('<center><form action="/create_ans{}">'.format(var[9:]) +
                     '<p><textarea name="answer" rows="10" cols="90">' +
                     '{}</textarea></p>'.format(bg_questions[int(var[9:])]) +
                     '<br><input type="submit" value="Save Answer"><center>')
        ret = ret + ('<br><br><br><center><a href="/create_backgrounds">' +
                     '**Click to move on to Backgrounds**</a><br><br><br>' +
                     '<center><a href="/create_cam:{}">'.format(campaign) +
                     '**Return to Campaign**</a>')
    if var[:4] == '_ans':
        bg_questions[int(var[4:])] = request.args.get('answer', None)
        if int(var[4:]) <= 14:
            return redirect('create_question{}'.format(int(var[4:]) + 1))
        else:
            return redirect('/create_backgrounds')
    if var[:12] == '_backgrounds':
        try:
            filt =  request.args.get('filter', None)
        except:
            filt = ''
        ret = ret + ('<center>' +
                     '<span style="font-family: Papyrus, fantasy; ' +
                     'font-size: 30px; font-variant: small-caps;">' +
                     '<b>Backgrounds</b></span>')
        ret = ret + '<form action="/create_backgrounds">'
        ret = ret + ('<p>Search: <input type="text" name="filter" value="">' +
                    '</p><input type="submit" value="Apply"><center>')
        # center tag here down...
        try:  # Nationality
            nat = db.query('SELECT name FROM backgrounds ' +
                           'WHERE _id={}'.format(bg_actual[0]))[0][0]
            ret = ret + ('<br><br><a href="create_bg_0_-1">' +
                         '** Change Nationality: {} **</a>'.format(nat))
        except:
            ret = ret + '<br><br><div class="dropdown">'
            ret = ret + '<button class="dropbtn">Select a Nationality</button>'
            ret = ret + '<div class="dropdown-content">'
            nats = db.query('SELECT _id, name FROM backgrounds ' +
                            'WHERE tags LIKE \'Nationality\' AND ' +
                            '(name LIKE \'%{}%\' OR '.format(filt) +
                            'description LIKE \'{}\')'.format(filt))
            for nat in nats:
                ret = ret + ('<a href="\create_bg_0_{}">'.format(nat[0]) +
                             '{}</a>'.format(nat[1]))
            ret = ret + '</div></div>'
        try:  # Progfession
            nat = db.query('SELECT name FROM backgrounds ' +
                           'WHERE _id={}'.format(bg_actual[1]))[0][0]
            ret = ret + ('<br><br><a href="create_bg_1_-1">' +
                         '** Change Profession: {} **</a>'.format(nat))
        except:
            ret = ret + '<br><br><div class="dropdown">'
            ret = ret + '<button class="dropbtn">Select a Profession</button>'
            ret = ret + '<div class="dropdown-content">'
            nats = db.query('SELECT _id, name FROM backgrounds ' +
                            'WHERE tags LIKE \'Profession\' AND ' +
                            '(name LIKE \'%{}%\' OR '.format(filt) +
                            'description LIKE \'{}\') '.format(filt) +
                            'AND (nation LIKE \'s-1e\' OR ' +
                            'nation LIKE \'%s{}e%\')'.format(bg_actual[0]))
            for nat in nats:
                ret = ret + ('<a href="\create_bg_1_{}">'.format(nat[0]) +
                             '{}</a>'.format(nat[1]))
            ret = ret + '</div></div>'
        try:
            sprk = db.query('SELECT name FROM backgrounds ' +
                            'WHERE _id={}'.format(bg_actual[2]))[0][0]
            ret = ret + ('<br><br><a href="create_bg_2_-1">' +
                         '** Change Divine Spark: {} **</a>'.format(sprk))
        except:
            ret = ret + '<br><br><div class="dropdown">'
            ret = ret + '<button class="dropbtn">Select a Divine Spark</button>'
            ret = ret + '<div class="dropdown-content">'
            nats = db.query('SELECT _id, name FROM backgrounds ' +
                            'WHERE tags LIKE \'Spark\' AND ' +
                            '(name LIKE \'%{}%\' OR '.format(filt) +
                            'description LIKE \'{}\') '.format(filt) +
                            'AND (nation LIKE \'s-1e\' OR ' +
                            'nation LIKE \'%s{}e%\')'.format(bg_actual[0]))
            for nat in nats:
                ret = ret + ('<a href="\create_bg_1_{}">'.format(nat[0]) +
                             '{}</a>'.format(nat[1]))
            ret = ret + '</div></div>'
        if len(var) >= 13:  # Display a Background
            ret = ret + "</center></center>"
            # Display Last Background pickd...
            dis = db.query('SELECT name, tags, description, abilities, ' +
                            'lang_p, lang_e ' +
                            'FROM backgrounds ' +
                            'WHERE _id={}'.format(var[12:]))[0]
            ret = ret + '<br><br><b>{}</b> [{}]'.format(dis[0], dis[1])
            ret = ret + '<br><i>{}</i><br>'.format(dis[2])
            ret = ret + ind + '<b>Ability:</b> <i>{}</i><br>'.format(dis[3])
            querylst = []
            for i in range(1, 9):
                querylst.append('SELECT skills.name FROM skills '+
                                'JOIN (SELECT skill_{}'.format(i) +
                                ' FROM backgrounds WHERE _id=' +
                                '{}'.format(var[12:]) +
                                ') as t ON t.skill_{} = skills._id'.format(i))
            query = ' UNION '.join(querylst)
            skills = db.query(query)
            ret = ret + ind + ('<b>Skills:</b> <i>{}</i><br>'
                                .format(', '.join([a[0] for a in skills])))
            if len(str(dis[4])) + len(str(dis[5])) >= 1:  # languages
                ret = ret + ind + ('<b>Languages:</b> <i>')
                lst = []
                try:
                    lst.append(db.query('SELECT name FROM skills WHERE _id' +
                                        '={}'.format(dis[4]))[0][0])
                except:
                    pass
                try:
                    lst.append(db.query('SELECT name FROM skills WHERE _id' +
                                        '={}'.format(dis[5]))[0][0])
                except:
                    pass
                try:
                    ret = ret + ', '.join(lst) + '</i></br>'
                except:
                    ret = ret + str(lst) + '</i></br>'
                    #  end languages
    if var[:4] == '_bg_':  # _bg_#_##
        if int(var[6:]) < 0:
            bg_actual[int(var[4])] = ''
            return redirect('/create_backgrounds')
        else:
            bg_actual[int(var[4])] = int(var[6:])
            return redirect('/create_backgrounds{}'.format(int(var[6:])))
    # done
    ret = ret + wb.end
    return ret, 200

@app.route('/load_<int:char_id>')
def load(char_id):
    '''
    '''
    pass

def check_ip(ip):
    '''
    Makes sure the ip has a listed user...
    '''
    ip = request.remote_addr
    try:
        uh.user_d[ip] = user
    except:
        return redirect('/')

if __name__ == '__main__':

     app.run(host='0.0.0.0', port=8888, debug=True)
