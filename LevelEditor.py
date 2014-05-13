#!/usr/bin/env python

import sys
import os
import argparse
import itertools
from fractions import Fraction as Frac
try:
    # Python 3
    from tkinter import *
    from tkinter import filedialog
except ImportError:
    # Python 2
    from Tkinter import *
    import tkFileDialog as filedialog

from level import Level, Coord, Tiles

class FuelChangeState(object):
    def __init__(self, f):
        self.fuel = Frac(f)
    def __call__(self, lvl, x, y):
        lvl.fuel[Coord(x,y)] = self.fuel

class TileChangeState(object):
    def __init__(self, c):
        self.tile = Tiles[c]
    def __call__(self, lvl, x, y):
        lvl[x,y] = self.tile

# Gui for inputting variables
class Editor(Frame):

    def __init__(self, master):
        '''
        Creates all of the buttons and boxes for the GUI based on the rules provided
        '''
        # Get the root window
        self.master = master
        self.level = Level()
        self.state = None

        self.file_opt = options = {
                'defaultextension': '.ilv',
                'filetypes': [('Math Island Level', '.ilv')],
                'parent': self.master,
                'title': 'Math Island Level',
        }

        self.master.bind("<Escape>", lambda e:self.master.destroy())

        header = Frame(self.master)
        header.pack(side=TOP)
        Button(header, text="Save", command=self.save).pack(side=LEFT)
        Button(header, text="Load", command=self.load).pack(side=LEFT)
        Button(header, text="Quit", command=self.master.destroy).pack(side=LEFT)

        infoframe = Frame(self.master)
        infoframe.pack(side=TOP)
        Label(infoframe, text="Title: ").pack(side=TOP)
        self.title = StringVar()
        Entry(infoframe, textvariable=self.title).pack()
        Label(infoframe, text="Text: ").pack(side=TOP)
        self.text = Text(infoframe, width=60, height=4)
        self.text.pack()

        fuelframe = Frame(self.master)
        fuelframe.pack(side=BOTTOM)
        for i in range(9):
            f = Frac(i, 8)
            btn = Button(fuelframe, text=str(f),
                         command=lambda f=f: self.setstate(FuelChangeState(f)))
            btn.grid(row=0, column=i)

        tileframe = Frame(self.master)
        tileframe.pack(side=RIGHT)
        getcost = lambda t: getattr(Tiles[t], "cost", None)
        tiles = sorted(Tiles, key=getcost)
        for i, c in enumerate(itertools.chain(('.','w'), tiles)):
            btn = Button(tileframe,
                         text="{0}: {1}".format(c, getcost(c)),
                         command=lambda c=c: self.setstate(TileChangeState(c)))
            btn.grid(column=(i//10), row=(i%10), sticky=N+E+S+W)

        mapframe = Frame(self.master)
        mapframe.pack(side=LEFT)
        self.btns = [[None for i in range(self.level.width)]
                           for j in range(self.level.height)]
        for y in range(self.level.height):
            for x in range(self.level.width):
                self.btns[x][y] = btn = Button(
                        mapframe, text=self.level[x, y].char,
                        command=lambda x=x, y=y: self.apply(x, y))
                btn.grid(row=y, column=x, sticky=N+E+S+W)

        self.redraw()

        '''
        TODO: START/END/STARTFUEL BUTTONS
        '''

    def redraw(self):

        for y in range(self.level.height):
            for x in range(self.level.width):
                self.btns[x][y].config(text=self.level[x,y].char)
    def reset(self):
        self.level = Level()
        self.build()

    def setstate(self, state):
        self.state = state

    def apply(self, x, y):
        if self.state:
            self.state(self.level, x, y)
            self.redraw()

    def save(self):
        self.level.title = self.title.get().strip()
        self.level.text = self.text.get(1.0, END).strip()
        fn = filedialog.asksaveasfilename(**self.file_opt)
        if not fn: return
        with open(fn, "w") as fi:
            fi.write(repr(self.level))

    def load(self):
        fn = filedialog.askopenfilename(**self.file_opt)
        if fn:
            self.level = Level(fn)
        self.title.set(self.level.title)
        self.text.delete(1.0, END)
        self.text.insert(1.0, self.level.text)
        self.redraw()

def main():
    root = Tk()
    root.title('Math Island Level Editor')
    app = Editor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
