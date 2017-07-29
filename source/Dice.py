import sys
import math
import random as rnd
import matplotlib.pyplot as plt
import matplotlib.image as image
from scipy.ndimage import rotate

class Roll(object):
    '''
    Rolls a dice code in Neverforged format.
        code -> the dice code (3d6, 2d6+1d4, etc.)
        dice -> list of face-up dice numbers
        total -> actual total.
        kept -> kept dice (if adv = "a" or "d", not the same as dice)
    '''

    def __init__(self, dicecode="3d6", adv='', image=False, fig=None, ax=None):
        '''
        Initialize the dice.
        '''
        self.dicecode = dicecode
        self.adv = adv.lower()
        self.dicesides = self.dice_translator(dicecode, adv)
        self.dice = self.roll_all(self.dicesides)
        self.dice_held = self.dice[:]
        self.total = self.get_total(adv)
        self.L = 0
        self.M = 0
        self.H = 0
        self.LM = 0
        self.LH = 0
        self.MH = 0
        self.LMH = 0
        self.get_stats(adv)
        if fig is None:
            self.fig, self.ax = plt.subplots(1, figsize=(4, 3))
        else:
            self.fig = fig
            self.ax = ax

    def __repr__(self):
        '''
        type Roll_name to see the results...
        '''
        a = ""
        if self.adv == 'a':
            a = " [Advantage]"
        elif self.adv == 'd':
            a = " [Disadvantage]"

        return ('{}{} -> {} = {}\n'.format(self.dicecode, a,
                                           self.dice, self.total) +
                'L:{}, M:{}, H:{}, LM:{}, LH:{}, MH:{}, LMH:{}'
                .format(self.L, self.M, self.H, self.LM, self.LH,
                        self.MH, self.LMH))

    def __getitem__(self, key):
        '''
        Gives a dice-value when called when called
        '''
        return self.dice[key]

    def __setitem__(self, key, value):
        '''
        Allows manual reset of dice values
        if higher than "sides", sets as if rolled max enough times to get there
        (as in, dice is less than dicesides)
        '''
        self.dice_held[key] = value
        while value > self.dicesides[key]:
            value -= self.dicesides[key]
        self.dice[key] = value

    def dice_translator(self, dicecode, adv=''):
        '''
        input: string containing numbers, the letter "d", and +/- signs
        output: list

        Turns standard rpg table-top dice codes into a list of lists
        examples:
            3d6 -> [[3, 6]]
            2d6+1d4 -> [[2, 6], [1, 4]]
            2d6+1 -> [[2,6], 1]
        '''
        lst = [a.split("d") for a in
               dicecode.replace(" ", "").replace("-", "+-").split("+")]
        ret = []
        for a in lst:
            for b in range(int(a[0])):
                ret.append(a[1])
        if adv != '':
            ret.append(ret[2])
        return ret

    def roll_all(self, lst):
        '''
        returns a list of dice values.
        '''
        return [rnd.randint(1, int(a)) for a in lst]

    def get_total(self, adv):
        '''
        Gets the Total based on dice_held and adv
        -=called by get_stats, so no need to call this=-
        '''
        total = sum(self.dice_held[:])
        if adv == 'a':
            total = total - min(self.dice_held)
        if adv == 'd':
            total = total - max(self.dice_held)
        return total

    def get_stats(self, adv):
        '''
        set all the L, M, etc. based on self.dice
        '''
        temp = self.dice[:]
        if adv == 'a':
            temp.remove(self.dice[self.dice_held.index(min(self.dice_held))])
        elif adv == 'd':
            temp.remove(self.dice[self.dice_held.index(max(self.dice_held))])
        # now temp is three numbers...
        self.L = min(temp)
        self.H = max(temp)
        self.M = sum(temp)-self.L-self.H
        self.LM = self.L+self.M
        self.LH = self.L+self.H
        self.MH = self.M+self.H
        self.LMH = self.MH + self.L
        self.total = self.get_total(adv)

    def reroll(self, n):
        '''
        rerolls the dice at position n, replacing the values in dice and
        diceheld
        '''
        self.dice[n] = rnd.randint(1, int(self.dicesides[n]))
        self.dice_held[n] = self.dice[n]
        self.get_stats(self.adv)

    def explode(self, n):
        '''
        explodes the dice at location n
        changes dice but NOT dice_held, allowing exploded value for total
        '''
        if int(self.dice[n]) == int(self.dicesides[n]):
            self.dice[n] = rnd.randint(1, int(self.dicesides[n]))
            self.dice_held[n] = self.dice_held[n] + self.dice[n]
            self.get_stats(self.adv)
        else:
            print(self.dice[n])
            print(self.dicesides[n])

    def show(self, title=''):
        '''
        Plots a roll in Matplotlib...
        '''
        fig = self.fig
        ax = self.ax
        fig_loc_x = []
        fig_loc_y = []

        for i, die in enumerate(self.dice):
            im = image.imread('../images/dice/d' + str(self.dicesides[i]) +
                              '_' + str(self.dice[i]) + '.png')
            angle = 0
            if int(self.dicesides[i]) >= 5:
                angle =  rnd.randint(0, 7)
                imr = rotate(im, angle * 45.0)
            else:
                imr = im
            y = rnd.randint(1, 2) * 0.15 + 0.1
            x = i * 0.25 + 0.1 * (i + 1)
            add = 0.25
            if angle % 2 != 0:
                add = 0.25 * (2**0.5)
            if int(self.dicesides[i]) == 6:
                add = add*0.8
            extent = (x, x + add, y, y + add)
            fig_loc_x.append((extent[0], extent[1]))
            fig_loc_y.append((extent[2], extent[3]))
            implot = plt.imshow(imr, aspect='equal', extent=extent)
        xl = 1.4
        yl = 0.9
        def onclick(event):
            for i in range(len(self.dice)):
                if (event.xdata >= fig_loc_x[i][0] - 0.05 and
                    event.xdata <= fig_loc_x[i][1] + 0.05 and
                    event.ydata >= fig_loc_y[i][0] - 0.05 and
                    event.ydata <= fig_loc_y[i][1] + 0.05):
                   # we have a dice click event....
                   if int(self.dice[i]) == int(self.dicesides[i]):
                       ax.cla()
                       # plt.close()
                       self.explode(i)
                       self.show(title)
                   else:
                       ax.cla()
                       # plt.close()
                       self.reroll(i)
                       self.show(title)
                elif (event.xdata >= xl - 0.05 and
                      event.ydata >= yl - 0.05):
                    plt.close()
        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        ax.set_xlim(0, 1.6)
        ax.set_ylim(0, 0.95)
        ax.axis('off')
        s = self.__repr__()
        ax.text(0.05, 0.05, s)
        scatter = plt.scatter(xl - 0.025, yl - 0.025, marker='s',
                              alpha=0.5, color='r')
        ax.scatter(xl - 0.025, yl - 0.025, marker='x',
                        alpha=0.75, color='w')
        ax.format_coord = lambda x, y: ''
        ax.set_title(title)
        plt.draw()


if __name__ == "__main__":
    dice = "3d6"
    adv = ""
    if len(sys.argv) > 1:
        dice = sys.argv[1]
    if len(sys.argv) > 2:
        adv = sys.argv[2]
    a_roll = Roll(dice, adv)
    a_roll.show()
    plt.show()
