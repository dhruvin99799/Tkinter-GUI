from tkinter import *
import mysql.connector

m = Tk()
m.title("Result")
m.geometry("500x500")
con=mysql.connector.connect(host="localhost",user="root",password="",database="system")
cur=con.cursor()

def call():
    name = e_name.get()
    s1 = e1.get()
    s2 = e2.get()
    s3 = e3.get()
    s4 = e4.get()
    s5 = e5.get()

    submit(name,s1,s2,s3,s4,s5)

def submit(name,s1,s2,s3,s4,s5):
    sql = "insert into result(name,s1,s2,s3,s4,s5) values (%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,(name,s1,s2,s3,s4,s5))
    m.destroy()

b=Button(m,text="Insert",command=call)
b.grid(row=7,column=3)

name = Label(m,text="Name")
name.grid(row=0,column=0)
e_name = Entry()
e_name.grid(row=0,column=3)


s1 = Label(m,text="Sub1")
s1.grid(row=1,column=0)
e1 = Entry()
e1.grid(row=1,column=3)

s2 = Label(m,text="Sub2")
s2.grid(row=2,column=0)
e2 = Entry()
e2.grid(row=2,column=3)

s3 = Label(m,text="Sub3")
s3.grid(row=3,column=0)
e3 = Entry()
e3.grid(row=3,column=3)

s4 = Label(m,text="Sub4")
s4.grid(row=4,column=0)
e4 = Entry()
e4.grid(row=4,column=3)

s5 = Label(m,text="Sub5")
s5.grid(row=5,column=0)
e5 = Entry()
e5.grid(row=5,column=3)



# b1=Button(m,text="Select")
# b1.grid(row=0,column=9)
# b2=Button(m,text="Update")
# b2.grid(row=2,column=9)
# b3=Button(m,text="Delete")
# b3.grid(row=4,column=9)
m.mainloop()