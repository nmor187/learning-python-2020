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
#
#
#
#Simple Calculator
first_number = float(raw_input("Enter first number: "))
operation = raw_input("Enter operation: ")
second_number = float(raw_input("Enter second number: "))
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
if operation == "+":
	print(addition)
elif operation == "-":
	print(subtraction)
elif operation == "*":
	print(multiplication)
elif operation == "/":
	print(division)
else:
	print("An error occurred while performing this operation")
#types of variables
a = 3
b = float(a)
c = int(a)
print(a)
print(b)
print(c)
d = "Floating Integers"
print(d)
e = str("Strings")
print(e)
#user input
user_input = raw_input("What would you like to input? ")
print("Accessing " + user_input)