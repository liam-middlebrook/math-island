#!/usr/bin/env python

import sys
import os
import argparse
from fractions import Fraction as Frac
try:
    # Python 3
    from tkinter import *
    from tkinter import filedialog
except ImportError:
    # Python 2
    from Tkinter import *
    import tkFileDialog as filedialog

from level import Level, Coord

class FuelChangeState(object):
    def __init__(self, f):
        self.fuel = Frac(f)
    def __call__(self, lvl, x, y):
        lvl.fuel[Coord(x,y)] = self.fuel

# Gui for inputting variables
class Editor(Frame):

    def __init__(self, master):
        '''
        Creates all of the buttons and boxes for the GUI based on the rules provided
        '''
        # Get the root window
        self.master = master
        self.mapframe = None
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
        self.titlebar = Entry(header)
        self.titlebar.pack()
        Button(header, text="Save", command=self.save).pack()
        Button(header, text="Load", command=self.load).pack()
        Button(header, text="Quit", command=self.master.destroy).pack()

        fuelframe = Frame(self.master)
        fuelframe.pack(side=BOTTOM)
        for i in range(9):
            f = Frac(i, 8)
            btn = Button(fuelframe, text=str(f),
                         command=lambda f=f: self.setstate(FuelChangeState(f)))
            btn.grid(row=0, column=i)

        self.build()

    def build(self):

        # Clean up if we're rebuilding
        if self.mapframe:
            self.mapframe.destroy()

        self.mapframe = Frame(self.master)
        self.mapframe.pack(side=LEFT)
        self.btns = [[None for i in range(self.level.width)]
                           for j in range(self.level.height)]
        for y in range(self.level.height):
            for x in range(self.level.width):
                btn = Button(self.mapframe, text=self.level[x, y].char,
                             command=lambda x=x, y=y: self.apply(x, y))
                btn.grid(row=y, column=x)
                self.btns[x][y] = btn

    def reset(self):
        self.level = Level()
        self.build()

    def setstate(self, state):
        self.state = state

    def apply(self, x, y):
        if self.state:
            self.state(self.level, x, y)

    def save(self):
        fn = filedialog.asksaveasfilename(**self.file_opt)
        if not fn: return
        with open(fn, "w") as fi:
            fi.write(repr(self.level))

    def load(self):
        fn = filedialog.askopenfilename(**self.file_opt)
        if fn:
            self.level = Level(fn)
        self.build()

def main():
    root = Tk()
    root.title('Math Island Level Editor')
    app = Editor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
