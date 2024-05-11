from tkinter import *
m = Tk()
m.title("Bank System")
m.geometry("300x300")
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="bank")
cur=con.cursor()



b_name = Entry()
ac_no = Entry()
mb_num = Entry()
pass_word = Entry()

def call():
    name = b_name.get()
    acno = ac_no.get()
    mb = mb_num.get()
     
    submit(name,acno,mb)

def submit(name,acno,mb):
    sql  =  "insert into data(name,acno,mb) values(%s,%s,%s)"
    cur.execute(sql,(name,acno,mb))
    con.commit()
    m.destroy()





create = Label(m,text="1.Create Account.").place(x=20,y=10)
saving = Label(m,text="2.Saving Account.").place(x=20,y=30)
currant = Label(m,text="3.Current Account.").place(x=20,y=50)
inqury = Label(m,text="4.Balance Inquiry.").place(x=20,y=70)
exit = Label(m,text="5.Exit").place(x=20,y=90)

choice =Label(m,text="Enter Your Choice")
choice.place(x=20,y=120)
choice_e = Entry()
choice_e.place(x=150,y=120)



button = Button(m,text="Submit",font="bold 10",padx=5,pady=5,bg="blue",fg="white",command=call).place(x=200,y=150)


m.mainloop()


master = Tk()
master.geometry("400x400")

# def all():
#     name = Label(master,text="Name")
#     name.place(x=20,y=200)
#     b_name = Entry()
#     b_name.place(x=150,y=200)

#     acno = Label(master,text="Account Number")
#     acno.place(x=20,y=230)
#     ac_no = Entry()
#     ac_no.place(x=150,y=230)

#     mb = Label(master,text="Phone Number")
#     mb.place(x=20,y=260)
#     mb_num = Entry()
#     mb_num.place(x=150,y=260)

#     password = Label(master,text="Enter Your Password")
#     password.place(x=20,y=290)
#     pass_word = Entry()
#     pass_word.place(x=150,y=290)

# def some():
#     name = Label(master,text="Name")
#     name.place(x=20,y=200)
#     b_name = Entry()
#     b_name.place(x=150,y=200)


#     mb = Label(master,text="Phone Number")
#     mb.place(x=20,y=260)
#     mb_num = Entry()
#     mb_num.place(x=150,y=260)

# def inq():
#     acno = Label(master,text="Account Number")
#     acno.place(x=20,y=230)
#     ac_no = Entry()
#     ac_no.place(x=150,y=230)

#     password = Label(master,text="Enter Your Password")
#     password.place(x=20,y=290)
#     pass_word = Entry()
#     pass_word.place(x=150,y=290)

while choice!=0:
    if(choice == '1'):
        name = Label(master,text="Name")
        name.place(x=20,y=30)
        b_name = Entry()
        b_name.place(x=150,y=30)


        mb = Label(master,text="Phone Number")
        mb.place(x=20,y=60)
        mb_num = Entry()
        mb_num.place(x=150,y=60)

    elif(choice == '2'):
        name = Label(master,text="Name")
        name.place(x=20,y=30)
        b_name = Entry()
        b_name.place(x=150,y=30)

        acno = Label(master,text="Account Number")
        acno.place(x=20,y=60)
        ac_no = Entry()
        ac_no.place(x=150,y=60)

        mb = Label(master,text="Phone Number")
        mb.place(x=20,y=90)
        mb_num = Entry()
        mb_num.place(x=150,y=90)

        password = Label(master,text="Enter Your Password")
        password.place(x=20,y=120)
        pass_word = Entry()
        pass_word.place(x=150,y=120)

    elif(choice == '3'):
        name = Label(master,text="Name")
        name.place(x=20,y=30)
        b_name = Entry()
        b_name.place(x=150,y=30)

        acno = Label(master,text="Account Number")
        acno.place(x=20,y=60)
        ac_no = Entry()
        ac_no.place(x=150,y=60)

        mb = Label(master,text="Phone Number")
        mb.place(x=20,y=90)
        mb_num = Entry()
        mb_num.place(x=150,y=90)

        password = Label(master,text="Enter Your Password")
        password.place(x=20,y=120)
        pass_word = Entry()
        pass_word.place(x=150,y=120)
    elif(choice == '4'):
        acno = Label(master,text="Account Number")
        acno.place(x=20,y=30)
        ac_no = Entry()
        ac_no.place(x=150,y=30)

        password = Label(master,text="Enter Your Password")
        password.place(x=20,y=60)
        pass_word = Entry()
        pass_word.place(x=150,y=60)
    elif(choice == '5'):
        exit()

