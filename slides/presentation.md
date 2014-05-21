# Math Island

- Derek Gonyeo (dgonyeo@csh.rit.edu)
- Liam Middlebrook (liammiddlebrook@gmail.com)
- Matt Soucy (msoucy@csh.rit.edu)
- Dylan Ayrey

---

# What is it?

Math Island is an open source game designed for 4th graders to learn fractions

- Provides many levels of challenge
- MIT licensed
- Started from scratch
- Mixed open source and home grown art
- Easy level editor

---

# How is it played?

- Robot wanders the island looking for a way home
- When the robot moves, it uses fuel
- Robot dies if fuel is depleted
- Fuel is scattered throughout the island

---

# DEMO

---

# How does the code work?

- On startup, level001.ilv is loaded in with Soucy's Level class
- Image objects for the different tiles in the map are made at this time
- The engine draws the background, the tiles it just loaded in, and the current fuel level
- Liam's Player class is used to draw the player, and react to key presses
- When the player reaches the end tile, it starts this process over with level002.ilv, and so on

---

# Best pieces of software

- The Level class is short and effective, and also comes with a super useful level editor
- The Player class is easy to use and works well

---

# Example of a level file:

    #Title Running low on fuel
    #Start 2 5
    #End 6 2
    #Fuel 1/4
    #Refuel 4 3 1/1 
    #Refuel 4 7 7/8
    ..........
    ..........
    ......g...
    ..ggg.g...
    ..g.g.g...
    ..ggg.g...
    ..g...g...
    ..ggggg...
    ..........
    ..........

---

# Worst Pieces of software

- Initially there was x-y confusion when the engine loaded in the levels (it's since been fixed)
- Level editor output could be beautified

---

# Stumbling blocks

- Different parts of the system were developed in parallel, so sometimes there was a failure to communicate design ideas
- There was some discussion about our Row-major order. Though fairly arbitrary it was confusing for some.


---

# Successes

- Having a level editor makes it easier for the community to contribute new levels
- Despite starting from scratch, we have a playable game with only one known bug (crashes at the end)

---

# Doing things differently

- Would have been better to meet up more frequently/make sure that all members were up to date on the status of all of the components
- Frequent tests on the XO
- Leadership/meetings make sure everyone is up to date


---

# In the future

- Level validation
	- There's no guarantee that levels are actually solvable at the moment
- Random level selection
	- Students would get bored playing the exact same levels in the exact same order every time
- General polish
	- Cleaner UI
	- Better explanations about things like tiles
- Better integration between components
	- levels.py declares some utilities that MathIsland.py could find useful
- Art needs polishing
- Replace existing open source art with home grown

---

# Questions?
