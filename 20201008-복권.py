import random
import tkinter

def RichLotto():
    global x
    Lotto = set()
    for i in range(6):
        a = random.randint(1,49)
        Lotto.add(a)
        x.set(Lotto)
        i += 1
    print(Lotto, end=" ")



root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()
x = tkinter.StringVar(value = "")
# x2 = tkinter.IntVar(value = 0)
# x3 = tkinter.IntVar(value = 0)
# x4 = tkinter.IntVar(value = 0)
# x5 = tkinter.IntVar(value = 0)
# x6 = tkinter.IntVar(value = 0)
button1 = tkinter.Button(frame, text = '오늘의 당첨번호는?', command = RichLotto)
button1.pack()
label1 = tkinter.Label(frame, text='start', textvariable =x)
# label2 = tkinter.Label(frame, text = 'start', textvariable =x2)
# label3 = tkinter.Label(frame, text = 'start', textvariable =x3)
# label4 = tkinter.Label(frame, text = 'start', textvariable =x4)
# label5 = tkinter.Label(frame, text = 'start', textvariable =x5)
# label6 = tkinter.Label(frame, text = 'start', textvariable =x6)
label1.pack()
# label2.pack()
# label3.pack()
# label4.pack()
# label5.pack()
# label6.pack()
#
root.mainloop()

# 강사님 코드

# ev = set()
# while len(ev) <6:
#     i = random.randint(1,45)
#     ev.add(i)
# print(list(ev))