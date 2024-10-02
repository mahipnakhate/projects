import mysql.connector
from tkinter import *
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()

    if username == '' or password == '':
        messagebox.showerror('login', 'BLANKS ARE NOT ALLOWED')
    elif username == 'login' and password == '1234':
        messagebox.showinfo('login', 'LOGIN SUCCESSFUL')
        root.destroy()

        base = Tk()
        base.configure(bg='white')
        base.geometry("1000x700")  

        label4 = Label(base, text='REGISTRATION FORM', bg='white', fg='black', font=('Arial', 30))
        label4.place(x=400, y=40)

        label5 = Label(base, text='Name', bg='white', fg='black', font=('Arial', 20))
        label5.place(x=400, y=150)

        label6 = Label(base, text='ID', bg='white', fg='black', font=('Arial', 20))
        label6.place(x=400, y=250)

        label7 = Label(base, text='Email', bg='white', fg='black', font=('Arial', 20))
        label7.place(x=400, y=350)

        label8 = Label(base, text='Phone', bg='white', fg='black', font=('Arial', 20))
        label8.place(x=400, y=450)

        entry3 = Entry(base, font=('Arial', 20), bg='gray', fg='white')
        entry3.place(x=600, y=150)

        entry4 = Entry(base, font=('Arial', 20), bg='gray', fg='white')
        entry4.place(x=600, y=250)

        entry5 = Entry(base, font=('Arial', 20), bg='gray', fg='white')
        entry5.place(x=600, y=350)

        entry6 = Entry(base, font=('Arial', 20), bg='gray', fg='white')
        entry6.place(x=600, y=450)

        def submit_data():
            n = entry3.get()
            i = entry4.get()
            em = entry5.get()
            p = entry6.get()

            if n == '' or i == '' or em == '' or p == '':
                messagebox.showerror('Error', 'All fields are required!')
                return

            myconn = mysql.connector.connect(host="localhost", user="root", password="", database="registration_form")
            cur = myconn.cursor()
            sql = "INSERT INTO form(name, id, email, phone) VALUES (%s, %s, %s, %s)"
            val = (n, i, em, p)
            try:
                cur.execute(sql, val)
                myconn.commit()
                messagebox.showinfo('Success', 'Record inserted successfully!')
            except Exception as e:
                messagebox.showerror('Database Error', str(e))
                myconn.rollback()
            finally:
                cur.close()
                myconn.close()

        button1 = Button(base, text='SUBMIT', bg='gray', font=('Arial', 20), bd=10, command=submit_data)
        button1.place(x=550, y=550)

    else:
        messagebox.showerror('login', 'INVALID USERNAME OR PASSWORD')


root = Tk()
root.configure(bg='white')

label1 = Label(root, text='LOGIN', bg='white', fg='cyan4', font=('Arial', 40))
label1.place(x=600, y=20)

label2 = Label(root, text='USERNAME :', bg='white', fg='black', font=('Arial', 30))
label2.place(x=400, y=190)

label3 = Label(root, text='PASSWORD', bg='white', fg='black', font=('Arial', 30))
label3.place(x=400, y=340)

entry1 = Entry(root, font=('Arial', 20))
entry1.place(x=700, y=190)

entry2 = Entry(root, font=('Arial', 20), show='*')
entry2.place(x=700, y=340)

button = Button(root, text='LOGIN', bg='brown', font=('Arial', 20), bd=10, command=login)
button.place(x=650, y=500)

root.geometry("1000x700") 
root.mainloop()
