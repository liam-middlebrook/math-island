#!/usr/bin/env python

import sys
import os
import argparse
try:
    # Python 3
    from tkinter import *
    from tkinter import filedialog
except ImportError:
    # Python 2
    from Tkinter import *
    import tkFileDialog as filedialog

from level import Level

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

        self.build()

    def build(self):

        # Clean up if we're rebuilding
        # self.InputPane.destroy()

        # The left pane, detailing the inputs
        self.InputPane = Frame(self.master)
        self.InputPane.pack(side='left')
        self.rules = []

        self.mapframe = Entry(self.master)
        self.mapframe.pack(side='left')
        self.btns = [[None for i in range(self.level.width)]
                           for j in range(self.level.height)]
        for y in range(self.level.height):
            for x in range(self.level.width):
                btn = Button(self.mapframe, text=".",
                             command=lambda x=x, y=y: self.apply(x, y))
                btn.grid(row=y, column=x)
                self.btns[x][y] = btn

        # Assorted deductions
        '''
        # Buttons
        ButtonFrame = Frame(self.InputPane)
        ButtonFrame.grid(row=row, column=0)
        # Reload the rules
        self.Reloader = Button(ButtonFrame, text='Reload', command=self.reload)
        self.Reloader.grid(row=0, column=0, sticky=N + S + E + W)
        # Reset the scores
        self.Resetter = Button(ButtonFrame, text='Reset', command=self.reset)
        self.Resetter.grid(row=0, column=1, sticky=N + S + E + W)

        # This one will change to show the final grade
        # Do the actual recalculation
        self.GradeButton = Button(
            self.InputPane, text='Result: ', command=self.recalculate)
        self.GradeButton.grid(row=row, column=1, sticky=N + S + E + W)

        # Print out the errors
        scrollbar = Scrollbar(self.ErrorText)
        scrollbar.pack(side='right', fill=Y)
        # The +2 is for the "penalty" box set and the result pane
        self.ErrorText = Text(self.master, width=80, height=(len(rules) + 2))
        self.ErrorText.pack(side='right', fill=BOTH)
        self.ErrorText.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.ErrorText.yview)
        '''

    def reset(self):
        '''
        Clears all output and resets scores to maximum
        '''
        self.level = Level()

    def apply(self, x, y):
        if self.state:
            self.state(self.level, x, y)


def main():
    root = Tk()
    root.title('Math Island Level Editor')
    app = Editor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
