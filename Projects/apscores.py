import math
# calculating basic stats from list of numbers
x_values = [89,83,94,87,85,87,80,85,87,80,85,91,90,87,73,62,81,87,90,60,89,64,90,84,70,85,86,77]
x_bar = float(sum(x_values))/float(len(x_values))
y_values = [4,3,5,3,2,4,4,4,4,3,4,3,1,3,5,4,1,4,1,5,3,2,3,4,2]
y_bar = float(sum(y_values))/float(len(y_values))
print(x_bar)
print(y_bar)
s_x = []
for i in x_values:
    s = (i - x_bar)*(i - x_bar)
    s_x.append(s)
s_x = float(sum(s_x))/float(len(x_values)-1)
s_x = math.sqrt(s_x)
s_y = []
for i in y_values:
    s = (i - y_bar)*(i - y_bar)
    s_y.append(s)
s_y = float(sum(s_y))/float(len(y_values)-1)
s_y = math.sqrt(s_y)
print(s_y)
print(s_x)
#calculating r
z_x = []
for i in x_values:
    s = (i - x_bar) / s_x
    z_x.append(s)
z_y = []
for i in y_values:
    s = (i - y_bar) / s_y
    z_y.append(s)
r_sum = []
for i, j in zip(z_x, z_y):
    s = i * j
    r_sum.append(s)
r = sum(r_sum) /((len(x_values))-1)
#Calculating a and b
#x_bar = 82.24
#y_bar = 3.24
#s_x = 9.41
#s_y = 1.20
b = r*(s_y/s_x)
a = y_bar-(b*x_bar)
#Input score of student
print("LSRL Equation is " + "y=" + str(a) + "+" + str(b) + "x")
x = float(80)
#Calculate score of student using equation
#Next addition would be to add the formulation of the equation
y = float(b)*x +a
print(y)
#if x < 0:
#    print("Inproper Usage")
#else:
#    print("A person with a grade of " + str(x) + " has a predicted ap score of " + str(y) + ".")
