import tkinter as tk
import tkinter.font as font
# customfont = font.font
m = tk.Tk()
m.title("Dhruvin Dhameliya")    



# # Pack Method



button = tk.Button(m,text="Press Me",font="Impact 10")
button.pack()
button = tk.Button(text="Press Me")
button.pack()
button = tk.Button(text="Press Me")
button.pack()

m.mainloop()




# # Grid Method 

# b = tk.Button(text="Click Here")
# b.grid(row=0,column=5)

# # Place Method
# # b = tk.Button(text="Hello I Am Here")
# # b.place(x=100,y=500)


# # Check Box
# master = tk()
# val1 = var()
# checkbutton(text="male",variable=var1)
# val2 = var()
# checkbutton(text="male",variable=var2)


# from tkinter import *
# master = Tk()
# var1 = IntVar()
# Checkbutton(master, text='male', variable=var1).grid(row=0)
# var2 = IntVar()
# Checkbutton(master, text='female', variable=var2).grid(row=1)
# mainloop()



# from tkinter import *
# master = Tk()
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()
