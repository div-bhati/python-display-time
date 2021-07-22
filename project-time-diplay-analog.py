from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("<----Enter What You Wanted To Call This Clock App---->")
#root.title is a field in which you have to place the name for your app. 

def time():
    string =strftime("Proudly made with Python "+'%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 50) ,background = "black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()
