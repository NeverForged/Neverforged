![Neverforged Roleplaying Game](images/neverforged_logo.png)

Neverforged is a table top role playing game I've been developing in my spare time for the last few years.

## Dice.py
The Dice class is a dice roller for the game I'm writing.  The reason I'm sharing it is that it creates a dice rolling space in MatPlotLib with clickable explodes/rerolls.  The actual method is tied into the game I'm writing; however the work I did getting the image to show and reroll I don't mind sharing.  If there is demand for it, I could make a general dice roller out of it.

![Image of Dice App](/images/Figure_1.png)

The [dice images](https://github.com/NeverForged/Neverforged/tree/master/images/dice) are images that were made a while ago for another App.  Clicking on one launches the reroll or explode code for the dice.  The "x" in the corner is a pair of scatter plots.  Click spaces were set using a for loop in an *onClick* event, using the areas assigned to the dice as the clickable spaces to operate code.  The "x" was assigned to close the plot, do it's business, and reopen it.  With more work one could save the locations of the dice and only change the location of the rerolled element.  I may do this for future versions.
