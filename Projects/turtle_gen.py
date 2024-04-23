from turtle import Turtle
t = Turtle()
i = raw_input("What would you like to draw? ")
i = list(i)
input()
if i[0] is 'a':
	letter_a()
else:
	print("An unregognized character was recognized")
def letter_a():
	t.setpos(0, 0)
	t.left(90)
	t.forward(25)
	t.right(90)
	t.forward(25)
	t.right(90)
	t.forward(30)
	t.left(180)
	t.forward(5)
	t.left(90)
	t.forward(25)
	t.penup()
	new_pos = t.pos()
	x = z.split((',')[0])
	y = z.split((',')[1])
	#draw letter
	#calculate distance over x
	#update pos_x and pos_y variables
#move pos over say dist of letter + 10 something like this
#pos = [(pos_x + 10), (pos_y + 10)]
