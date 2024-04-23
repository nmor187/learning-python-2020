def appending():
    f = open('/Users/nathanmorgan/Documents/Atom/Python/Random/datarec.txt', 'a+')
    list = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    for i in list:
        f.write(i + "\n")
    f.close()
#opening a refreshed verison of it
def txt_to_list():
    f = open('/Users/nathanmorgan/Documents/Atom/Python/Random/datarec.txt', 'r')
    list = []
    for line in f:
        stripped = line.strip()
        splitted = stripped.split()
        list.append(splitted)
    print(list)
txt_to_list()
#f = open('/Users/nathanmorgan/Documents/Atom/Python/Random/datarec.txt', 'r')
#print(f.read())
