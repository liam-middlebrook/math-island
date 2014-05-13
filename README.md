math-island
===========

A python game for the OLPC that teaches basic operations

##Running Math Island on the OLPC XO

###In the Sugar Desktop Enviornment
1. Open the Terminal Activity
2. Clone this repository `git clone https://github.com/liam-middlebrook/math-island`
3. Move into the math-island directory `cd math-island`
4. Run MathIsland.py `./MathIsland.py`

###In the Gnome Desktop Enviornment
1. Open your terminal of choice
2. Clone this repository `git clone https://github.com/liam-middlebrook/math-island`
3. Move into the math-island directory `cd math-island`
4. Run MathIsland.py `./MathIsland.py`

##Installing Math Island Into Sugar Activities
1. Open your terminal of choice
2. Clone this repository `git clone https://github.com/liam-middlebrook/math-island`
3. Move into the math-island directory `cd math-island`
4. Run setup.py to generate the pot files `python setup.py genpot`
5. Run setup.py to build the activity `python setup.py build`
6. Run setup.py to link your development directory `python setup.py dev`
7. Run setup.py to distribute the activity onto your XO `python setup.py dist_xo`
