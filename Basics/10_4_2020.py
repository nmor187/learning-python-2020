#Basics practice for the 4th of October
prnt = "Basics 10-4-2020"
print(prnt)
if "BASICS" in prnt.upper():
    bool = True
else:
    bool = False
def func():
    if bool = False:
        print("This was a waste of time")
    elif bool = True:
        print("Turns out java > python")
    else:
        print("why are you here")
def lists():
    numbers = [1,2,3,4,5,6,]
    languages = ['Java', 'Python', 'C']
    if 1 in numbers:
        print("The value is in there")
    else:
        print("Values " + nums_langs + "are written in " + langs_nums)
    nums_langs = numbers[0:5]
    langs_nums = languages[1]
    for i in languages:
        print("One common language is " + i)
def story():
    protagonist = "Tim"
    antagonist = "Lindsey"
    location = "Canada"
    print("Once upon a time, " + protagonist + " was in " + location + " with " + antagonist + "!")
def taking_inputs():
    first_name = raw_input("What is your first name? ")
    last_name = raw_input("What is your last name? ")
    age = int(input("How many years old are you? "))
    print("The following information has been recorded for security purposes...")
    info = [first_name, last_name, age]
    for i in info:
        print(i)
    email = raw_input("Enter your email: ")
    password = raw_input("Enter your password: ")
    correct_email = "user@gmail.com"
    correct_password = "123456"
    if email is correct_email and password is correct_password:
        print("Access granted")
        access()
    else:
        print("Access denied")
def access():
    print("Welcome to the program! I have no idea what this is.")
    
