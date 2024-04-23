x = 1
y = 2
z = 3
def variables():
    x = 1
    y = "string"
    z = ['a', 'b', 'c']
    print(z[0].lower() + z[1].upper() + z[2].upper())
    print(z[0:4])
    float_x = float(x)
    print(float_x)
    int_x = int(x)
    print(int_x)
def comparing_variables():
    sum = x + y + z
    if sum == 10:
        print("The sum is 10")
    else:
        print("The sum is not 10")
    string = "How to get the sum of numbers"
    string_split = string.lower().split()
    print(string_split)
    print(len(string_split))
def chaining_conditions():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Comparing conditions through chain comparisons")
    print("AND THE VERDICT IS...")
    if x > y:
        print("x is greater than y")
    elif x < y:
        print("x is less than y")
    else:
        print("x is equal to y")
def operations():
    input = raw_input("What operation would you like to perform? divide, multiply, add, subtract")
    a = 10
    b = 940
    c = 345
    if input is "add" or "+" or "addition":
        print(a + b + c)
    elif input is "subtract" or "sub" or "-":
        print(a - b - c)
    elif input is "divide" or "division" or "/":
        print(a / b / c)
    else:
        print(a * b * c)
#
#
#

def test_func():
    x = 3
    y = x
    z = x + y
    list = [1,2,3,4,5]
    test =  list[0]
    test1 = list[1]
    answer = test1 + test
    print(answer)
def test_eq():
    import re
    first_equation = "12x+1y=18"
    second_equation = "7x-8y=32"
    nums = '\d+'
    nums_1 = re.findall(nums, first_equation)
    nums_2 = re.findall(nums, second_equation)
    for i in range(0, len(nums_1)):
        nums_1[i] = float(nums_1[i])
    print(nums_1)
    print(nums_2)
def variables_ifs():
    x = 3
    y = 4
    z = [1,2,3,4,5,6,7,8]
    a = z[1]
    test = ("Test")
    if a is x:
        print(test)
    elif a not in z:
        print("The answer is in the list")
    else:
        print("Error, please try again.")
