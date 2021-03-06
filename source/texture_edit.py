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
    print(rav, gav, bav)
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

def double_texture(file1, file2):
    fname = '../images/texture/' + file1
    im1 = Image.open(fname).convert('RGBA')
    pix1 = im1.load()
    fname = '../images/texture/' + file2
    im2 = Image.open(fname).convert('RGBA')

    pix2 = im2.load()
    w=im2.size[0]
    h=im2.size[1]
    img = Image.new( im2.mode, im2.size)
    pix_new = img.load()
    for i in range(w):
      for j in range(h):
          clrs1 = pix1[i, j]
          clrs2 = pix2[i, j]
          pix_new[i, j] = (clrs1[0] + clrs2[0] - 221,
                           clrs1[1] + clrs2[1] - 221,
                           clrs1[2] + clrs2[2] - 221,
                           clrs2[3])
    img.save(fname,"PNG")


if __name__ == '__main__':
    try:
        if sys.argv[1] == '@':
            file1 = sys.argv[2]
            file2 = sys.argv[3]
            double_texture(file1, file2)
        else:
            fname = sys.argv[1]
            main('../images/texture/' + fname)
    except:
        for f in os.listdir('../images/appearance'):
            if f.endswith(".png"):
                print(str(f))
                main('../images/appearance/' + str(f))
