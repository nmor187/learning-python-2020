#Drawing a window in tkinter
def tkint():
    from tkinter import *
    test = Tk()
    test.title("Tryna figure this out rn")
    test.geometry('100x200')
    text = Label(test, text="chicken fries taste yummy")
    text.pack()
    test.mainloop()
tkint()
