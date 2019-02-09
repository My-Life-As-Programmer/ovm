from Tkinter import *
import time


root = Tk()
txt = Text(root, width=30, height=10)
def func():
    txt.grid_forget()

root.minsize(width=1500, height=850)


txt.insert(END, "hi")
txt.grid(row=0, column=0)

btn=Button(root,text="click",command=func)
btn.grid(row=1,column=1)


root.mainloop()
