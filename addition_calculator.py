from tkinter import *
root = Tk()
root.title("Simple Calculator Application")
root.geometry("500x500")
root['background']='#a1ebff'
root.grid()
text_num1 = Label(root, text = "First number")
text_num1.grid(row=1, column=0)
text_num1.pack()
text_num2 = Label(root, text = "Second number")
text_num2.grid(row=1, column=0)
text_num2.pack()
enter_num1 = Entry(root)
enter_num1.grid(row=0, column=1)
enter_num1.pack()
enter_num2 = Entry(root)
enter_num2.grid(row=1, column=1)
enter_num2.pack()
def submit():
	global num_1
	global num_2
	num_1 = enter_num1.get()
	num_2 = enter_num2.get()
	calc()
def calc():
	x = float(num_1) + float(num_2)
	popup = Tk()
	popup.geoemtry("100x50")
	popup.title("Test")
	text = Label(popup, text = x)
	text.pack()
submit = Button(root,text = 'Submit', command = submit)
submit.grid(row=3,column=0)
submit.pack()

root.mainloop()