from tkinter import *
window = Tk()
window.title("Nathan's First Window In Tkinter")
window.geometry('500x250')
text = Label(window, text="This is a little bit of text.")
text.grid(column=0, row=0)
text2 = Label(window, text="Some text can be put into different columns.")
text2.grid(column=1, row=0)
text4 = Label(window, text="This is in the 6th column and the 4th row.")
text4.grid(column=5, row=3)

window.mainloop()
