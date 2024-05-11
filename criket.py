from tkinter import *
import mysql.connector
a = Tk()
a.geometry("500x500")
a.title("contact Book")

con=mysql.connector.connect(host="localhost" , user="root" , password="" , database="system")

cur = con.cursor()


def total():
    name =  s1.get()
    m1 = s2.get()
    m2 = s3.get()
    m3 = s4.get()
    m4 = s5.get()
    m5 = s6.get()


    name = str(name)
    m1 = int(m1)
    m2 = int(m2)
    m3 =int(m3)
    m4= int(m4)
    m5 = int(m5)

    total = m1+m2+m3+m4+m5
    # l7.config(text = total)

    per = total/5
    # l8.config(text= per)

    min_val = min(m1,m2,m3,m4,m5)
    # l9.config(text = min_val)

    max_val = max(m1,m2,m3,m4,m5)
    # l10.config(text = max_val)


    call(name,m1,m2,m3,m4,m5,total,per,min_val,max_val)

def call(name,m1,m2,m3,m4,m5,total,per,min_val,max_val):
    sql = "insert into cricket(name,m1,m2,m3,m4,m5,total,per,min,max) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,(name,m1,m2,m3,m4,m5,total,per,min_val,max_val))
    con.commit()
    # con.close()

def Select():
    sql = "SELECT * FROM `cricket`"
    cur.execute(sql)
    rows = cur.fetchall()
    i=10
    for row in rows:
        j=0
        for data in row:
            lbl = Label(a,text=data)
            lbl.grid(row=i,column=j)
            j+=1
        i+=1
    print(rows)
Select()

# def update():
#     sql = "UPDATE `cricket` SET `name`='%s',`m1`='%s',`m2`='%s',`m3`='%s',`m4`='%s',`m5`='%s' WHERE 1"
#     cur.execute(sql)
#     con.commit()
# update()

def delete():
    sql = "DELETE FROM `cricket` "
    cur.execute(sql)
    con.commit()
delete()



# b1 = Label(a,text="Total")
# b1.grid(row=7,column=0)
# l7 = Label(a,text="")
# l7.grid(row=7,column=1)

# b2 = Label(a,text="Avrage")
# b2.grid(row=8,column=0)
# l8 = Label(a,text="")
# l8.grid(row=8,column=1)

# b3 = Label(a,text="Min")
# b3.grid(row=9,column=0)
# l9 = Label(a,text="")
# l9.grid(row=9,column=1)

# b4 = Label(a,text="max")
# b4.grid(row=10,column=0)
# l10 = Label(a,text="")
# l10.grid(row=10,column=1)




l1 = Label(a,text="Enter Name = ")
l1.grid(row=0,column=0)
s1 = Entry()
s1.grid(row=0,column=1)

l2 = Label(a,text="Enter M1 = ")
l2.grid(row=1,column=0)
s2 = Entry()
s2.grid(row=1,column=1)

l3 = Label(a,text="Enter M2 = ")
l3.grid(row=2,column=0)
s3 = Entry()
s3.grid(row=2,column=1)

l4 = Label(a,text="Enter M3 = ")
l4.grid(row=3,column=0)
s4 = Entry()
s4.grid(row=3,column=1)


l5 = Label(a,text="Enter M4 = ")
l5.grid(row=4,column=0)
s5 = Entry()
s5.grid(row=4,column=1)

l6 = Label(a,text="Enter M5 = ")
l6.grid(row=5,column=0)
s6 = Entry()
s6.grid(row=5,column=1)


done = Button(a,text="Done",command=total)
done.grid(row=6,column=1)

sel = Button(a,text="Show",command=Select)
sel.grid(row=7,column=1)

# up = Button(a,text="Update",command=update)
# up.grid(row=8,column=1)

de = Button(a,text="Delete",command=delete)
de.grid(row=9,column=1)
a.mainloop()




# def cal():
#     name=d_name.get()
#     number=d_number.get()
#     email=d_email.get()
#     submit(name,number,email)

# def submit(name,number,email):
#     sql = "insert into contact(name,number,email) values (%s,%s,%s)"
#     cur.execute(sql,(name,number,email))
#     con.commit()
#     a.destroy()
    
    
   

# name=Label(a,text="Contact Book")
# name.grid(row=1, column=1)
# name=Label(a,text="Name")
# name.grid(row=2, column=1)
# number=Label(a,text="Phone Number")
# number.grid(row=3, column=1)
# email=Label(a,text="Email")
# email.grid(row=4, column=1)



# d_name = Entry()
# d_name.grid(row= 2 , column=2)
# d_number = Entry()
# d_number.grid(row=3 , column=2)
# d_email = Entry()
# d_email.grid(row=4 , column=2)

# b=Button(a,text="Submit Hear" , command=cal)
# b.grid(row= 5 , column= 2)
# a.mainloop()







