import random as rnd
import sys


class Wound(object):
    '''
    Wounds sytem in Neverforged.
    5 levels: minor, light, moderate, serious, critical.

    Come in lethal and nonlethal (daze).

    - When damage is taken, it occupies it's own spot.
    - if spot occupied, they combine and become a wound of a step higher
    - repeat until slot is unoccupied
    - if critical tries to move up, creature is knocked out (daze) or dead.
    - daze damage does not move real damage, but still steps up as per normal.

    - healing heals all daze damage
    - healing has an associated level with it
    - healing removes a wound of that level.
    - if the space is empty, it reduces the next highest wound, and fills down
      until the wound spot occupied by the style taken is filled
    - if healing > all wounds taken, they are eliminated

    - injuries are kept with wounds
    -  when all boxes above or with an injury are cleared, the injury is

        PARAMETERS/ATTRIBUTES
        wounds: A list of int/boul objects that determine if the wound
                represents dead, critical, serious, moderate, light, minor
        injuries: list of string values that return injuries to the creature
        stun: A list of int/boul objects that determine if the wound is a coma,
                critical stun, serious stun, moderate stun, light stun, or
                minor stun

        METHODS
        heal(level): Healing based on an int value: 1 = critical, 2 = serious,
                3 = moderate, 4 = light, 5 = minor.  Healing clears ALL stun
                damage, then reduces the highest damage level, then adds all
                levels above itself to the highest-1 back in.
        make(self, dmg=1, location=0, fortitude=11, nonlethal=False): Create a
                new wound object based on damage, fortitude, and location (i.e.
                last number of the roll).  Sets the wound object.  Make sure any
                dmg reduction due to armor is already calculated before this
                object is created.
    '''

    def __init__(self, lst_wounds=[0, 0, 0, 0, 0, 0],
                 lst_injuries=['', '', '', '', '', ''],
                 lst_stun=[0, 0, 0, 0, 0, 0]):
        '''
        initializer for wounds/injuries.
        0 = dead
        1 = critical wound/stun
        2 = serious wound/stun
        3 = moderate wound/stun
        4 = light wound/stun
        5 = minor wound/stun
        '''
        self.wounds = lst_wounds
        self.injuries = lst_injuries
        self.stun = lst_stun


    # def __repr__(self):
    #     '''
    #     output the wounds...in a print function
    #     '''
    #     lst = ['    dead',
    #            'critical',
    #            ' serious',
    #            'moderate',
    #            '   light',
    #            '   minor',
    #            '        ']
    #     #       print 'moderate - '
    #     ret = ''
    #     for i in range(6):
    #         if self.wounds[i] > 0:
    #             ret = ret + lst[i]
    #         else:
    #             ret = ret + lst[6]
    #         if self.stun[i] > 0:
    #             ret = ret + '[stun]'
    #         else:
    #             ret = ret + '      '
    #         if len(self.injuries[i]) > 1:
    #             ret = ret + " - " + self.injuries[i]
    #         ret = ret + "\n"
    #     return ret


    def __add__(self, new):
        '''
        This adds a 'new' wound to the existing wound 'self'
        NOT for use in healing

        recomended that new wound object be a single
        wound.

        Rules:
            lethal replaces and adds up lethal
            stun adds up with lethal
            lethal adds up and replaces stun
        '''
        wounds = self.wounds
        stun = self.stun
        injuries = self.injuries
        # determine where the new thing is...
        if 1 in new.wounds:  # lethal
            idx = new.wounds.index(1)
            stund = 0
        elif 1 in new.stun:  # nonlethal
            idx = new.stun.index(1)
            stund = 1
        hold = idx
        # print(idx)
        actual = 0
        for i in range(idx, -1, -1):  # don't bother with lesser wounds
            if hold == i:  # have damage to deal with...
                if stund == 0:  # add lethal dmg...
                    if wounds[i] == 1:
                        wounds[i] = 0
                        hold = i - 1
                    elif stun[i] ==  1:
                        stun[i] = 0
                        wounds[i] = 0
                        hold = i - 1
                    else:  # lands here
                        wounds[i] = 1
                        actual = i
                elif stund == 1:  #stun damage
                    if wounds[i] == 1:
                        hold = i - 1
                    elif stun[i] ==  1:
                        stun[i] = 0
                        hold = i - 1
                    else:  # lands here
                        stun[i] = 1
        # injuries...
        if len(injuries[actual]) >= 1:
            injuries[actual] = injuries[actual] + '<br>' + ''.join(new.injuries)
        else:
            injuries[actual] = ''.join(new.injuries)
        # done...
        return Wound(wounds, injuries, stun)

    def heal(self, level):
        '''
        Healing based on an integer value:
        1 = critical
        2 = serious
        3 = moderate
        4 = light
        5 = minor

        Healing clears ALL stun damage, then reduces the highest damage level,
        then adds all levels above itself to the highest-1 back in.
        '''
        reinjure = 1
        wound_level = 0
        temp_wound = Wound()
        self_wounds = self.wounds
        self_injuries = self.injuries
        self_stun = self.stun
        for i in range(1, 6, 1):
            if (i < level) and (reinjure == 1):
                # weirdness with same or worse injuries
                if self_wounds[i] == 1:
                    # print("runs for ", i)
                    # injury higher than healing level...
                    self_wounds[i] = 0
                    for j in range(level, i, -1):
                        # print(i, j)
                        if self_wounds[j] == 0:
                            self_wounds[j] = 1
                        else:
                            self_wounds[j-1] = 1
                            self_wounds[j] = 0
                        # print(self_wounds)
                    reinjure = 0 # only do this once...
                    # print(reinjure)
            if (i >= level) and (reinjure == 1):
                # heal all below healing level
                self_wounds[i] = 0
                self_injuries[i] = ''

        # check injuries...
        injury_clear = 1
        for i in range(6):
            if (injury_clear == 1) and (self_wounds[i] == 0):
                self_injuries[i] = ''
            elif self_wounds[i] == 1:
                # we have or highest left-over wound...
                injury_clear = 0
        self = Wound(self_wounds, self_injuries, self_stun)


    def __getitem__(self, index, injury=False):
        '''
        returns the state of wounds of the box picked
        returns injuries if applicable
        '''
        if injury:
            return (self.wounds[index],
                    self.stun[index],
                    self.injuries[index])
        else:
            return (self.wounds[index],
                    self.stun[index])


    def make(self, dmg=1, location=0, fortitude=11, nonlethal=False):
        '''
        Create a new wound object based on damage, fortitude, and location (i.e.
        last number of the roll).  Sets the wound object.  Make sure any dmg
        reduction due to armor is already calculated before this object created.
        '''
        # print(dmg, location, fortitude)
        wound = [0, 0, 0, 0, 0, 0]
        injury = ['', '', '', '', '', '']
        stun = [0, 0, 0, 0, 0, 0]
        temp = ''
        actual = 0
        side = 'left'
        dis = 'Disadvantage'
        if location >= 1 and location <= 4:
            side = 'right'
        #  wound level...
        done = 0
        if dmg >= fortitude:
            wound[1] = 1
            actual = 1
            done = 1
        elif dmg >= int(fortitude/2):
            wound[2] = 1
            actual = 2
            done = 1
        elif dmg >= int(fortitude/4):
            wound[3] = 1
            actual = 3
            done = 1
        elif dmg >= int(fortitude/8):
            wound[4] = 1
            actual = 4
            done = 1
        elif dmg >= int(fortitude/16):
            wound[5] = 1
            actual = 5
            done = 1
        # if less than lowest number, or less than 0, minor stun
        if (done == 0) and (dmg < fortitude/16):
                nonlethal = True
                wound[5] = 0
                stun[5] = 1
                actual = 5
                done = 1

        # injury time...
        if nonlethal == False:
            # Torso
            if ((location == 0) or (location == 1) or (location == 2)
                                or (location == 5) or (location == 9)):
                # torso shot...
                if actual < 4:
                    injury[actual] = '{} Physical'.format(dis)
                    temp = "Stunned"
            # arms
            if (location == 3) or (location == 8):
                injury[actual] = '{} with {} arm'.format(dis, side)
                if actual < 4:
                    temp = 'Drop item in {} hand'.format(side)
            # legs
            if (location == 4) or (location == 7):
                mtype = 'Offturn'
                if actual < 3:
                    mtype = 'Offturn and Onturn'
                if actual < 4:
                    temp = 'Prone'
                injury[actual] = '{} Move reduced by 1'.format(mtype)
            # head
            if (location == 6):
                temp = "Stunned"
                injury[actual] = '{} Mental'.format(dis)
        else:
            stun[actual] = 1
            wound[actual] = 0
        return Wound(wound, injury, stun)
