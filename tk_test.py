from Tkinter import *

root = Tk()
root.title("OVM Status Report")
var= "Alex"

label = Label(root,text=var)

if len(var) > 5:
    label.config(bg="red")
else:
    label.config(bg="green")
label.grid(row=0,column=0)
root.mainloop()
