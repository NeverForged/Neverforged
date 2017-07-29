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


    def __repr__(self):
        '''
        output the wounds...in a print function
        '''
        lst = ['    dead',
               'critical',
               ' serious',
               'moderate',
               '   light',
               '   minor',
               '        ']
        #       print 'moderate - '
        ret = ''
        for i in xrange(6):
            if self.wounds[i] > 0:
                ret = ret + lst[i]
            else:
                ret = ret + lst[6]
            if self.stun[i] > 0:
                ret = ret + '[stun]'
            else:
                ret = ret + '      '
            if len(self.injuries[i]) > 1:
                ret = ret + " - " + self.injuries[i]
            ret = ret + "\n"
        return ret


    def __add__(self, new):
        '''
        This adds a 'new' wound to the existing wound 'self'
        NOT for use in healing (__sub__ covers healing).

        recomended that new wound object be a single value of
        wound.

        Rules:
            lethal replaces and adds up lethal
            stun adds up with lethal
            lethal adds up and replaces stun
        '''
        temp_wounds = [0, 0, 0, 0, 0, 0]
        new_wounds = [0, 0, 0, 0, 0, 0]
        temp_injuries = ['', '', '', '', '', '']
        temp_stun = [0, 0, 0, 0, 0, 0]
        new_injuries = ['', '', '', '', '', '']
        new_stun = [0, 0, 0, 0, 0, 0]
        stun = 0
        # all but lethal...
        # initialize temp_wounds
        for i in xrange(6):
            temp_wounds[i] = self.wounds[i]
            temp_injuries[i] = self.injuries[i]
            temp_stun[i] = self.stun[i]
            new_wounds[i] = new.wounds[i]
            new_injuries[i] = new.injuries[i]
            new_stun[i] = new.stun[i]

        for i in xrange(5, -1, -1):
            # print i
            #is there damage here...
            if new_wounds[i] >= 1:
                # we have damage...
                if temp_wounds[i] == 0: #lands here
                    temp_wounds[i] = 1
                    temp_stun[i] = new_stun[i] + stun
                    if ((len(new_injuries[i]) > 2) and
                        (new_injuries[i] not in temp_injuries[i]) and
                        (len(temp_injuries[i]) > 1)):
                        temp_injuries[i] = (temp_injuries[i] + ", " +
                                            new_injuries[i])
                    else:
                        temp_injuries[i] = new_injuries[i]
                else:  # already wounded there...
                    if i > 0:
                        new_wounds[i-1] = 1
                        new_injuries[i-1] = new_injuries[i]
                        new_injuries[i] = ''
                    if new_stun[i] + stun > 0:
                        stun = 1
                    # lethal or stun replacing stun...
                    if (stun == 0) or (temp_stun[i] == 1):
                        # lethal... take it up
                        temp_wounds[i] = 0
                        temp_stun[i] = 0

        return Wound(temp_wounds,
                     temp_injuries,
                     temp_stun)


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
        self_stun = [0, 0, 0, 0, 0, 0]
        for i in xrange(1, 6, 1):
            if (i < level) and (reinjure == 1):
                # weirdness with same or worse injuries
                if self_wounds[i] == 1:
                    print("runs for ", i)
                    # injury higher than healing level...
                    self_wounds[i] = 0
                    for j in xrange(level, i, -1):
                        print(i, j)
                        if self_wounds[j] == 0:
                            self_wounds[j] = 1
                        else:
                            self_wounds[j-1] = 1
                            self_wounds[j] = 0
                        print(self_wounds)
                    reinjure = 0 # only do this crap once...
                    print(reinjure)
            if (i >= level) and (reinjure == 1):
                # heal all below healing level
                self_wounds[i] = 0
                self_injuries[i] = ''

        # check injuries...
        injury_clear = 1
        for i in xrange(6):
            if (injury_clear == 1) and (self_wounds[i] == 0):
                self_injuries[i] = ''
            elif self_wounds[i] == 1:
                # we have or highest left-over wound...
                injury_clear = 0

        return Wound(self_wounds, self_injuries, self_stun)


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
        wound = [0, 0, 0, 0, 0, 0]
        injury = ['', '', '', '', '', '']
        stun = [0, 0, 0, 0, 0, 0]
        temp = ''
        actual = 0
        side = 'right'
        dis = 'Disadvantage'
        if location % 2 == 0:
            side = 'left'
        #  wound level...
        done = 0
        if dmg >= fortitude:
            wound[1] = 1
            actual = 1
            done = 1
        elif dmg >= fortitude/2:
            wound[2] = 1
            actual = 2
            done = 1
        elif dmg >= fortitude/4:
            wound[3] = 1
            actual = 3
            done = 1
        elif dmg >= fortitude/8:
            wound[4] = 1
            actual = 4
            done = 1
        elif dmg >= fortitude/16:
            wound[5] = 1
            actual = 5
            done = 1
        # if less than lowest number, or less than 0, minor stun
        if (done == 0) and (dmg < fortitude/16):
                nonlethal = True
                wound[5] = 1
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
        return Wound(wound, injury, stun)
