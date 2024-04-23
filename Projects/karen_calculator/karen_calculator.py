#Karen Calculator - Predict if someone is a Karen based on their responses to certain questions
loop = 1
while (loop == 1):
	name = raw_input("What is your first name? " ).lower()
	f = open('/Users/nathanmorgan/Desktop/Python/Projects/karen_calculator/karens.txt', "r")
	karens = f.read().splitlines()
	if name in karens:
		print("Error")
		exit()
		f.close()
	else:
		break
		f.close()
while (loop == 1):
	question_1 = raw_input("Do you find teenagers annoying? ")
	if ('Y' in question_1) or ('y' in question_1):
		answer_1 = 1
		break
	elif ('N' in question_1) or ('n' in question_1):
		answer_1 = 0
		break
	else:
		print("Error")
		exit()
while (loop == 1):
	question_2 = raw_input("Does loud noise bother you? ")
	if ('Y' in question_2) or ('y' in question_2):
		answer_2 = 1
		break
	elif ('N' in question_2) or ('n' in question_2):
		answer_2 = 0
		break
	else:
		print("Error")
		exit()
while (loop == 1):
	race_white = ["white", "caucasian", "european"]
	race_asian = ["asian", "chinese", "japanese"]
	race_african = ["africa", "black"]
	question_3 = raw_input("What would you consider your race or ethnicity? ").lower()
	if question_3 in race_white:
		answer_3 = 1
		break
	elif question_3 in race_asian:
		answer_3 = 0
		break
	elif question_3 in race_african:
		answer_3 = 0
		break
	else:
		print("Error")
		exit()
#Actual Karen Calculation Section
#Still need 10 total questions to make proper analysis of data entered
print("Thank you for taking this test " + name + "!")
points = answer_3 + answer_2 + answer_1
if points >= 2:
	f = open('/Users/nathanmorgan/Desktop/Python/Projects/karen_calculator/karens.txt', "a")
	f.write("\n" + name)
	f.close()
	print("We have determined that you ARE a Karen.")
else:
	print("We have determined that you AREN'T a Karen.")
