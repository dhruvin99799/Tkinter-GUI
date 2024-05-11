from tkinter import *
m = Tk()
m.geometry("500x500")
m.title("Tic Tac TOe")

frame1 = Frame(m)
frame1.pack()
titlelabel = Label(frame1 , text="Tic Tac Toe" , font=("arial", 30), bg="black", fg="white")
titlelabel.pack()

frame2 = Frame(m)
frame2.pack()

turn = "x"

def play(event):
    global turn
    button = event.widget
    if turn =="x":
        button["text"] = "X"
        turn = "o"
    else:
        button["text"] = "O"
        turn = "x"

button1 = Button(frame2, text=" ", width=4, height=2 , font=("arial",30), bg="blue",fg="white",relief=RAISED,borderwidth=5)
button1.grid(row=0 , column=0)
button1.bind("<Button-1>",play)

button1 = Button(frame2, text=" ", width=4, height=2 , font=("arial",30), bg="blue",fg="white",relief=RAISED,borderwidth=5)
button1.grid(row=0 , column=1)
button1.bind("<Button-1>",play)


button1 = Button(frame2, text=" ", width=4, height=2 , font=("arial",30), bg="blue",fg="white",relief=RAISED,borderwidth=5)
button1.grid(row=0 , column=2)
button1.bind("<Button-1>",play)



button1 = Button(frame2, text=" ", width=4, height=2 , font=("arial",30), bg="blue",fg="white",relief=RAISED,borderwidth=5)
button1.grid(row=1 , column=0)
button1.bind("<Button-1>",play)


button1 = Button(frame2, text=" ", width=4, height=2 , font=("arial",30), bg="blue",fg="white",relief=RAISED,borderwidth=5)
button1.grid(row=1 , column=1)
button1.bind("<Button-1>",play)


button1 = Button(frame2, text=" ", width=4, height=2 , font=("arial",30), bg="blue",fg="white",relief=RAISED,borderwidth=5)
button1.grid(row=1 , column=2)
button1.bind("<Button-1>",play)



button1 = Button(frame2, text=" ", width=4, height=2 , font=("arial",30), bg="blue",fg="white",relief=RAISED,borderwidth=5)
button1.grid(row=2 , column=0)
button1.bind("<Button-1>",play)


button1 = Button(frame2, text=" ", width=4, height=2 , font=("arial",30), bg="blue",fg="white",relief=RAISED,borderwidth=5)
button1.grid(row=2 , column=1)
button1.bind("<Button-1>",play)


button1 = Button(frame2, text=" ", width=4, height=2 , font=("arial",30), bg="blue",fg="white",relief=RAISED,borderwidth=5)
button1.grid(row=2 , column=2)
button1.bind("<Button-1>",play)




m.mainloop()