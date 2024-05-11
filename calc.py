from tkinter import *

m=Tk()
m.title("Calculater")
m.geometry("500x300")

def btnClick():
    ans = str(int(e1.get())+int(e2.get()))
    l3.config(text=ans)

def btnClick1():
    ans1 = str(int(e1.get())-int(e2.get()))
    l4.config(text=ans1)

def btnClick2():
    ans2 = str(int(e1.get())*int(e2.get()))
    l5.config(text=ans2)

def btnClick3():
    ans3 = str(int(e1.get())/int(e2.get()))
    l6.config(text=ans3)






l1 = Label(text="Value 1:")
l1.grid(row=0,column=0)

l2 = Label(text="Value 2:")
l2.grid(row=1,column=0)



l3 = Label(text="0")
l3.grid(row=2,column=0)

l4 = Label(text="0")
l4.grid(row=2,column=0)

l5 = Label(text="0")
l5.grid(row=2,column=0)

l6 = Label(text="0")
l6.grid(row=2,column=0)



e1 = Entry()
e1.grid(row=0,column=1)

e2 = Entry()
e2.grid(row=1,column=1)


b = Button(m,text="Sum",command=btnClick)
b.grid(row=2,column=1)

b = Button(m,text="Sub",command=btnClick1)
b.grid(row=2,column=2)

b = Button(m,text="Mul",command=btnClick2)
b.grid(row=2,column=3)

b = Button(m,text="Div",command=btnClick3)
b.grid(row=2,column=4)




m.mainloop()