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
from flask import Flask, render_template, request, jsonify, redirect

class UserHandler(object):
    '''
    Stores user objects in a dictionary by ip.
    '''
    def __init__(self):
        self.db = Database('NeverforgedData')
        self.user_d = {}

    def add(self, email, pword):
            user = User(email, pword)
            ip = request.remote_addr
            self.user_d[ip] = user
            print(self.user_d.keys())

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

    print("THE IP IS {}".format(ip))
    if ip in uh.user_d.keys():
        user_name = uh.user_d[ip].user
        ret = ret + '''
              <center>
              <img src='/static/images/neverforged_logo.png' width="60%"><br><br>
              <span style='font-size: 24px'>
              ''' + 'Hello {}, welcome to Neverforged!'.format(user_name)
    else:
        ret = ret + '''
        <center>
            <span style="font-family: Georgia, Times, "Times New Roman", serif;">
            <img src='/static/images/neverforged_logo.png' width="60%"><br><br>
            <form action="/user_check">
            <p >E-mail: <input type="text" name="email" value=""></p><br>
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
    uh.add(email, pword)
    return redirect('/')


if __name__ == '__main__':

     app.run(host='0.0.0.0', port=8888, debug=True)
