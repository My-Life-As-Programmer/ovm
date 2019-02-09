from Tkinter import *
import ttk
import requests
# def chg():
#    frm1.tkraise()

'''
def show_connect_frm():
    try:
        ip = ip_val.get()
        usr = unm_val.get()
        pwd = pw_val.get()
        r = requests.get('https://' + ip + ':7002/ovm/core/wsapi/rest/', auth=(usr, pwd))
        connect_frm.tkraise()
    except Exception:
        #error_frm.tkraise()
        connect_frm.tkraise()


def show_login_form():#(self):
    #self.login_frm.tkraise()
    login_frm.tkraise()

def show_repo_frm():#(self):
    #self.repo_frm.tkraise()
    error_frm.tkraise()


def show_serv_frm():  # (self):
    # self.repo_frm.tkraise()
    error_frm.tkraise()

'''





'''
frm1 = Frame(root,height="120",width="120")
btn1 = Button(frm1,text="vignesh")
btn1.pack()

#frm1.pack(fill="both",side="top")
frm1.rowconfigure(0,weight=1)
frm1.columnconfigure(0,weight=1)

frm2 = Frame(root, height="120",width="120")
btn2 = Button(frm2,text="chaitu")
btn2.pack()

btnch = Button(frm2,text="change",command=chg)
btnch.pack()
#frm2.pack(fill="both",side="top")


frm1.grid(row=0,column=0,sticky="NSEW")
frm2.grid(row=0,column=0,sticky="NSEW")
'''


'''  login frame 
login_frm = Frame(root, height=850, width=1500)
connect_frm = Frame(root, height=850, width=1500)
error_frm = Frame(root, height=850, width=1500)

disp = ttk.Label(login_frm, text="Welcome, enter the details to connect to the OVM ", font=("Verdana", 20))

disp.place(x=700, y=25, anchor="center")

ip_lbl = ttk.Label(login_frm, text="IP address :", font=("Verdana", 15))
unm_lbl = ttk.Label(login_frm, text="Username :", font=("Verdana", 15))
pw_lbl = ttk.Label(login_frm, text="Password :", font=("Verdana", 15))

ip_lbl.place(x=600, y=200, anchor="center")             # 100
unm_lbl.place(x=600, y=250, anchor="center")            # 125
pw_lbl.place(x=600, y=300, anchor="center")             # 150

ip_val = Entry(login_frm, width=25)
unm_val = Entry(login_frm, width=25)
pw_val = Entry(login_frm, width=25)

ip_val.place(x=800, y=205, anchor="center")             # 100
unm_val.place(x=800, y=255, anchor="center")            # 125
pw_val.place(x=800, y=305, anchor="center")             # 150


login_btn = ttk.Button(login_frm, width=30, text="Log In", command=show_connect_frm)

login_btn.place(x=800, y=405, anchor="center")

login_frm.rowconfigure(0, weight=1)
login_frm.columnconfigure(0, weight=1)

show_lbl = ttk.Label(connect_frm, text="Successfully Connected", font=("Verdana", 20), foreground="dark green")
show_lbl.place(x=700, y=250, anchor="center")

con_repo = ttk.Button(connect_frm, width=30, text="Repositories", command=show_repo_frm)
con_serv = ttk.Button(connect_frm, width=30, text="Servers", command=show_serv_frm)

con_repo.place(x=600, y=350, anchor="center")
con_serv.place(x=800, y=350, anchor="center")






connect_frm.rowconfigure(0, weight=1)
connect_frm.columnconfigure(0, weight=1)


err_lbl = ttk.Label(error_frm, text="Error Connecting OVM , please check the details and Try again ...",
                    font=("Verdana",20), foreground="red")
err_lbl.place(x=700, y=250, anchor="center")
err_go_back = ttk.Button(error_frm, width=30, text="Try Again", command=show_login_form)
err_go_back.place(x=700, y=350, anchor="center")


error_frm.grid(row=0, column=0, sticky="NSEW")
connect_frm.grid(row=0, column=0, sticky="NSEW")
login_frm.grid(row=0, column=0, sticky="NSEW")
login_frm.tkraise()
'''


def test(s):
    print s

root = Tk()
root.minsize(width=1500, height=850)
# root.withdraw()
# number = root.clipboard_get()
serv_frm = Frame(root, height=850, width=1500)
vm_frm = Frame(serv_frm, height=100, width=1500)
vm_dtl_frm = Frame(root, height=850, width=1500)

but = ttk.Button(serv_frm, text="click me", command=lambda:test("chaitu"))
but.pack()
serv_frm.pack()
root.mainloop()
# print number
