import tkinter as tk
from tkinter import ttk
import psycopg2 as pg
from tkinter import messagebox as mb, ttk
import pandas as pd

try:
    conn = pg.connect(
        database='Student',
        user='postgres',
        password='Tush@r2264',
        host='localhost',
        port='5432'
    )

    cur = conn.cursor()
except Exception as e:
    print(e)


def Create_Tables():
    try:
        cur.execute('''DROP TABLE IF EXISTS student;

            DROP TABLE IF EXISTS Division;

            DROP TABLE IF EXISTS Clg;
            
            DROP TABLE IF EXISTS Dep;

            CREATE TABLE student (StudentID  SERIAL PRIMARY KEY ,
            name VARCHAR(20) NOT NULL,
            Depat VARCHAR(20) NOT NULL,
            Div VARCHAR(20) NOT NULL,
            Clg VARCHAR(20) NOT NULL);

            CREATE TABLE Division (Div_ID  SERIAL PRIMARY KEY,
            Div VARCHAR(10) NOT NULL);

            CREATE TABLE Clg (Clg_ID   SERIAL PRIMARY KEY,
            Clg VARCHAR(30) NOT NULL);
            
            CREATE TABLE Dep (Dep_ID   SERIAL PRIMARY KEY,
            Dep VARCHAR(50) NOT NULL);''')
        mb.showinfo('Successful', 'Tables Are Created Successfullly...')
    except pg.Error as e:
        mb.showerror('Error', e)
    conn.commit()


def Add_Clg():
    clg_value = str(Clg_Entry.get())
    if clg_value == '':
        mb.showerror('Invalid Input', 'Please Enter Collage Name')
    else:
        ClgQuery = "INSERT INTO Clg (Clg) VALUES('{}');".format(clg_value)

        try:
            cur.execute(ClgQuery)
            mb.showinfo('Successful', 'Collage Name Entered Successfullly...')
        except pg.Error as e:
            mb.showerror('Error', e)
        conn.commit()


def Add_Div():
    div_value = str(Div_Entry.get())
    if div_value == '':
        mb.showerror('Invalid Input', 'Please Enter Division')
    else:
        DivQuery = "INSERT INTO Division (Div) VALUES('{}');".format(div_value)

        try:
            cur.execute(DivQuery)
            mb.showinfo('Successful', 'Division Entered Successfullly...')
        except pg.Error as e:
            mb.showerror('Error', e)
        conn.commit()


def Add_Dep():
    dep_value = str(Dep_Entry.get())
    if dep_value == '':
        mb.showerror('Invalid Input', 'Please Enter Department')
    else:
        DepQuery = "INSERT INTO Dep (Dep) VALUES('{}');".format(dep_value)

        try:
            cur.execute(DepQuery)
            mb.showinfo('Successful', 'Department Entered Successfullly...')
        except pg.Error as e:
            mb.showerror('Error', e)
        conn.commit()


def Show_Clg():
    try:
        Query = "SELECT * FROM Clg;"
        cur.execute(Query)
        rows = cur.fetchall()
        my_w = tk.Tk()
        i = 0
        for student in rows:
            for j in range(len(student)):
                e = tk.Entry(my_w, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tk.END, student[j])
            i = i+1
    except pg.Error as e:
        mb.showerror('Error', e)


def Show_Div():
    try:
        Query = "SELECT * FROM Division;"
        cur.execute(Query)
        rows = cur.fetchall()
        my_w = tk.Tk()
        i = 0
        for student in rows:
            for j in range(len(student)):
                e = tk.Entry(my_w, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tk.END, student[j])
            i = i+1
    except pg.Error as e:
        mb.showerror('Error', e)


def Show_Dep():
    try:
        Query = "SELECT * FROM Dep;"
        cur.execute(Query)
        rows = cur.fetchall()
        my_w = tk.Tk()
        i = 0
        for student in rows:
            for j in range(len(student)):
                e = tk.Entry(my_w, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tk.END, student[j])
            i = i+1
    except pg.Error as e:
        mb.showerror('Error', e)


