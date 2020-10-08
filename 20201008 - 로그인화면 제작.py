# import 하고 함수들 선언하고 그리고 GUI로 화면 구성
import tkinter
import pandas as pd
def reset():
    text_id.set('')
    text_pw.set('')
root = tkinter.Tk()
root.title("Login")
root.geometry('180x80')
#윈도우 사이즈 설정, x 를 기준으로 계산이 가능하다.
text_id = tkinter.StringVar(value='')
text_pw = tkinter.StringVar(value='')
frame = tkinter.Frame(root)
frame.pack()
button = tkinter.Button(frame, text='reset', command=reset)
button.grid(row=0, column=0, columnspan = 2)
label = tkinter.Label(frame, text='ID')
label.grid(row=1, column=0)
entry_id = tkinter.Entry(frame, textvariable=text_id)
entry_id.grid(row=1, column=1)
label = tkinter.Label(frame, text = 'PW')
label.grid(row=2, column=0)
entry_pw = tkinter.Entry(frame, textvariable=text_pw, show="*")
entry_pw.grid(row=2, column=1)
root.mainloop()

