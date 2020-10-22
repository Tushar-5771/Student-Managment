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

            CREATE TABLE student (StudentID  SERIAL PRIMARY KEY ,
            name VARCHAR(20) NOT NULL,
            Depat VARCHAR(20) NOT NULL,
            Div INTEGER NOT NULL,
            Clg INTEGER NOT NULL);

            CREATE TABLE Division (Div_ID  SERIAL PRIMARY KEY,
            Div VARCHAR(10) NOT NULL);

            CREATE TABLE Clg (Clg_ID   SERIAL PRIMARY KEY,
            Clg VARCHAR(30) NOT NULL);''')
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


def Insert():
    window = tk.Tk()
    tk.Label(window, text='Enter Student Name: ', font=(
        "verdana 12 bold")).grid(row=0, column=0)
    tk.Entry(window, font=("verdana 12 bold")).grid(row=0, column=1)

    tk.Label(window, text='Enter Department: ', font=(
        "verdana 12 bold")).grid(row=1, column=0)
    tk.Entry(window, font=("verdana 12 bold")).grid(row=1, column=1)

    cur.execute("SELECT * FROM Division;")
    Div_Query = cur.fetchall()
    length = len(Div_Query)
    if length > 0:
        Div_List = []
        for i in range(length):
            Div_List.append(Div_Query[i][1])
    

def Menu():
    choice = F1_Entry.get().strip()
    if choice == '1':
        Insert()
