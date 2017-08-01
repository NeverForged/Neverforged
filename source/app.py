import os
import sys
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from Appearance import Appearance
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

@app.route('/draw/<specs>.png')
def draw(specs):
    plt.ioff()
    #if not os.path.exists('/static/images/' + self.specs + '.png'):
    print('need to draw this combination')
    fig, ax = plt.subplots(1, figsize=(4.0, 6.0))
    appr = Appearance(None, None, ax, specs)
    appr.draw_char()
    appr.show()
    time.sleep(1)
    # return redirect("../source/static/images/" + specs + ".png", code=302)
    return redirect('/static/images/temp.png')


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8880, debug=True)
