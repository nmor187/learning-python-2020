#importing tkinter which we will use the frame class from tkinter modecule (import/from)
from tkinter import *
#creating the window frame
class Window(Frame):
	#initializing the window
	def __init__(self):
		Frame.__init__(self, master)
	#master or main frame
	self.master = master
root = Tk
#creating instance
app = Window(root)
#Showing the instance and beginning loop
root.mainloop()
#Creating a window with tkinter
#DOESNT WORK
#https://pythonprogramming.net/python-3-tkinter-basics-tutorial/