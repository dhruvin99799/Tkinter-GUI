from tkinter import *
import mysql.connector
m = Tk()
m.geometry("500x500")
m.title("contact Book")

con=mysql.connector.connect(host="localhost" , user="root" , password="" , database="system")

cur = con.cursor()


def cal():
    name=c_name.get()
    number=c_number.get()
    email=c_email.get()


    # e1.config(text=name)
    # e2.config(text=number)
    # e3.config(text=email)
    submit(name,number,email)


def submit(name,number,email):
    sql = "insert into contact(name,number,email) values (%s,%s,%s)"
    cur.execute(sql,(name,number,email))
    con.commit()
    # m.destroy()
    
def select():
    sql ="SELECT * FROM `contact`"
    cur.execute(sql)
    rows = cur.fetchall()
    i=5
    for row in rows:
        j=0
        for data in row:
            lbl =  Label(m,text=data)
            lbl.grid(row=i,column=j)
            j+=1
        i+=1
    print(rows)
select()   


def update():
    sql = "UPDATE `contact` SET `name`='Dhruvin',`number`='99799',`email`='email@gmail.com'"
    cur.execute(sql)
    con.commit()
update()

def delete():
    sql = "DELETE FROM `contact`"
    cur.execute(sql)
    con.commit()
delete()
    
   

name=Label(m,text="Name")
name.grid(row=0, column=0)
number=Label(m,text="Phone Number")
number.grid(row=1, column=0)
email=Label(m,text="Email")
email.grid(row=2, column=0)



c_name = Entry()
c_name.grid(row= 0 , column=1)
c_number = Entry()
c_number.grid(row=1 , column=1)
c_email = Entry()
c_email.grid(row=2 , column=1)



b=Button(m,text="Insert" , command=cal)
b.grid(row= 0 , column= 5)
b1=Button(m,text="Select",command=select)
b1.grid(row=0,column=6)
b2=Button(m,text="Update",command=update)
b2.grid(row=0,column=7)
b3=Button(m,text="Delete",command=delete)
b3.grid(row=0,column=8)
# e1 = Label(m, text="")
# e1.grid(row=8,column=1)
# e2 = Label(m, text="")
# e2.grid(row=8,column=2)
# e3 = Label(m, text="")
# e3.grid(row=8,column=3)
# name.config

m.mainloop()