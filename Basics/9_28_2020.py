import cmath
import sys
a = 1
b = 3
c = 3
d = float(input("Enter your value: "))
answer = a * b * c * d
print(answer)
#
#
#
bool = True
if bool == True:
	print("test")
else:
	print(answer)

if b >= 4:
	bool = True
elif b == 3:
	bool = True
else:
	bool = input("Password: ")
if bool == 5:
	print("Password is correct")
else:
	print("Password is incorrect")
print(bool)
#
#
#
import math
m = cmath.sqrt(c)
print(m)
n = math.sqrt(c)
print(n)
#
#
#
import os
x = os.getlogin()
y = (x[0:6])
first_name = y
print(first_name)
z = (x[6:12])
last_name = z
print(last_name)
print("This is a really long sentence about " + last_name + ", " + first_name)


