from Tkinter import *
import ttk


def chg():
    frm1.tkraise()


root = Tk()
root.minsize(width=1500, height=850)
# root.withdraw()
#number = root.clipboard_get()

frm1 = Frame(root,height=850,width=1500)
btn1 = Button(frm1,text="vignesh")
btn1.pack()

#frm1.pack(fill="both",side="top")
frm1.rowconfigure(0,weight=1)
frm1.columnconfigure(0,weight=1)

frm2 = Frame(root, height=850,width=1500)
btn2 = Button(frm2, text="chaitu")
btn2.place(x=10, y=20)

btnch = Button(frm2,text="change",command=chg)
btnch.place(x=60,y=20)
#frm2.pack(fill="both",side="top")



frm2.grid(row=0,column=0,sticky="NSEW")
frm1.grid(row=0,column=0,sticky="NSEW")

root.mainloop()