import ovmclient
from Tkinter import *
import requests
import ttk

'''
server_pool
    servers
        vms

    repo


'''

# common info
#ovm_ip = '192.168.1.21'
ovm_ip = "172.23.36.245"
baseUri = 'https://' + ovm_ip + ':7002/ovm/core/wsapi/rest'
uname = 'admin'
pwd = 'Hitachi123'
hd = {'Accept': 'application/json', 'Content-Type': 'application/json'}


# using ovmclient
client = ovmclient.Client(baseUri, uname, pwd)

# JSON support
s = requests.Session()
s.auth = (uname, pwd)
s.verify = False  # disables SSL certificate verification
s.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json'})

# baseUri='https://192.168.1.21:7002/ovm/core/wsapi/rest'


# GUI info
root = Tk()
root.title("OVM Status Report")
root.minsize(width=1500, height=850)
# root.maxsize(width=666, height=666)
repo_frm = Frame(root,height="850", width="1500")
serv_frm = Frame(root,height="850", width="1500")
login_frm = Frame(root, height=850, width=1500)
connect_frm = Frame(root, height=850, width=1500)
error_frm = Frame(root, height=850, width=1500)

#font_style = ttk.style()
#font_style.config(font=("Verdana", 16))

def check_manager_state(baseUri, s):
    while True:
        r = s.get(baseUri + '/Manager')
        manager = r.json()
        if manager[0]['managerRunState'].upper() == 'RUNNING':
            return "OVM Manager is Running  ...... \n\n\n"
            time.sleep(1)
        else:
            return


print check_manager_state(baseUri, s)

'''
def servers():
    r=s.get(baseUri+'/Server')
    for i in r.json():
        # do something with the content
        print(i)
        print '{name} is {state}'.format(name=i['name'], state=i['serverRunState'])
'''


def show_repo(repo):
    # print "Repo details"
    repo_lbl = ttk.Label(repo_frm, text="Repo details", font=("Verdana", 20), background="cyan")
    repo_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
    tsz_lbl = ttk.Label(repo_frm, text="Total Size", font=("Verdana", 20), background="cyan")
    fsz_lbl = ttk.Label(repo_frm, text="Free Size", font=("Verdana", 20), background="cyan")
    usz_lbl = ttk.Label(repo_frm, text="Used Size", font=("Verdana", 20), background="cyan")
    tsz_lbl.grid(row=0, column=1, padx=20, pady=20, sticky="NSEW")
    fsz_lbl.grid(row=0, column=3, padx=20, pady=20, sticky="NSEW")
    usz_lbl.grid(row=0, column=2, padx=20, pady=20, sticky="NSEW")

    rw = 2
    tmp_lbl = ttk.Label(repo_frm,text=" ")

    for line in repo:
        # print line["name"]
        name = line["name"]
        ids = line["id"]
        #        r = requests.get(ids["uri"], auth=('admin', 'Hitachi123'), json=True, verify=False)
        fsid = line["fileSystemId"]
        r = requests.get(fsid["uri"], auth=('admin', 'Hitachi123'), json=True, verify=False, headers=hd)
        data = r.json()
        total_size_raw = int(data["size"])
        total_size_gb = total_size_raw / (1024 ** 3)
        used_space_raw = int(data["freeSize"])
        used_space_gb = used_space_raw / (1024 ** 3)
        # print "total size of repo is " + str(total_size_gb) + "GB"
        # print "free size of repo is " + str(used_space_gb) + "GB"
        # print "used space of repo is " + str(total_size_gb - used_space_gb) + "GB"
        # print '\n'
        u_size = total_size_gb - used_space_gb
        ttl_size = str(total_size_gb) + "GB"
        free_size = str(used_space_gb) + "GB"
        used_size = str(u_size) + "GB"
        nm_lbl = ttk.Label(repo_frm, text=name, font=("Verdana", 16), background="cyan", padding=2)
        ttl_sz_lbl = ttk.Label(repo_frm, text=ttl_size, font=("Verdana", 16), padding=2)
        fr_sz_lbl = ttk.Label(repo_frm, text=free_size, font=("Verdana", 16), padding=2)
        usd_sz_lbl = ttk.Label(repo_frm, text=used_size, font=("Verdana", 16), padding=2)
        if u_size > 0.8 * total_size_gb:
            usd_sz_lbl.config(background="red")
            fr_sz_lbl.config(background="red")
            ttl_sz_lbl.config(background="red")
        else:
            usd_sz_lbl.config(background="green")
            fr_sz_lbl.config(background="green")
            ttl_sz_lbl.config(background="green")
        nm_lbl.grid(row=rw, column=0, sticky="NSEW", padx=10)
        tmp_lbl.grid(row=rw-1, column=1)
        ttl_sz_lbl.grid(row=rw, column=1, padx=10, pady=10, sticky="NSEW")
        fr_sz_lbl.grid(row=rw, column=3, padx=10, pady=10, sticky="NSEW")
        usd_sz_lbl.grid(row=rw, column=2, padx=10, pady=10, sticky="NSEW")
        rw += 2
    repo_frm.pack()


