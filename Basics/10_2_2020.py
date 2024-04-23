import re
from re import search
def finding():
    string = "y=2x+1"
    #default search for numbers
    regex = '\d+'
    find = re.findall(regex, string)
    mapped = list(map(int, find))
    print(mapped)
    operation = "+"
    if re.search(operation, string):
        print("+")
    else:
        print("no operations")
finding()
