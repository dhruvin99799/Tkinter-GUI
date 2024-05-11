from tkinter import *
import mysql.connector
m = Tk()
m.title("Student Result")
m.geometry("500x500")
con = mysql.connector.connect(host="localhost",user="root",password="",database="demo1")
cur=con.cursor()
def call():
    name = e_name.get()
    s1 = e1.get()
    s2 = e2.get()
    s3 = e3.get()
    s4 = e4.get()
    s5 = e5.get()

    name = str(name)
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)
    s4 = int(s4)
    s5 = int(s5)


    total = s1+s2+s3+s4+s5
    
    mi = str(min(s1,s2,s3,s4,s5))
    ma = str(max(s1,s2,s3,s4,s5))
    per = total/5

    if(per>35):
        result = "Pass"
    else:
        result = "Fail"


    if(per>90):
        grade = "A"
    elif(per>80):
        grade = "B"
    elif(per>70):
        grade = "C1"
    elif(per>60):
        grade = "C"
    elif(per>50):
        grade = "D1"
    elif(per>35):
        grade = "D"
    else:
        grade = "****"

    submit(name,s1,s2,s3,s4,s5,total,mi,ma,per,result,grade)

def submit(name,s1,s2,s3,s4,s5,total,mi,ma,per,result,grade):
    sql  =  "insert into demo(name,s1,s2,s3,s4,s5,total,mi,ma,per,result,grade) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,(name,s1,s2,s3,s4,s5,total,mi,ma,per,result,grade)) 
    con.commit()
    # m.destroy()

def edit_data(id):
    print(id)
    e1.delete(0,END)
    e1.insert(0,id)
    
   

def select():
    sql = "SELECT * FROM `demo`"
    cur.execute(sql)
    rows = cur.fetchall()
    i=10
    for row in rows:
        j=0
        for data in row:
            lbl = Label(m,text=data)
            lbl.grid(row=i,column=j)
            j+=1
        b = Button(m,text="Edit",command=lambda temp_id = row[0]:edit_data(temp_id))
        b.grid(row=i,column=j+1)
        i+=1
    print(rows)
select()


# def del_data(id):
#     print(id)
# def delete():
#     sql="DELETE FROM `demo`"
#     cur.execute(sql)
#     con.commit()
#     rows = cur.fetchall()
#     i=10
#     for row in rows:
#         j=0
#         for data in row:
#             lbl = Label(m,text=data)
#             lbl.grid(row=i,column=j)
#             j+=1
#         b = Button(m,text="Edit",command=lambda temp_id = row[0]:del_data(temp_id))
#         b.grid(row=i,column=j+1)
#         i+=1
#     print(rows)
# delete()




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
   
button = Button(text="Submit",command=call)
button.grid(row=7,column=1)

button = Button(text="Show",command=select)
button.grid(row=7,column=2)

# button = Button(text="Delete",command=delete)
# button.grid(row=7,column=3)


m.mainloop()