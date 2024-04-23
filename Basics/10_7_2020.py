#basics 10-7-2020
def variables():
    #integer
    a = 3
    #float
    b = 3.44444
    #string
    c = "Yo whats up"
    #character
    d = 'a'
    print(a + b + c + d)
def operations():
    x = 3
    y = 5
    mult = x * y
    div = x / y
    add = x + y
    sub = x - y
    print(mult + div + add + sub)
def if_statements():
    x = 3
    y = 4
    if x == 3:
        print("x is 3")
    elif x > y:
        print("x is greater than y")
    elif x < y:
        print("x is less than y")
    else:
        print("An error occured while executing this function")
def for_loops():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in list:
        print("Are there " + list + " months in a year?")
def methods():
    string = "Strings are made to be changed."
    print(string.upper())
    print(string.lower())
