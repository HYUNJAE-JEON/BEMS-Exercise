import tkinter

def callback():
    root.title("Hello Python")

root = tkinter.Tk()
frame = tkinter.Frame(root, padx=100, pady=50)
frame.pack()

button = tkinter.Button(frame, text = 'click')
button.pack()

button.bind("<ButtonPress-1>",lambda  e: callback())
button.bind("<Double-1>", lambda e: root.title("Mouse Double Click"))
button.bind("<ButtonPress-3>",lambda e: root.title("Mouse Right Click"))

root.mainloop()