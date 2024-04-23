#Quadratic formula WIP
import cmath
#3 input variables a,b,c x=-b+-sqrt of b2-4ac /2a
a = float(raw_input("Enter value of a: "))
b = float(raw_input("Enter value of b: "))
c = float(raw_input("Enter value of c: "))
#discriminent b2 - 4ac
d = cmath.sqrt(b * b - 4 * a * c)
x = (-b + d) / (2 * a)
print(x)
x = (-b - d) / (2 * a)
print(x)