import tkinter, sys
def increase():
    number1.set(number1.get() + 1)
    if number1.get() > 10:
        root.destroy() #화면에 보이는 것만 없애는 것이다.
        root.quit()
        sys.exit() #어플리케이션 전체종료
def decrease():
    number1.set(number1.get() - 1)
    if number1.get() < 0:
        root.destroy()
        root.quit()
        sys.exit()
def inverse():
    if number2.get() == 0:
        number2.set(1)
    else:
        number2.set(0)

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()
number1 = tkinter.IntVar(value = 0)
number2 = tkinter.IntVar(value = 0)
button1 = tkinter.Button(frame, text = '밝게', command = increase)
button2 = tkinter.Button(frame, text = '어둡게', command = decrease)
button3 = tkinter.Button(frame, text = 'on/off', command = inverse)
button1.pack(side='left',fill='both')
button2.pack(side='right',fill='both')
button3.pack(side='bottom',fill='both')
label1 = tkinter.Label(frame, text = 'start', textvariable = number1)
label2 = tkinter.Label(frame, text = 'start', textvariable = number2)
label1.pack()
label2.pack()
#textvariable을 number 로 주었기 때문에 0으로 덮어씌어져서 start가 실제로는 보이지가 않는다.

root.mainloop()
