from Tkinter import *
import ttk

def chg():
    btn.config(text="hi")
    btn.pack()


root = Tk()

btn = ttk.Button(root,text="new button",command=chg)

btn.pack()

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Entry(root,text="<a>www.google.com</a>")
l1.config(text="hi")
l2 = ttk.Label(root,text="Test", style="BW.TLabel")

l1.pack()
l2.pack()

print l1.get()
root.mainloop()