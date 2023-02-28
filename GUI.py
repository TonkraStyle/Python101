from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('วันนี้รู้สึกอย่างไร')
GUI.geometry('500x500')

L1 = Label(GUI,text='วันนี้รู้สึกอย่างไร',font=('Angsana New',30),fg='black')
L1.place(x=150,y=1)

def Button1():
    text = 'อย่าลืมมาเเสดงความรู้สึกอีกนะ'
    messagebox.showinfo ('app' ,text)

FB1 = Frame(GUI)
FB1.place(x=175,y=100)
B1 = ttk.Button(FB1,text='สบาย',command=Button1)
B1.pack(ipadx=20,ipady=20)

def Button2():
    text = 'อย่าลืมมาเเสดงความรู้สึกอีกนะ'
    messagebox.showinfo ('app' ,text)

FB2 = Frame(GUI)
FB2.place(x=175,y=100)
B2 = ttk.Button(FB1,text='ชิลๆ',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'อย่าลืมมาเเสดงความรู้สึกอีกนะ'
    messagebox.showinfo ('app' ,text)

FB3 = Frame(GUI)
FB3.place(x=175,y=100)
B3 = ttk.Button(FB1,text='เครียด',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'อย่าลืมมาเเสดงความรู้สึกอีกนะ'
    messagebox.showinfo ('app' ,text)

FB4 = Frame(GUI)
FB4.place(x=175,y=100)
B4 = ttk.Button(FB1,text='ป่วย',command=Button4)
B4.pack(ipadx=20,ipady=20)

def Button5():
    text = 'อย่าลืมมาเเสดงความรู้สึกอีกนะ'
    messagebox.showinfo ('app' ,text)

FB5 = Frame(GUI)
FB5.place(x=175,y=100)
B5 = ttk.Button(FB1,text='หงุดหงิด',command=Button5)
B5.pack(ipadx=20,ipady=20)

def Button6():
    text = 'อย่าลืมมาเเสดงความรู้สึกอีกนะ'
    messagebox.showinfo ('app' ,text)

FB6 = Frame(GUI)
FB6.place(x=175,y=100)
B6 = ttk.Button(FB1,text='เบื่อ',command=Button6)
B6.pack(ipadx=20,ipady=20)

















