from tkinter import * 
m=Tk()
m.title("Number Puzzle")
m.geometry("350x390")

def click(num):
    if num == 1:
        if b2.cget("text") == "":
            b2.config(text=b1.cget("text"))
            b1.config(text="")
    if num == 2:
        if b1.cget("text") == "":
            b1.config(text=b2.cget("text"))
            b2.config(text="")
        elif b3.cget("text") ==  "":
            b3.config(text=b2.cget("text"))
            b2.config(text="")
    if num == 3:
        if b2.cget("text") == "":
            b2.config(text=b3.cget("text"))
            b3.config(text="")

    if num == 4:
        if b5.cget("text") == "":
            b5.config(text=b4.cget("text"))
            b4.config(text="")
    if num == 5:
        if b4.cget("text") == "":
            b4.config(text=b5.cget("text"))
            b5.config(text="")
        elif b6.cget("text") ==  "":
            b6.config(text=b5.cget("text"))
            b5.config(text="")
    if num == 6:
        if b5.cget("text") == "":
            b5.config(text=b6.cget("text"))
            b6.config(text="")

    if num == 7:
        if b8.cget("text") == "":
            b8.config(text=b7.cget("text"))
            b7.config(text="")
    if num == 8:
        if b7.cget("text") == "":
            b7.config(text=b8.cget("text"))
            b8.config(text="")
        elif b9.cget("text") ==  "":
            b9.config(text=b8.cget("text"))
            b8.config(text="")
    if num == 9:
        if b8.cget("text") == "":
            b8.config(text=b9.cget("text"))
            b9.config(text="")
    

       

b1 = Button(m,text="1",padx=50,pady=50,command=lambda:click(1))
b1.place(x=0,y=0)

b2 = Button(m,text="2",padx=50,pady=50,command=lambda:click(2))
b2.place(x=120,y=0)

b3 = Button(m,text="3",padx=50,pady=50,command=lambda:click(3))
b3.place(x=240,y=0)

b4 = Button(m,text="4",padx=50,pady=50,command=lambda:click(4))
b4.place(x=0,y=130)

b5 = Button(m,text="5",padx=50,pady=50,command=lambda:click(5))
b5.place(x=120,y=130)

b6 = Button(m,text="6",padx=50,pady=50,command=lambda:click(6))
b6.place(x=240,y=130)

b7 = Button(m,text="7",padx=50,pady=50,command=lambda:click(7))
b7.place(x=0,y=260)

b8 = Button(m,text="8",padx=50,pady=50,command=lambda:click(8))
b8.place(x=120,y=260)

b9 = Button(m,text="",padx=50,pady=50,command=lambda:click(9))
b9.place(x=240,y=260)




m.mainloop()

