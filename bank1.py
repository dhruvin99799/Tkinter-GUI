from tkinter import *
m = Tk()
m.title("Bank System")
m.geometry("500x500")
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="system")
cur=con.cursor()


name = Label(m,text="Name")
name.place(x=30,y=30)
c_name = Entry()
c_name.place(x=150,y=30)

mn = Label(m,text="M.Number")
mn.place(x=30,y=60)
mn_num = Entry()
mn_num.place(x=150,y=60)
    
acno = Label(m,text="Account Number")
acno.place(x=30,y=90)
ac_no = Entry()
ac_no.place(x=150,y=90)



def call():

    name = c_name.get()
    mn = mn_num.get()
    acno = ac_no.get()

    select.config
  

   

    insert(name,mn,acno)
    select(name,mn,acno)
    delete(name,mn,acno)

def insert(name,mn,acno):
    sql = "insert into new(name,mn,acno) values (%s,%s,%s)"
    cur.execute(sql,(name,mn,acno))
    con.commit()
    m.destroy()

def select(name,mn,acno):
    select = "SELECT * FROM `new` WHERE 1"
    cur.execute(select)
    con.commit

def delete():
    delete = "DELETE FROM `new` WHERE 1"
    cur.execute(delete)
    con.commit()





    
    

    
Button(m,text="submit",font="bold 15",border=5,bg="#000814",fg="white",padx=5,pady=5,command=call).place(x=150,y=150)
Button(m,text="Select",font="bold 15",border=5,bg="#000814",fg="white",padx=5,pady=5,command=select).place(x=250,y=150)
Button(m,text="Delete",font="bold 15",border=5,bg="#000814",fg="white",padx=5,pady=5,command=select).place(x=350,y=150)










    

# Button(m,text="1.Create Account",font="bold 15",border=5,bg="#000814",fg="white",command=crte).place(x=20,y=20)
# Button(m,text="2.Saving Account",font="bold 15",border=5,bg="#000814",fg="white",command=save).place(x=220,y=20)
# Button(m,text="3.Currant Account",font="bold 15",border=5,bg="#000814",fg="white",command=curt).place(x=20,y=100)
# Button(m,text="4.Display Account",font="bold 15",border=5,bg="#000814",fg="white",command=disp).place(x=220,y=100)
# Button(m,text="5.Exit",font="bold 15",border=5,bg="#000814",fg="white",padx=5,pady=5,command=close).place(x=180,y=160)

m.mainloop()





