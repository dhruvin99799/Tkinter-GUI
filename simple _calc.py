# import tkinter
from tkinter import *

m = Tk()
m.title("Simple Calculator")
m.geometry("400x350+100+200")
m.resizable(False,False)
m.configure(bg="#17161b")

equation = ""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result="error"
            equation = ""
    label_result.config(text=result)


label_result = Label(m,width=40,height=2,text="", font=("arial"))
label_result.pack()

Button(m,text="C", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#202099",command=lambda: clear()).place(x=10,y=100)
Button(m,text="/", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("/")).place(x=100,y=100)
Button(m,text="%", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("%")).place(x=200,y=100)
Button(m,text="*", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("*")).place(x=300,y=100)

Button(m,text="7", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=150)
Button(m,text="8", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("8")).place(x=100,y=150)
Button(m,text="9", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("9")).place(x=200,y=150)
Button(m,text="-", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("-")).place(x=300,y=150)

Button(m,text="4", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=200)
Button(m,text="5", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("5")).place(x=100,y=200)
Button(m,text="6", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("6")).place(x=200,y=200)
Button(m,text="+", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("+")).place(x=300,y=200)

Button(m,text="1", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=250)
Button(m,text="2", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("2")).place(x=100,y=250)
Button(m,text="3", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("3")).place(x=200,y=250)
Button(m,text="0", width=13, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show("0")).place(x=10,y=300)

Button(m,text=".", width=5, height=1, font="arial", bd=1,fg="#fefae0",bg="#2a2d36",command=lambda: show(".")).place(x=200,y=300)
Button(m,text="=", width=5, height=3, font="arial", bd=1,fg="#fefae0",bg="#fe9037",command=lambda: calculate()).place(x=300,y=250)



m.mainloop()