master.mainloop()

# import tkinter
# from tkinter import *
# import mysql.connector

# con = mysql.connector.connect(host="localhost", user="root", password="", database="system")
# cur = con.cursor()

# m = tkinter.Tk()
# m.geometry("1250x650")
# m.title("Student Mangment System")
# m.resizable(0, 0)


# Label(m, text="Bank Management System", fg="white", bg="#00008B", width=1200, height=0).pack()


# class btnclick():
#     def __init__(self):
#         ans = str(s1.get())
#         name_disp = str(s2.get())
#         class_disp = str(s3.get())
#         mobile_disp = str(s4.get())
#         pay_amt = str(s5.get())

#         e1.config(text=ans)
#         e2.config(text=name_disp)
#         e3.config(text=class_disp)
#         e4.config(text=mobile_disp)
#         e5.config(text=pay_amt)
        

#         sql = "INSERT INTO bank(`acc`, `name`, `acc_type`,`mobie`, `pay_amt`) VALUES (%s,%s,%s,%s,%s)"
#         cur.execute(sql, (ans, name_disp, class_disp, mobile_disp, pay_amt))
#         con.commit()

# def select():
#     sql = "SELECT * FROM `bank`"
#     cur.execute(sql)
#     rows = cur.fetchall()
#     # i=5
#     # for row in rows:
#     #     j=0
#     #     for data in row:
#     #         lbl =  Label(m,text=data)
#     #         lbl.grid(row=i,column=j)
#     #         j+=1
#     #     i+=1
#     print(rows)
# select()

        


# one_box = Frame(m, bg="#ADD8E6", width=420, height=550).place(x=20, y=60)
# two_box = Frame(m, bg="#ADD8E6", width=765, height=550).place(x=460, y=60)

# # ----------manage student---------

# Label(m, text="Bank Management", fg="black", bg="#ADD8E6").place(x=150, y=70)

# acc = tkinter.Label(m, text="Account No",  bg="#ADD8E6")
# acc.place(x=40, y=120)
# s1 = Entry(m, width=35)
# s1.place(x=150, y=120)

# name = tkinter.Label(m, text="Name", bg="#ADD8E6")
# name.place(x=40, y=160)
# s2 = Entry(m, width=35)
# s2.place(x=150, y=160)

# acc_type = tkinter.Label(m, text="Acc Type", bg="#ADD8E6")
# acc_type.place(x=40, y=200)
# s3 = Entry(m, width=35)
# s3.place(x=150, y=200)


# mobie = tkinter.Label(m, text="Mobie", bg="#ADD8E6")
# mobie.place(x=40, y=320)
# s4 = Entry(m, width=35)
# s4.place(x=150, y=320)

# pay_amt = tkinter.Label(m, text="pay Amount", bg="#ADD8E6")
# pay_amt.place(x=40, y=360)
# s5 = Entry(m, width=35)
# s5.place(x=150, y=360)


# btn = tkinter.Button(m, text="Submit", height=1, width=10, activebackground="green", command=btnclick)
# btn.place(x=200, y=450)
# btn1 = tkinter.Button(m, text="Select", height=1, width=10, activebackground="green", command=select)
# btn1.place(x=300,y=450)

# # -----Set name as line-------

# a1 = tkinter.Button(m, text="Ac No")
# a1.place(x=460, y=60, width=80)
# a2 = tkinter.Button(m, text="Name")
# a2.place(x=540, y=60, width=180)
# a3 = tkinter.Button(m, text="Ac Type")
# a3.place(x=720, y=60, width=80)
# a4 = tkinter.Button(m, text="Mobile No")
# a4.place(x=800, y=60, width=90)
# a5 = tkinter.Button(m, text="Pay Amount")
# a5.place(x=890, y=60, width=90)


# # show details for student when submit

# e1 = Label(m, text="0")
# e1.place(x=460, y=85, width=80)
# e2 = Label(m, text="0")
# e2.place(x=540, y=85, width=180)
# e3 = Label(m, text="0")
# e3.place(x=720, y=85, width=80)
# e4 = Label(m, text="0")
# e4.place(x=800, y=85, width=80)
# e5 = Label(m, text="0")
# e5.place(x=880, y=85, width=80)


# # select query 

# # sel_data = Entry(m)
# # sel_data.place(x=800,y=300)

# obj = btnclick()

# m.mainloop()