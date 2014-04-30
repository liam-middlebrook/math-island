import os
import os.path as path
import random
from fractions import Fraction as Frac
from collections import namedtuple

CONTENTHOME = 'content'
LEVELHOME = path.join(CONTENTHOME, "levels")
TILESETTINGS = path.join(LEVELHOME, "tiles")
TILEHOME = path.join(CONTENTHOME, "tiles")
OBSHOME = path.join(CONTENTHOME, "obstacles")
WATERTILE = path.join(OBSHOME, "water.png")

Coord = namedtuple('Coord', ['x', 'y'])

obstacles = [path.join(OBSHOME, x) for x in os.listdir(OBSHOME)]

def safeloadlines(fn):
    with open(fn) as f:
        return f.readlines()

class Tile(object):
    def __init__(self, name, image, frac):
        self.name = name
        self.image = image
        self.passable = True
        self.cost = Frac(frac)

class BlockingTile(object):
    def __init__(self, fn=None):
        self.image = fn or random.choice(obstacles)
        self.passable = False

class WaterTile(BlockingTile):
    def __init__(self):
        BlockingTile.__init__(self, WATERTILE)

class Tiles(object):
    def __init__(self):
        assert path.exists(TILESETTINGS), "Could not load tiles"
        self.tilemap = {}
        with open(TILESETTINGS) as tiledata:
            for line in tiledata:
                sym, name, image, frac = line.split("\t")
                self.tilemap[sym] = Tile(name, image, frac)
        self.tilemap['w'] = WaterTile()
    def __getitem__(self, index):
        if index == '.': return BlockingTile()
        return self.tilemap[index]
Tiles = Tiles()

class Level(object):
    def __init__(self, lvsource):
        data = safeloadlines(lvsource)
        take = lambda prefix: (line.replace(prefix, "", 1).strip()
                               for line in data if line.startswith(prefix))
        take1 = lambda prefix: next(take(prefix))
        self.title = take1("#Title")
        self.text  = "\n".join(take("#Text"))
        self.start = Coord(*map(int, take1("#Start").split()))
        self.end   = Coord(*map(int, take1("#End").split()))
        self.startfuel = Frac(take1("#Fuel"))
        self._map = [[Tiles[c] for c in line.replace(" ","").strip()]
                     for line in data if line.strip() and not line.startswith("#")]
        self.height = len(self._map)
        self.width = len(self._map[0])
    def __getitem__(self, indices):
        assert len(indices) == 2, "Invalid level lookup"
        return self._map[indices[0]][indices[1]]

if __name__ == '__main__':
    lv = Level(path.join(LEVELHOME, "001.ilv"))
    print "TITLE:", lv.title
    print "TEXT:\n",lv.text
    for i in range(lv.width):
        for j in range(lv.height):
            print lv[i,j]
