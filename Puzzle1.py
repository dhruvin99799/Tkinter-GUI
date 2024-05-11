from tkinter import *
from tkinter import font
import random

m = Tk()
m.title('Number puzzle')
m.grid()


b = [0,1,2,3,4,5,6,7,8]

index = [1,'',2,3,4,5,6,7,8]
random.shuffle(index)

b[0] = Button(m,text=index[0],height=4,width=10,command=lambda:transfer(0))
b[1] = Button(m,text=index[1],height=4,width=10,command=lambda:transfer(1))
b[2] = Button(m,text=index[2],height=4,width=10,command=lambda:transfer(2))
b[3] = Button(m,text=index[3],height=4,width=10,command=lambda:transfer(3))
b[4] = Button(m,text=index[4],height=4,width=10,command=lambda:transfer(4))
b[5] = Button(m,text=index[5],height=4,width=10,command=lambda:transfer(5))
b[6] = Button(m,text=index[6],height=4,width=10,command=lambda:transfer(6))
b[7] = Button(m,text=index[7],height=4,width=10,command=lambda:transfer(7))
b[8] = Button(m,text=index[8],height=4,width=10,command=lambda:transfer(8))

b[0].grid(row=0,column=0)
b[1].grid(row=0,column=1)
b[2].grid(row=0,column=2)
b[3].grid(row=1,column=0)
b[4].grid(row=1,column=1)
b[5].grid(row=1,column=2)
b[6].grid(row=2,column=0)
b[7].grid(row=2,column=1)
b[8].grid(row=2,column=2)

def transfer(btn):
    if b[btn].cget('text') != '':
        if btn == 0:
            if b[1].cget('text') == '':
                b[1].config(text=b[0].cget('text'))
                b[0].config(text='')
                call()
            elif b[3].cget('text') == '':
                b[3].config(text=b[0].cget('text'))
                b[0].config(text='')
                call()
        elif btn == 2:
            if b[1].cget('text') == '':
                b[1].config(text=b[2].cget('text'))
                b[2].config(text='')
                call()
            elif b[5].cget('text') == '':
                b[5].config(text=b[2].cget('text'))
                b[2].config(text='')
                call()
        elif btn == 6:
            if b[3].cget('text') == '':
                b[3].config(text=b[6].cget('text'))
                b[6].config(text='')
                call()
            elif b[7].cget('text') == '':
                b[7].config(text=b[6].cget('text'))
                b[6].config(text='')
                call()
        elif btn == 8:
            if b[5].cget('text') == '':
                b[5].config(text=b[8].cget('text'))
                b[8].config(text='')
                call()
            elif b[7].cget('text') == '':
                b[7].config(text=b[8].cget('text'))
                b[8].config(text='')
                call()
        elif btn == 1:
            if b[0].cget('text') == '':
                b[0].config(text=b[1].cget('text'))
                b[1].config(text='')
                call()
            elif b[2].cget('text') == '':
                b[2].config(text=b[1].cget('text'))
                b[1].config(text='')
                call()
            elif b[4].cget('text') == '':
                b[4].config(text=b[1].cget('text'))
                b[1].config(text='')
                call()
        elif btn == 3:
            if b[0].cget('text') == '':
                b[0].config(text=b[3].cget('text'))
                b[3].config(text='')
                call()
            elif b[4].cget('text') == '':
                b[4].config(text=b[3].cget('text'))
                b[3].config(text='')
                call()
            elif b[6].cget('text') == '':
                b[6].config(text=b[3].cget('text'))
                b[3].config(text='')
                call()
        elif btn == 7:
            if b[8].cget('text') == '':
                b[8].config(text=b[7].cget('text'))
                b[7].config(text='')
                call()
            elif b[4].cget('text') == '':
                b[4].config(text=b[7].cget('text'))
                b[7].config(text='')
                call()
            elif b[6].cget('text') == '':
                b[6].config(text=b[7].cget('text'))
                b[7].config(text='')
                call()
        elif btn == 5:
            if b[2].cget('text') == '':
                b[2].config(text=b[5].cget('text'))
                b[5].config(text='')
                call()
            elif b[4].cget('text') == '':
                b[4].config(text=b[5].cget('text'))
                b[5].config(text='')
                call()
            elif b[8].cget('text') == '':
                b[8].config(text=b[5].cget('text'))
                b[5].config(text='')
                call()
        elif btn == 4:
            if b[1].cget('text') == '':
                b[1].config(text=b[4].cget('text'))
                b[4].config(text='')
                call()
            elif b[5].cget('text') == '':
                b[5].config(text=b[4].cget('text'))
                b[4].config(text='')
                call()
            elif b[3].cget('text') == '':
                b[3].config(text=b[4].cget('text'))
                b[4].config(text='')
                call()
            elif b[7].cget('text') == '':
                b[7].config(text=b[4].cget('text'))
                b[4].config(text='')
                call()

a1 = font.Font(m,size=30)
a2 = Label(m,text='',font=a1)
a2.grid(row=3,column=0,columnspan=3)

def call():
    if b[0].cget('text') == '' and b[1].cget('text') == 1 and b[2].cget('text') == 2 and b[3].cget('text') == 3 and b[4].cget('text') == 4 and b[5].cget('text') == 5 and b[6].cget('text') == 6 and b[7].cget('text') == 7 and b[8].cget('text') == 8:
        a2.config(text='Winnner !',fg='green')
        m.geometry('240x262')
    else:
        a2.config(text='')
        m.geometry('240x214')

m.mainloop()