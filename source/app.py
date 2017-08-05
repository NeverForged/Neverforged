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
    print(user)
    lst = ['S', 'D', 'F', 'C', 'I', 'W']
    trt_adds = []
    for item in lst:
        try:
            trt_adds.append(int(request.args.get(item, None)))
            print(trt_adds)
        except:
            trt_adds.append(0)
    print(trt_adds)
    try:
        ans = request.args.get('answer', None)
    except:
        ans = ''
    try:
        filt = request.args.get('filter', None)
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
        print(type(cc))
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
    '''
    pass

def check_ip():
    '''
    Makes sure the ip has a listed user...
    '''
    ip = request.remote_addr
    try:
        uh.user_d[ip] = user
        return ip
    except:
        return redirect('/')



if __name__ == '__main__':

     app.run(host='0.0.0.0', port=8888, debug=True)
