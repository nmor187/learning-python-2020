def for_statements():
	x = [1,2,3,4,5]
	for i in x:
		print(i)
		if i == 3:
			break
for_statements()
def for_ranges():
	f = open('/Users/nathanmorgan/Desktop/100k.txt', "w")
	for x in range (100000):
		f.write("\n" + str(x))
	f.close()
def variables():
	x = 3
	y = True
	z = "No"
	a = 4
	dictionary = {
	"year":2020}
	r = dictionary["year"]
	print(r)
variables()