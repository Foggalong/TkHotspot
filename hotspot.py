#!/usr/bin/python2

# from time import sleep; sleep(5)
																															   
title='Ap-Hotspot'
																															   
# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']

import Tkinter
import Pmw
import os

class Demo:
	def __init__(self, parent):
	# Create and pack the ButtonBox.
		self.buttonBox = Pmw.ButtonBox(parent,
			labelpos = 'nw',
			label_text = 'Would you like to start a hotspot?',
			frame_relief = 'groove')
		self.buttonBox.pack(fill = 'both', expand = 1, padx = 8, pady = 8)	

		# Add some buttons to the ButtonBox.
		self.buttonBox.add('Yes', command = self.yes)
		self.buttonBox.add('No', command = self.no)
		self.buttonBox.add('Help', command = self.help)	

		# Set the default button (the one executed when <Return> is hit).
		self.buttonBox.setdefault('Yes')
		parent.bind('<Return>', self._processReturnKey)
		parent.focus_set()	

		# Make all the buttons the same width.
		self.buttonBox.alignbuttons()	

	def _processReturnKey(self, event):
		self.buttonBox.invoke()

	def yes(self):
		os.system("gksu ap-hotspot start")
		exit()

	def no(self):
		exit()

	def help(self):
		os.system("uzbl-core -u http://www.webupd8.org/2013/06/how-to-set-up-wireless-hotspot-access.html")

######################################################################

# Create demo in root window for testing.
if __name__ == '__main__':
	root = Tkinter.Tk()
	root.attributes("-topmost", 1)
	root.resizable(0,0)
	Pmw.initialise(root)
	root.title(title)
	widget = Demo(root)
	root.mainloop()
