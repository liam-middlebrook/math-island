from __future__ import print_function
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
EMPTYMAP = r"""
#Title Welcome to Math Island
#Start 0 0
#End 0 0
#Fuel 1

..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
""".split("\n")

Coord = namedtuple('Coord', ['x', 'y'])

obstacles = [path.join(OBSHOME, x) for x in os.listdir(OBSHOME)]

def safeloadlines(fn):
    with open(fn) as f:
        return f.readlines()

def bound(low, val, hi):
    return max(low, min(val, hi))

class Tile(object):
    def __init__(self, char, name, image, frac):
        self.char = char
        self.name = name
        self.image = path.join(TILEHOME,image)
        self.passable = True
        self.cost = Frac(frac)

class BlockingTile(object):
    def __init__(self, fn=None):
        self.image = fn or random.choice(obstacles)
        self.passable = False
        self.char = '.'

class WaterTile(BlockingTile):
    def __init__(self):
        BlockingTile.__init__(self, WATERTILE)
        self.char = 'w'

class Tiles(object):
    def __init__(self):
        assert path.exists(TILESETTINGS), "Could not load tiles"
        self.tilemap = {}
        with open(TILESETTINGS) as tiledata:
            for line in tiledata:
                sym, name, image, frac = line.split("\t")
                self.tilemap[sym] = Tile(sym, name, image, frac)
    def __getitem__(self, index):
        if index == '.': return BlockingTile()
        elif index == 'w': return WaterTile()
        else: return self.tilemap[index]
    def __iter__(self):
        return self.tilemap.__iter__()
Tiles = Tiles()

class Level(object):
    def __init__(self, lvsource=None):
        self.loads(safeloadlines(lvsource) if lvsource else EMPTYMAP)

    def loads(self, data):
        take = lambda prefix: (line.replace(prefix, "", 1).strip()
                               for line in data if line.startswith(prefix))
        take1 = lambda prefix: next(take(prefix))
        # I know that this isn't perfect, but it's the most convenient way to do it
        try: self.title = take1("#Title")
        except StopIteration: self.title = "Escape from Math Island!"
        self.text  = "\n".join(take("#Text"))
        self.start = Coord(*map(int, take1("#Start").split()))
        self.end   = Coord(*map(int, take1("#End").split()))
        self.startfuel = Frac(take1("#Fuel"))
        self._map = [[Tiles[c] for c in line.replace(" ","").strip()]
                     for line in data if line.strip() and not line.startswith("#")]
        self.height = len(self._map)
        self.width = len(self._map[0])
        self.fuel = {Coord(int(x), int(y)): Frac(f)
                     for x, y, f in [
                         line.split() for line in take("#Refuel")]}

    def __getitem__(self, indices):
        assert len(indices) == 2, "Invalid level lookup"
        return self._map[indices[1]][indices[0]]

    def __setitem__(self, indices, newtile):
        assert len(indices) == 2, "Invalid level lookup"
        self._map[indices[1]][indices[0]] = newtile
        return newtile

    def getcost(self, x, y):
        return bound(-1, self.fuel.pop(Coord(x,y),0) - self[x,y].cost, 1)

    def clean(self):
        self.fuel = {c:f for c,f in self.fuel.items() if f}

    def __repr__(self):
        self.clean()
        ret = []
        ret.append("#Title " + self.title)
        if self.text:
            ret.extend(("#Text "+s) for s in self.text.split("\n"))
        ret.append("#Start {0.x} {0.y}".format(self.start))
        ret.append("#End {0.x} {0.y}".format(self.end))
        ret.append("#Fuel "+str(self.startfuel))
        ret.extend("#Refuel {0.x} {0.y} {1}".format(c, t) for c,t in self.fuel.items())
        ret.extend(" ".join(t.char for t in row) for row in self._map)
        return "\n".join(ret)


if __name__ == '__main__':
    #lv = Level(path.join(LEVELHOME, "003.ilv"))
    lv = Level()
    print(lv)
