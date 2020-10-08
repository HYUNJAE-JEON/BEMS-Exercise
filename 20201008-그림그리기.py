import tkinter
import random
def randxy():
    a = random.randint(1,250)
    return a

def click():
    cvs.create_line(randxy(),0,0,randxy())

root = tkinter.Tk()
cvs = tkinter.Canvas(root, width=250, height=250)
cvs.pack()

button = tkinter.Button(text='click', command=click)
cvs.create_window(150, 200, window=button)

label=tkinter.Label(text="Hellow")
label_w =cvs.create_window(100, 200)
cvs.itemconfigure(label_w,window=label)

root.mainloop()