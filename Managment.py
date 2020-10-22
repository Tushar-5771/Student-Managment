import tkinter as tk
from tkinter import ttk
import psycopg2 as pg
from tkinter import messagebox as mb
import pandas as pd


root = tk.Tk()

NoteBook = ttk.Notebook(root)

frame1 = tk.Frame(NoteBook, height=500, width=900)
frame2 = tk.Frame(NoteBook, height=500, width=900)
frame3 = tk.Frame(NoteBook, height=500, width=900)


NoteBook.add(frame1, text='Managment')
NoteBook.add(frame2, text='Collage Table')
NoteBook.add(frame3, text='Division Table')
NoteBook.pack()

tk.Label(frame1, text="1.Insert Data of Student\n2.Search For Studnet\n3.Update Data\n4.Delete Record\n5.View All Data\n6.Exit",
         justify='left', font=("verdana 12 bold")).pack()
F1_Label = tk.Label(frame1, text='Enter Your Choice: ',
                    font=("verdana 12 bold"))
F1_Label.place(x=160, y=120)
F1_Entry = tk.Entry(frame1, font=("verdana 12"))
F1_Entry.place(x=340, y=120)


F1_Button = tk.Button(frame1, text='Submit', font=("verdana 12"), command=Menu)
F1_Button.place(x=470, y=150)


Menu = tk.Menu(frame1, tearoff=False)
Menu.add_command(label='Create or Truncate all Tables', command=Create_Tables)


def callbackf1(event):
    Menu.post(event.x_root, event.y_root)


frame1.bind('<3>', callbackf1)


Clg_lable = tk.Label(frame2, text="Enter Collage Name: ",
                     font=("verdana 12 bold"))
Clg_lable.place(x=10, y=10)

Clg_Entry = tk.Entry(frame2, font=("verdana 12"))
Clg_Entry.place(x=200, y=10)

Clg_Button = tk.Button(frame2, text="Add Collage",
                       font=("verdana 12"), command=Add_Clg)
Clg_Button.place(x=200, y=50)

Menu2 = tk.Menu(frame2, tearoff=False)
Menu2.add_command(label='Show Collage', command=Show_Clg)


def callbackf2(event):
    Menu2.post(event.x_root, event.y_root)


frame2.bind('<3>', callbackf2)


Div_lable = tk.Label(frame3, text="Enter Division: ",
                     font=("verdana 12 bold"))
Div_lable.place(x=10, y=10)

Div_Entry = tk.Entry(frame3, font=("verdana 12"))
Div_Entry.place(x=200, y=10)

Div_Button = tk.Button(frame3, text="Add Division",
                       font=("verdana 12"), command=Add_Div)
Div_Button.place(x=200, y=50)

Menu3 = tk.Menu(frame3, tearoff=False)
Menu3.add_command(label='Show Division', command=Show_Div)


def callbackf3(event):
    Menu3.post(event.x_root, event.y_root)


frame3.bind('<3>', callbackf3)


root.mainloop()
