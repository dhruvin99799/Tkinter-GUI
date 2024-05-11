from tkinter import *
m = Tk()
m.geometry("500x500")
m.title("Bank")
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="system")
cur=con.cursor()

    

def openAcc(e_name,pho_n,ob_b,acno_n):
    name = Label(m,text="Name")
    name.place(x=0,y=50)
    e_name = Entry()
    e_name.place(x=50,y=50)

    pho = Label(m,text="Acno")
    pho.place(x=0,y=100)
    pho_n = Entry()
    pho_n.place(x=50,y=100)

    ob = Label(m,text="Opning Balance")
    ob.place(x=0,y=150)
    ob_b = Entry()
    ob_b.place(x=100,y=150)
    
    acno = Label(m,text="Account Number")
    acno.place(x=0,y=200)
    acno_n = Entry()
    acno_n.place(x=100,y=200)

    
    # print("Data Entered Successfully")
    Button(m,text="Submit",padx=10,pady=10,command=openAcc).place(x=100,y=250)
    
Button(m,text="Insert",padx=10,pady=10,command=openAcc).place(x=0,y=0)




m.mainloop()