def Insert():

    def saveData():
        name = str(inName.get())
        dep = str(inDep.get())
        div = inDiv.get()
        clg = inClg.get()
        if name == '' and dep == '' and div == '' and clg == '':
            mb.showerror('Invalid Input', 'Please All The Fields..')
        else:
            inQuery = "INSERT INTO student(name,depat,div,clg) VALUES('{}','{}','{}','{}');".format(
                name, dep, div, clg)
            try:
                cur.execute(inQuery)
                mb.showinfo('Successful', 'Data Inserted Successfullly...')
            except pg.Error as e:
                mb.showerror('Error', e)
            conn.commit()

    window = tk.Tk()
    tk.Label(window, text='Enter Student Name: ', font=(
        "verdana 12 bold")).grid(row=0, column=0)
    inName = tk.Entry(window, font=("verdana 12 bold"))
    inName.grid(row=0, column=1)

    cur.execute("SELECT * FROM Dep;")
    Dep_Query = cur.fetchall()
    depLength = len(Dep_Query)
    Dep_List = []
    if depLength > 0:
        for i in range(depLength):
            Dep_List.append(Dep_Query[i][1])
    tk.Label(window, text='Department: ', font=(
        "verdana 12 bold")).grid(row=1, column=0)
    inDep = ttk.Combobox(window, values=Dep_List, font=(
        "verdana 11 bold"))
    inDep.grid(row=1, column=1)

    cur.execute("SELECT * FROM Division;")
    Div_Query = cur.fetchall()
    length = len(Div_Query)
    Div_List = []
    if length > 0:
        for i in range(length):
            Div_List.append(Div_Query[i][1])
    tk.Label(window, text='Division: ', font=(
        "verdana 12 bold")).grid(row=2, column=0)
    inDiv = ttk.Combobox(window, values=Div_List, font=(
        "verdana 11 bold"))
    inDiv.grid(row=2, column=1)

    cur.execute("SELECT * FROM Clg;")
    Clg_Query = cur.fetchall()
    Clglength = len(Clg_Query)
    Clg_List = []
    if Clglength > 0:
        for i in range(Clglength):
            Clg_List.append(Clg_Query[i][1])
    tk.Label(window, text='College: ', font=(
        "verdana 12 bold")).grid(row=3, column=0)
    inClg = ttk.Combobox(window, values=Clg_List, font=(
        "verdana 11 bold"))
    inClg.grid(row=3, column=1)

    tk.Button(window, text='Insert', font=("verdana 12"),
              command=saveData).grid(row=4, column=1)


def Menu():
    choice = F1_Entry.get().strip()
    if choice == '1':
        Insert()
    elif choice == '6':
        root.destroy()


root = tk.Tk()

NoteBook = ttk.Notebook(root)

frame1 = tk.Frame(NoteBook, height=500, width=900)
frame2 = tk.Frame(NoteBook, height=500, width=900)
frame3 = tk.Frame(NoteBook, height=500, width=900)
frame4 = tk.Frame(NoteBook, height=500, width=900)


NoteBook.add(frame1, text='Managment')
NoteBook.add(frame2, text='Collage Table')
NoteBook.add(frame3, text='Division Table')
NoteBook.add(frame4, text='Department Table')
NoteBook.pack()


# main menu
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

# clg panel
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

# div panel
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

# dept panel
Dep_lable = tk.Label(frame4, text="Enter Department: ",
                     font=("verdana 12 bold"))
Dep_lable.place(x=10, y=10)

Dep_Entry = tk.Entry(frame4, font=("verdana 12"))
Dep_Entry.place(x=200, y=10)

Dep_Button = tk.Button(frame4, text="Add Department",
                       font=("verdana 12"), command=Add_Dep)
Dep_Button.place(x=200, y=50)

Menu4 = tk.Menu(frame4, tearoff=False)
Menu4.add_command(label='Show Department', command=Show_Dep)


def callbackf4(event):
    Menu4.post(event.x_root, event.y_root)


frame4.bind('<3>', callbackf4)

root.mainloop()
