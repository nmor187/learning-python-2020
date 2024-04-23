#Basics October 1st 2020
x = 3
y = 4
multiply = x * y
add = x + y
def statement():
	if x > y:
		print(multiply)
	else:
		print(add)
def loops():
	list = [1,2,3,4,5,6,7,8,9,10]
	for i in list:
		print(i)
def structures():
	name = raw_input("What is your name? ")
	names = ("jeff", "jim", )
	if (name.lower()) in names:
		return(True)
	else:
		return(False)
structures()
def true_false():
	global y
	if x == 3:
		print("your name probably begins with a J")
		y = y*3
	else:
		print("Nobody knows you sorry")
true_false()
print(y)
