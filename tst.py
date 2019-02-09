import requests
import ovmclient
from Tkinter import *
import ttk

ovm_ip='192.168.1.21'
baseUri = 'https://' + ovm_ip + ':7002/ovm/core/wsapi/rest'
uname = 'admin'
pwd = 'Hitachi123'

# client = ovmclient.Client(baseUri, uname, pwd)
'''
ssn = requests.Session()
ssn.auth = (usr, pwd)
ssn.verify = False  # disables SSL certificate verification
ssn.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json'})

r = ssn.get('https://' + ovm_ip + ':7002/ovm/core/wsapi/rest/')

'''
'''
for line in client.vms.get_all():
    print line
    print "\n"

'''



def showw():
    root = Tk()
    lst = {"hi": "hello", "sai": "chaitu", "f": "you"}

    r = 0
    for i in lst:
        btn = ttk.Button(root, text="click "+str(i), command=lambda sid=lst[i]: prints(sid))
        btn.grid(row=r,  column=r)
        r += 1
    # print i

    def prints(n):
        print n


    root.mainloop()

showw()