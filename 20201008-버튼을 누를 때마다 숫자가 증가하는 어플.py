import tkinter
def increase():
    number.set(number.get()+1)

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()
number = tkinter.IntVar(value = 0)
button = tkinter.Button(frame, text = 'increase', command = increase)
button.pack()
label = tkinter.Label(frame, text = 'start', textvariable = number)
#textvariable을 number 로 주었기 때문에 0으로 덮어씌어져서 start가 실제로는 보이지가 않는다.

label.pack()
root.mainloop()