def show_server_pools(spool):
    for line in spool:
        if line["name"]:
            print "Server Pool : " + line["name"] + "\nServers:\n"
        else:
            print "Server Pool : " + line["value"] + "\nServers:\n"
        servers(line)
    return


'''
def servers(serverpool):
    serv = client.servers.get_all();
    for line in serv:
        if line["serverPoolId"] == serverpool:
            print line["name"]
            print line["id"]
            uri
         #   show_vms(line)
        #print line
    print "\n"
    return
'''


def servers(serverpool):
    serv = client.servers.get_all();
    for line in serv:
        if line["serverPoolId"] == serverpool:
            print line["name"]
            uri = line["id"]["uri"]
            r = requests.get(uri, auth=('admin', 'Hitachi123'), json=True, verify=False, headers=hd)
            data = r.json()
            print data["serverRunState"]
            print data["ipAddress"]
            cpus = line["cpuIds"]
            print "total CPU :" + str(len(cpus))
            mem_raw = int(data["memory"])
            mem_gb = mem_raw / 1024
            print "total RAM : " + str(mem_gb) + "GB"
            free_mem_raw = int(data["usableMemory"])
            free_mem_gb = free_mem_raw / 1024
            print " used RAM : " + str(mem_gb - free_mem_gb) + "GB"
            print "Total free RAM : " + str(free_mem_gb) + "GB\n\n"
            show_vms(line["id"])
    print "\n\n"
    return


def show_vms(server):
    print "Virtual Machines\n"
    vms = client.vms.get_all()
    for line in vms:
        if line["serverId"] == server:
            print "Name : " + line["name"]
            print "Status : " + line["vmRunState"]
            print "OS : " + line["osType"]
            print "Hypervisor : " + line["vmDomainType"]
            print "total CPU : " + str(line["cpuCountLimit"])
            print "current used RAM:" + str(line["currentMemory"])
            print "total RAM: " + str(line["memory"])
            # print "boot order :"+line["bootOrder"]
            repo = line["repositoryId"]
            print "Repository using for disk data : " + repo["name"]
            print "\n\n *************************************************\n"
    return


def show_connect_frm():
    try:
        ip = ip_val.get()
        usr = unm_val.get()
        pwd = pw_val.get()
        r = requests.get('https://' + ip + ':7002/ovm/core/wsapi/rest/', auth=(usr, pwd))
        connect_frm.tkraise()
    except Exception:
        error_frm.tkraise()


repo = client.repositories.get_all()
show_repo(repo)

spool = client.server_pools.get_all_ids()
show_server_pools(spool)

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

show_lbl = ttk.Label(connect_frm, text="Conected", font=("Verdana", 20))
show_lbl.place(x=700, y=25, anchor="center")

connect_frm.rowconfigure(0, weight=1)
connect_frm.columnconfigure(0, weight=1)


err_lbl = ttk.Label(error_frm, text="Error Connecting OVM , please check the details and Try again ...",
                    font=("Verdana",20), foreground="red")
err_lbl.place(x=700, y=250, anchor="center")


error_frm.grid(row=0, column=0, sticky="NSEW")
connect_frm.grid(row=0, column=0, sticky="NSEW")
login_frm.grid(row=0, column=0, sticky="NSEW")
login_frm.tkraise()


root.mainloop()
