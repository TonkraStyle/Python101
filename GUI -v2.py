from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime

######################################################################

import csv

def writecsv(datalist):
    with open ('Data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('Data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
        return data

######################################################################


GUI = Tk()
GUI.title('วันนี้อ่านหนังสืออะไร')
GUI.geometry('800x600')

L1 = Label(GUI,text='วันนี้อ่านหนังสืออะไร',font=('Angsana New',30),fg='black')
L1.place(x=120,y=1)


def Button1():
    text = 'กลับมาบันทึกอีกนะ'
    messagebox.showerror ('app' ,text)

FB1 = Frame(GUI)
FB1.place(x=175,y=100)
B1 = ttk.Button(FB1,text='การ์ตูน',command=Button1)
B1.pack(ipadx=20,ipady=20)

def Button2():
    text = 'กลับมาบันทึกอีกนะ'
    messagebox.showerror ('app' ,text)

FB2 = Frame(GUI)
FB2.place(x=175,y=100)
B2 = ttk.Button(FB1,text='วรรณกรรม',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'กลับมาบันทึกอีกนะ'
    messagebox.showerror ('app' ,text)

FB3 = Frame(GUI)
FB3.place(x=175,y=100)
B3 = ttk.Button(FB1,text='เเปล',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'กลับมาบันทึกอีกนะ'
    messagebox.showerror ('app' ,text)

FB4 = Frame(GUI)
FB4.place(x=175,y=100)
B4 = ttk.Button(FB1,text='นิยาย',command=Button4)
B4.pack(ipadx=20,ipady=20)

def Button5():
    text = 'กลับมาบันทึกอีกนะ'
    messagebox.showerror ('app' ,text)

FB5 = Frame(GUI)
FB5.place(x=175,y=100)
B5 = ttk.Button(FB1,text='อื่นๆ',command=Button5)
B5.pack(ipadx=20,ipady=20)

def Button6():
    text = 'กลับมาบันทึกอีกนะ'
    messagebox.showerror ('app' ,text)

FB6 = Frame(GUI)
FB6.place(x=175,y=100)
B6 = ttk.Button(FB1,text='ไม่ได้อ่าน',command=Button6)
B6.pack(ipadx=20,ipady=20)

######################################################################################

LF1 = ttk.LabelFrame(GUI,text='ชื่อหนังสือ')
LF1.place(x=400,y=250)

v_data = StringVar() 
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=70)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() 
    text = [t,data] 
    writecsv(text) 
    v_data.set('') 

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)
