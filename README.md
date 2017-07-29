![Neverforged Roleplaying Game](images/neverforged_logo.png)

**Neverforged** is a table top role playing game I've been developing in my spare time for the last few years.  After graduating from [Galvanize](https://www.galvanize.com/seattle/data-science), I decided to write it up in Python 3 to keep up my coding skills as I job hunt.  Shameless self-plug [here](https://www.linkedin.com/in/darinlasota/).

The game itself is an attempt to integrate Narrative and Tactical combat styles into a single game, allowing players to act on all turns, with turn ownership being about Narrative control.

At present, the *"Fluff"* of the game is based on a reimagined Earth where deserts are smaller, allowing resources to travel more easily, placing cultures at roughly the same technological level.  A planet where *Dong Gua* (Read: China) conquered *The Great Republic* (Read: Rome) around the time of the switch from *Republic* to *Empire*, thus creating a more integrated East-West (and allowing a combination of *Medieval Fantasy* and *Wu Xia*, as well as a use of *Dong Hua* as a language of education and religion).  The specific area of focus at the moment, given the ease of understanding due to *[other roleplaying games](http://dnd.wizards.com/)*, is the equivalent of Medieval England about to suffer the *Restless Death*, a bubonic-plague where, upon death, the infected rise as zombies to infect the living.

>A Plague is sweeping through the continent, killing thousands, replacing them with mindless undead that seek to infect and consume the living.  An ancient order, fallen into disrepair, is recalled by the Church; prisoners are being sentenced to the order, and others are volunteering, fearing that the Plague may reach the shores of the Raven Isle.  The order hopes to reestablish their old castles, hopefully before the Plague reaches Corvish Shores.
Can the Plague be stopped?  Can anyone survive it?  Will the Plague Hunters keep the people safe, or just add to the Army of Pestilence that seeks to devour all of humanity?

## Dice.py
At the moment, this shows that a dice roller with rerolls is possible using MatPlotLib.

![Image of Dice App](/images/Figure_1.png)

The [dice images](https://github.com/NeverForged/Neverforged/tree/master/images/dice) are images that were made a while ago for another App.  Clicking on one launches the reroll or explode code for the dice.  The "x" in the corner is a pair of scatter plots.  Click spaces were set using a for loop in an *onClick* event, using the areas assigned to the dice as the clickable spaces to operate code.  The "x" was assigned to close the plot, do it's business, and reopen it.  With more work one could save the locations of the dice and only change the location of the rerolled element.  I may do this for future versions.
