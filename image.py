import tkinter as tk
from PIL import Image
from PIL import ImageTk
m = tk.Tk()
m.title("Dhruvin Dhameliya")

width = 500
height = 500
img = Image.open("photo/1.jpeg")
img = img.resize((width,height))
photoImg = ImageTk.PhotoImage(img)
b = tk.Button(m,image=photoImg)
b.pack()

m.mainloop()