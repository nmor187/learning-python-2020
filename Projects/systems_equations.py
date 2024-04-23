#Systems of equations solver
def number_equations():
    num = int(input("Do you have 2 or 3 equations? "))
    if num == 2:
        input_equations_2()
        organize_equations_2()
        solve_equations_2()                                 
        print_equations_2()
    elif num == 3:
        input_equations_3()
        organize_equations_3()
        solve_equations_3()
        print_equations_3()
    else:
        print("An error occured")
        exit()
import re
from re import search
#first_equation = "12x+1y=18"
#second_equation = "7x+8y=32"
def input_equations_2():
    global first_equation
    global second_equation
    first_equation = raw_input("What is your first equation? ")
    second_equation = raw_input("What is your second equation? ")
def organize_equations_2():
    nums = '\d+'
    global first_equation
    global second_equation
    global nums_1
    global nums_2
    nums_1 = re.findall(nums, first_equation)
    nums_2 = re.findall(nums, second_equation)
    for i in range(0, len(nums_1)):
        nums_1[i] = float(nums_1[i])
    for i in range(0, len(nums_2)):
        nums_2[i] = float(nums_2[i])
    print(nums_1)
    print(nums_2)
#    find_ops_1 =
#    find_ops_2 =
#    ops_1 =
#    ops_2 =
#    print(ops_1)
#    print(ops_2)
def solve_equations_2():
    global nums_1
    global nums_2
    global x
    global y
    a = nums_1[0]
    b = nums_1[1]
    c = nums_1[2]
    f = nums_2[0]
    d = nums_2[1]
    g = nums_2[2]
    y = ((c * (-f / a)) + g) / ((b * (-f / a)) + d)
    x = (((y) * (c - b)) / a)
def print_equations_2():
    print("x = ")
    print(x)
    print("y = ")
    print(y)
organize_equations_2()
solve_equations_2()
print_equations_2()
def input_equations_3():
    first_equation = raw_input("What is your first equation? ")
    second_equation = raw_input("What is your second equation? ")
    third_equation = raw_input("What is your third equation? ")
def organize_equations_3():
    print("Organizing")
def solve_equations_3():
    print("Solving")
def print_equations_3():
    print("Printing")
