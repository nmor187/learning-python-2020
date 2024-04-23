#10-28-20/10-31-20
print("Ayo gang gang")
x = 3
y = 4
z = x + y
def ifs():
	if x > 3:
		print("x is greater than 3")
	elif x < 3:
		print("x is less than 3")
	else:
		print("pranked")
def ifs2():
	if y == 4:
		print("y is 4")
	else:
		print("y isn't 4")
print("ayo gang gang")
def printers():
	words = "Bro-ski"
	print("Cool")
	print("Stuff")
	print(words)
input = None
def user_input():
	input = raw_input("What is your favorite color?")
	input_new = input.lower()
	colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink', 'purple', 'brown', 'white', 'black']
	if input_new in colors:
		print("Your favorite color is " + str(input_new) + "!")
	else:
		print("The color you entered is not a real color!")
user_input()