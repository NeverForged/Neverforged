import os
import sys
import numpy as np
from PIL import Image

def main(fname):
    '''
    Edits a texture file to be colored with an average of 100.
    '''
    image = Image.open(fname).convert('RGBA')
    r, g, b = (221, 221, 221)
    R = []
    G = []
    B = []
    pix_old = image.load()
    img = Image.new( image.mode, image.size)
    pix_new = img.load()
    w=image.size[0]
    h=image.size[1]
    # find avergae value of all vars...
    for i in range(w):
      for j in range(h):
        temp = pix_old[i, j]
        if temp[3] > 0:
            R.append(temp[0])
            G.append(temp[1])
            B.append(temp[2])
    # avaoid NaN
    lst = [R, G, B]
    for cl in lst:
        if len(cl) == 0:
            cl.append(0)
    rav = int(np.mean(R))
    gav = int(np.mean(G))
    bav = int(np.mean(B))
    for i in range(w):
      for j in range(h):
        clrs = pix_old[i, j]
        ar = clrs[0]
        ag = clrs[1]
        ab = clrs[2]
        alp = clrs[3]
        if clrs[3] > 0:
            ar = clrs[0] - rav + r
            ag = clrs[1] - gav + g
            ab = clrs[2] - bav + b
        pix_new[i,j] = (ar, ag, ab, alp)
    img.save(fname,"PNG")

if __name__ == '__main__':
    try:
        fname = sys.argv[1]
        main('../images/texture/' + fname)
    except:
        for f in os.listdir('../images/appearance'):
            if f.endswith(".png"):
                main('../images/appearance/' + str(f))
        lst = ['beard', 'ear', 'ebrow', 'hair', 'nose']
        for item in lst:
            for f in os.listdir('../images/appearance/' + item):
                if f.endswith(".png"):
                    main('../images/appearance/' + item +'/' + str(f))
