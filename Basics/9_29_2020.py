a = float(raw_input("Enter first number: "))
b = float(raw_input("Enter second number: "))
c = float(raw_input("Enter third number: "))
a2 = a * a
b2 = b * b
c2 = c * c
if a2 == b2 + c2:
	print("RIGHT TRIANGLE")
else:
	print("NOT RIGHT TRIANGLE")
#
#
#
#imports the datetime library and extensions
from datetime import datetime
hour = datetime.today().hour
even_hours = [2,4,6,8,10,12,14,16,18,20,22,24]
even = "It is currently an even hour!"
odd = "It is currently an odd hour!"
if hour in even_hours:
	print(even)
else:
	print(odd)
#
#
#
#password entrance thing
username_input = str(raw_input("Enter your username: "))
password_input = str(raw_input("Enter your password: "))
username = "admin"
password = "123456"
if username_input == username and password_input == password:
	print("Access Granted")
else:
	print("Error")