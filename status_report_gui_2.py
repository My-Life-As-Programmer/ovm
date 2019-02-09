import ovmclient
from ovmclient import constants
from Tkinter import *
import requests
from urllib3 import *
import ttk
import ssl
import time

requests.packages.urllib3.disable_warnings()

# Disabling SSL certificate verification
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_NONE


# START of the class
class OvmStatusReport:

    def __init__(self, parent):

        # common info
        self.ovm_ip = ''
        self.baseUri = 'https://' + self.ovm_ip + ':7002/ovm/core/wsapi/rest'
        self.usr = ''
        self.pwd = ''
        self.hd = {'Accept': 'application/json', 'Content-Type': 'application/json'}

        # using ovmclient
        self.client = None

        # JSON support
        self.ssn = requests.Session()
        # s.auth = (usr, pwd)
        # s.verify = False  # disables SSL certificate verification
        # s.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json'})

        # baseUri='https://192.168.1.21:7002/ovm/core/wsapi/rest'

        # Frames
        self.repo_frm = Frame(parent, height="850", width="1500")
        self.serv_frm = Frame(parent, height="850", width="1500")
        self.serv_pool_frm = Frame(parent, height="850", width="1500")
        self.vm_frm = Frame(parent, height="850", width="1500")
        self.login_frm = Frame(parent, height=850, width=1500)
        self.connect_frm = Frame(parent, height=850, width=1500)
        self.error_frm = Frame(parent, height=850, width=1500)
        self.vm_dtl_frm = Frame(parent, height=850, width=1500)

        # Labels
        # for login screen
        self.ip_lbl = ttk.Label(self.login_frm, text="IP address :", font=("Verdana", 15))
        self.unm_lbl = ttk.Label(self.login_frm, text="Username :", font=("Verdana", 15))
        self.pw_lbl = ttk.Label(self.login_frm, text="Password :", font=("Verdana", 15))

        self.ip_val = Entry(self.login_frm, width=25)
        self.unm_val = Entry(self.login_frm, width=25)
        self.pw_val = Entry(self.login_frm, show="*", width=25)

        self.ip_lbl.place(x=600, y=200, anchor="center")  # 100
        self.unm_lbl.place(x=600, y=250, anchor="center")  # 125
        self.pw_lbl.place(x=600, y=300, anchor="center")  # 150

        self.ip_val.place(x=800, y=205, anchor="center")  # 100
        self.unm_val.place(x=800, y=255, anchor="center")  # 125
        self.pw_val.place(x=800, y=305, anchor="center")  # 150

        # for connected screen
        self.con_show_lbl = ttk.Label(self.connect_frm, text="Successfully Connected", font=("Verdana", 20), foreground="dark green")
        self.con_show_lbl.place(x=700, y=250, anchor="center")

        self.con_repo = ttk.Button(self.connect_frm, width=30, text="Repositories", command=self.show_repo_frm)
        self.con_serv = ttk.Button(self.connect_frm, width=30, text="Servers", command=self.show_serv_pool_frm)
        self.con_repo.place(x=600, y=350, anchor="center")
        self.con_serv.place(x=800, y=350, anchor="center")

        # for error screen
        self.err_lbl = ttk.Label(self.error_frm, text="Error Connecting OVM , please check the details and Try again ...",
                            font=("Verdana", 20), foreground="red")

        self.err_go_back = ttk.Button(self.error_frm, width=30, text="Try Again", command=self.show_login_frm)
        self.err_go_back.place(x=700, y=350, anchor="center")

        self.err_lbl.place(x=700, y=250, anchor="center")

        # for login screen
        self.disp = ttk.Label(self.login_frm, text="Welcome, enter the details to connect to the OVM ", font=("Verdana", 20))
        self.disp.place(x=700, y=25, anchor="center")
        self.login_btn = ttk.Button(self.login_frm, width=30, text="Log In", command=self.show_connect_frm)
        self.login_btn.place(x=800, y=405, anchor="center")

        self.connect_frm.rowconfigure(0, weight=1)
        self.connect_frm.columnconfigure(0, weight=1)
        self.login_frm.rowconfigure(0, weight=1)
        self.login_frm.columnconfigure(0, weight=1)

        self.error_frm.grid(row=0, column=0, sticky="NSEW")
        self.connect_frm.grid(row=0, column=0, sticky="NSEW")
        self.login_frm.grid(row=0, column=0, sticky="NSEW")
        self.serv_pool_frm.grid(row=0, column=0, sticky="NSEW")
        self.vm_frm.grid(row=0, column=0, sticky="NSEW")
        self.vm_dtl_frm.grid(row=0, column=0, sticky="NSEW")

        # login_frm.tkraise()
        self.login_frm.tkraise()

    # To navigate to connection frame
    def show_connect_frm(self):
        print "in connect frm"
        try:

            self.ovm_ip = self.ip_val.get()
            self.usr = self.unm_val.get()
            self.pwd = self.pw_val.get()
            print self.ovm_ip
            print self.usr
            print self.pwd
            # r = requests.get('https://' + self.ovm_ip + ':7002/ovm/core/wsapi/rest/', auth=(self.usr, self.pwd))
            print self.ovm_ip
            print self.usr
            print self.pwd
            # print r.text
            # self.connect_frm.tkraise()
            # common info
            # ovm_ip = '192.168.1.21'
            # uname = 'admin'
            # pwd = 'Hitachi123'
            self.baseUri = 'https://' + self.ovm_ip + ':7002/ovm/core/wsapi/rest'

            # using ovmclient
            self.client = ovmclient.Client(self.baseUri, self.usr, self.pwd)

            # JSON support
            # self.ssn = requests.Session()
            self.ssn.auth = (self.usr, self.pwd)
            self.ssn.verify = False  # disables SSL certificate verification
            self.ssn.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json'})
            print 'https://' + self.ovm_ip + ':7002/ovm/core/wsapi/rest/'
            # self.ssn.get('https://' + self.ovm_ip + ':7002/ovm/core/wsapi/rest/')
            requests.get('https://' + self.ovm_ip + ':7002/ovm/core/wsapi/rest/', verify=False)

            self.connect_frm.tkraise()
        except IOError as e:
            print e.message
            self.error_frm.tkraise()
        except requests.exceptions.ConnectionError as e:
            print e.message
            self.error_frm.tkraise()
        except Exception:
            print "in exception"
            self.error_frm.tkraise()

    # go back to login screen
    def show_login_frm(self):
        self.login_frm.tkraise()

    # to show repositories
    def show_repo_frm(self):
        repo = self.client.repositories.get_all()
        self.show_repo(repo)

    # to show servers
    def show_serv_pool_frm(self):
        spool = self.client.server_pools.get_all_ids()
        self.serv_pool_serv(spool)

    # to go back to Servers
    def show_serv_frm(self):
        self.serv_pool_frm.tkraise()

    # to check ovm manager state
    def check_manager_state(self, baseUri, s):
        while True:
            r = s.get(baseUri + '/Manager')
            manager = r.json()
            if manager[0]['managerRunState'].upper() == 'RUNNING':
                return "OVM Manager is Running  ...... \n\n\n"
                time.sleep(1)
            else:
                return

    # to show ovm repo details & frame
    def show_repo(self, repo):
        # print "Repo details"
        repo_lbl = ttk.Label(self.repo_frm, text="Repo details", font=("Verdana", 20), background="cyan")
        repo_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
        tsz_lbl = ttk.Label(self.repo_frm, text="Total Size", font=("Verdana", 20), background="cyan")
        fsz_lbl = ttk.Label(self.repo_frm, text="Free Size", font=("Verdana", 20), background="cyan")
        usz_lbl = ttk.Label(self.repo_frm, text="Used Size", font=("Verdana", 20), background="cyan")
        tsz_lbl.grid(row=0, column=1, padx=20, pady=20, sticky="NSEW")
        fsz_lbl.grid(row=0, column=3, padx=20, pady=20, sticky="NSEW")
        usz_lbl.grid(row=0, column=2, padx=20, pady=20, sticky="NSEW")

        rw = 2
        tmp_lbl = ttk.Label(self.repo_frm, text=" ")

        for line in repo:
            # print line["name"]
            name = line["name"]
            ids = line["id"]
            #        r = requests.get(ids["uri"], auth=('admin', 'Hitachi123'), json=True, verify=False)
            fsid = line["fileSystemId"]
            r = requests.get(fsid["uri"], auth=(self.usr, self.pwd), json=True, verify=False, headers=self.hd)
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
            nm_lbl = ttk.Label(self.repo_frm, text=name, font=("Verdana", 16), background="cyan", padding=2)
            ttl_sz_lbl = ttk.Label(self.repo_frm, text=ttl_size, font=("Verdana", 16), padding=2)
            fr_sz_lbl = ttk.Label(self.repo_frm, text=free_size, font=("Verdana", 16), padding=2)
            usd_sz_lbl = ttk.Label(self.repo_frm, text=used_size, font=("Verdana", 16), padding=2)
            if u_size > 0.8 * total_size_gb:
                usd_sz_lbl.config(background="red")
                fr_sz_lbl.config(background="red")
                ttl_sz_lbl.config(background="red")
            else:
                usd_sz_lbl.config(background="green")
                fr_sz_lbl.config(background="green")
                ttl_sz_lbl.config(background="green")
            nm_lbl.grid(row=rw, column=0, sticky="NSEW", padx=10)
            tmp_lbl.grid(row=rw - 1, column=1)
            ttl_sz_lbl.grid(row=rw, column=1, padx=10, pady=10, sticky="NSEW")
            fr_sz_lbl.grid(row=rw, column=3, padx=10, pady=10, sticky="NSEW")
            usd_sz_lbl.grid(row=rw, column=2, padx=10, pady=10, sticky="NSEW")
            rw += 2
        go_back = ttk.Button(self.repo_frm, text=" Back ", command=self.show_connect_frm)
        go_back.place(x=500, y=500, anchor="center")
        self.repo_frm.grid(row=0, column=0, sticky="NSEW")
        self.repo_frm.tkraise()

    def show_server_pools(self, spool):
        for line in spool:
            if line["name"]:
                print "Server Pool : " + line["name"] + "\nServers:\n"
            else:
                print "Server Pool : " + line["value"] + "\nServers:\n"
            self.servers(line)
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

    def servers(self, serverpool):
        serv = self.client.servers.get_all()
        for line in serv:
            if line["serverPoolId"] == serverpool:
                print line["name"]
                uri = line["id"]["uri"]
                r = requests.get(uri, auth=('admin', 'Hitachi123'), json=True, verify=False, headers=self.hd)
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
                self.show_vms(line["id"])
        print "\n\n"
        return

    # to display serverpools and ovs
    def serv_pool_serv(self,spool):
        # sp_name = ttk.Label(self.serv_pool_frm, font=("Verdana", 16), padding=2, background="cyan")
        sp_name_lbl = ttk.Label(self.serv_pool_frm, text="Server Pool  " , font=("Verdana", 18), padding=2,
                            background="cyan")
        sr_name_lbl = ttk.Label(self.serv_pool_frm, text="Server  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        st_name_lbl = ttk.Label(self.serv_pool_frm, text="Status  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        ip_name_lbl = ttk.Label(self.serv_pool_frm, text="IP Address  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        cp_name_lbl = ttk.Label(self.serv_pool_frm, text="CPU   ", font=("Verdana", 18), padding=2,
                                background="cyan")
        rm_name_lbl = ttk.Label(self.serv_pool_frm, text="RAM  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        ur_name_lbl = ttk.Label(self.serv_pool_frm, text="Used RAM  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        fr_name_lbl = ttk.Label(self.serv_pool_frm, text="Free RAM  ", font=("Verdana", 18), padding=2,
                                background="cyan")

        sp_name_lbl.grid(row=0, column=0)
        sr_name_lbl.grid(row=0, column=1)
        st_name_lbl.grid(row=0, column=2)
        ip_name_lbl.grid(row=0, column=3)
        cp_name_lbl.grid(row=0, column=4)
        rm_name_lbl.grid(row=0, column=5)
        ur_name_lbl.grid(row=0, column=6)
        fr_name_lbl.grid(row=0, column=7)

        sprw=1
        serv = self.client.servers.get_all()
        for line in spool:
            # print sprw
            if line["name"]:
                # print "Server Pool : " + line["name"] + "\nServers:\n"
                sp_name = ttk.Label(self.serv_pool_frm, text=line["name"], font=("Verdana", 16), padding=2)#, background="cyan")
                # sp_text = "Server Pool : " + line["name"]
                # sp_name.config(text=sp_text)
                sp_name.grid(row=sprw, column=0)

            else:
                # print "Server Pool : " + line["value"] + "\nServers:\n"
                sp_name = ttk.Label(self.serv_pool_frm, text="Server Pool : " + line["value"], font=("Verdana", 16),
                                    padding=2, background="cyan")
                # sp_text = "Server Pool : " + line["value"]
                # sp_name.config(text=sp_text)
                sp_name.grid(row=sprw, column=0)

            sprw += 1
            srrw = sprw
            # print str(sprw)+"-----"+str(srrw)
            for line1 in serv:
                if line1["serverPoolId"] == line:
                    sname_lbl = ttk.Label(self.serv_pool_frm, text=line1["name"], font=("Verdana", 12), padding=2)
                    uri = line1["id"]["uri"]
                    r = requests.get(uri, auth=(self.usr, self.pwd), json=True, verify=False, headers=self.hd)
                    data = r.json()
                    if data["serverRunState"] == "RUNNING":
                        srnst_lbl = ttk.Label(self.serv_pool_frm, text=data["serverRunState"], font=("Verdana", 12),
                                              padding=2, background="green")
                    else:
                        srnst_lbl = ttk.Label(self.serv_pool_frm, text=data["serverRunState"], font=("Verdana", 12),
                                              padding=2, background="red")
                    sip_lbl = ttk.Label(self.serv_pool_frm, text=data["ipAddress"], font=("Verdana", 12), padding=2)
                    cpus = line1["cpuIds"]
                    cpu_lbl = ttk.Label(self.serv_pool_frm, text=str(len(cpus)), font=("Verdana", 12),
                                        padding=2)
                    mem_raw = int(data["memory"])
                    mem_gb = mem_raw / 1024
                    ttlmem_lbl = ttk.Label(self.serv_pool_frm, text=str(mem_gb) + "GB", font=("Verdana", 12),
                                           padding=2)
                    free_mem_raw = int(data["usableMemory"])
                    free_mem_gb = free_mem_raw / 1024
                    usd_mem_gb = mem_gb - free_mem_gb
                    usdmem_lbl = ttk.Label(self.serv_pool_frm, text=str(usd_mem_gb) + "GB", font=("Verdana", 12), padding=2)
                    frmem_lbl = ttk.Label(self.serv_pool_frm, text=str(free_mem_gb) + "GB", font=("Verdana", 12), padding=2)

                    if usd_mem_gb > 0.8 * mem_gb:
                        usdmem_lbl.config(background="red")
                        frmem_lbl.config(background="red")
                        ttlmem_lbl.config(background="red")
                    else:
                        usdmem_lbl.config(background="green")
                        frmem_lbl.config(background="green")
                        ttlmem_lbl.config(background="green")
                    sname_lbl.grid(row=srrw, column=1)
                    srnst_lbl.grid(row=srrw, column=2)
                    sip_lbl.grid(row=srrw, column=3)
                    cpu_lbl.grid(row=srrw, column=4)
                    ttlmem_lbl.grid(row=srrw, column=5)
                    usdmem_lbl.grid(row=srrw, column=6)
                    frmem_lbl.grid(row=srrw, column=7)
                    # print line1["id"]
                    vm_btn = ttk.Button(self.serv_pool_frm, text="VMS", command=lambda sid=line1["id"]: self.show_vms(sid))
                    vm_btn.grid(row=srrw, column=8)

                    srrw += 1
                    # print srrw
            sprw += srrw+1

            #print sprw
        sr_go_back = ttk.Button(self.serv_pool_frm, text="Back", command=self.show_connect_frm)
        sr_go_back.grid(row=sprw+1, column=5)
        self.serv_pool_frm.tkraise()
        return

    def show_vms(self, server):

        #print "Virtual Machines\n"
        vms = self.client.vms.get_all()
        vm_frm1 = Frame(self.vm_frm, height=850, width=1500)
        temp_lbl = ttk.Label(vm_frm1, text=" ", font=("Verdana", 16), padding=2)
        lbls = []
        lbls.append(temp_lbl)
        sr_name_lbl = ttk.Label(vm_frm1, text="VM Name  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        st_name_lbl = ttk.Label(vm_frm1, text="Status  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        os_name_lbl = ttk.Label(vm_frm1, text="OS Type  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        cp_name_lbl = ttk.Label(vm_frm1, text="CPU   ", font=("Verdana", 18), padding=2,
                                background="cyan")
        rm_name_lbl = ttk.Label(vm_frm1, text="RAM  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        ur_name_lbl = ttk.Label(vm_frm1, text="Used RAM  ", font=("Verdana", 18), padding=2,
                                background="cyan")
        # fr_name_lbl = ttk.Label(vm_frm1, text="Free RAM  ", font=("Verdana", 18), padding=2, background="cyan")
        sr_name_lbl.grid(row=0, column=0)
        # sr_name_lbl.grid(row=0, column=1)
        st_name_lbl.grid(row=0, column=2)
        os_name_lbl.grid(row=0, column=4)
        cp_name_lbl.grid(row=0, column=6)
        ur_name_lbl.grid(row=0, column=8)
        rm_name_lbl.grid(row=0, column=10)
        # fr_name_lbl.grid(row=0, column=7)

        #  server
        rw = 1
        for line in vms:
            #print "in for line['serverId'] = "
            # print line["serverId"]
            if line["serverId"] == server:
                # print "in if line['serverId'] = "
                # print line["serverId"]
                vm_name_lbl = ttk.Label(vm_frm1, text=line["name"], font=("Verdana", 16), padding=2)
                vm_name_lbl.grid(row=rw, column=0)
                lbls.append(vm_name_lbl)
                vm_sts_lbl = ttk.Label(vm_frm1, text=line["vmRunState"], font=("Verdana", 12), padding=2)
                temp_lbl.grid(row=rw, column=1)
                vm_sts_lbl.grid(row=rw, column=2)
                lbls.append(vm_sts_lbl)
                vm_os_lbl = ttk.Label(vm_frm1, text=line["osType"], font=("Verdana", 12), padding=2)
                vm_cpu_lbl = ttk.Label(vm_frm1, text=str(line["cpuCountLimit"]), font=("Verdana", 12),
                                       padding=2)
                vm_uram_lbl = ttk.Label(vm_frm1, text=str(int(line["currentMemory"])/1024)+"GB", font=("Verdana", 12), padding=2)
                vm_ttlram_lbl = ttk.Label(vm_frm1, text=str(int(line["memory"])/1024)+"GB", font=("Verdana", 12), padding=2)
                '''
                vm_creat_btn = ttk.Button(vm_frm1, text="Create VM")#, command=lambda: self.create_vm(server, line["repositoryId"]))
                temp_lbl.grid(row=rw, column=3)
                vm_creat_btn.grid(row=rw, column=4)
                '''
                # vm_lbl = ttk.Label(vm_frm1, text=line["name"], font=("Verdana", 12), padding=2)
                # rw += 1
                temp_lbl.grid(row=rw, column=3)
                vm_os_lbl.grid(row=rw, column=4)
                temp_lbl.grid(row=rw, column=5)
                vm_cpu_lbl.grid(row=rw, column=6)
                temp_lbl.grid(row=rw, column=7)
                vm_uram_lbl.grid(row=rw, column=8)
                temp_lbl.grid(row=rw, column=9)
                vm_ttlram_lbl.grid(row=rw, column=10)
                rw += 1
                lbls.append(vm_os_lbl)
                lbls.append(vm_cpu_lbl)
                lbls.append(vm_uram_lbl)
                lbls.append(vm_ttlram_lbl)
                # lbls.append(vm_os_lbl)
                # lbls.append(vm_os_lbl)

                # print "Name : " + line["name"]
                # print "Status : " + line["vmRunState"]
                # print "OS : " + line["osType"]
                # print "Hypervisor : " + line["vmDomainType"]
                # print "total CPU : " + str(line["cpuCountLimit"])
                # print "current used RAM:" + str(line["currentMemory"])
                # print "total RAM: " + str(line["memory"])
                # print "boot order :"+line["bootOrder"]
                #repo = line["repositoryId"]
                #print "Repository using for disk data : " + repo["name"]
                #print "\n\n *************************************************\n"

        def change():
            vm_frm1.grid_forget()
            self.show_serv_frm()

        vm_creat_btn = ttk.Button(vm_frm1, width=30, text="Create VM",
                                  command=lambda: self.create_vm(server, line["repositoryId"]))
        vm_creat_btn.grid(row=rw + 1, column=5)
        vm_go_back = ttk.Button(vm_frm1, width=30, text="Back", command=change)
        vm_go_back.grid(row=rw + 1, column=3)
        lbls.append(vm_creat_btn)
        lbls.append(vm_go_back)
        vm_frm1.rowconfigure(0, weight=1)
        vm_frm1.columnconfigure(0, weight=1)
        vm_frm1.grid(row=0, column=0)
        self.vm_frm.tkraise()

        return

    # to create a new VM
    def create_vm(self, server, repo):
        title = ttk.Label(self.vm_dtl_frm , text="Creating a VM in Server : "+server["name"] ,font=("Verdana", 25), foreground="dark green")
        title.place(x=600, y=100, anchor="center")
        name_lbl = ttk.Label(self.vm_dtl_frm, text="Name :", font=("Verdana", 15))
        desc_lbl = ttk.Label(self.vm_dtl_frm, text="Description :", font=("Verdana", 15))
        cpu_lbl = ttk.Label(self.vm_dtl_frm, text="CPU :", font=("Verdana", 15))
        ram_lbl = ttk.Label(self.vm_dtl_frm, text="RAM(GB) :", font=("Verdana", 15))
        disk_lbl = ttk.Label(self.vm_dtl_frm, text="Disk_Name :", font=("Verdana", 15))
        disksz_lbl = ttk.Label(self.vm_dtl_frm, text="Disk_Size(GB) :", font=("Verdana", 15))

        name_val = Entry(self.vm_dtl_frm, width=25)
        desc_val = Entry(self.vm_dtl_frm, width=25)
        cpu_val = Entry(self.vm_dtl_frm, width=25)
        ram_val = Entry(self.vm_dtl_frm, width=25)
        disk_val = Entry(self.vm_dtl_frm, width=25)
        disksz_val = Entry(self.vm_dtl_frm, width=25)

        name_lbl.place(x=600, y=200, anchor="center")  # 100
        desc_lbl.place(x=600, y=250, anchor="center")  # 125
        cpu_lbl.place(x=600, y=300, anchor="center")  # 150
        ram_lbl.place(x=600, y=350, anchor="center")  # 125
        disk_lbl.place(x=600, y=400, anchor="center")  # 150
        disksz_lbl.place(x=600, y=450, anchor="center")

        name_val.place(x=800, y=205, anchor="center")  # 100
        desc_val.place(x=800, y=255, anchor="center")  # 125
        cpu_val.place(x=800, y=305, anchor="center")  # 150
        ram_val.place(x=800, y=355, anchor="center")  # 125
        disk_val.place(x=800, y=405, anchor="center")  # 150
        disksz_val.place(x=800, y=455, anchor="center")

        # creating vm
        def create():
            repo_id2 = self.client.repositories.get_id_by_name('nfs_repo')
            network_id = self.client.networks.get_id_by_name('192.168.1.0')
            pool_id = self.client.servers.get_by_id(server)["serverPoolId"]
            # for line in self.client.servers.get_all():
            #   if line["serverID"] == server:
            #       pool_id = line["id"]

            # Create a virtual disk
            disk_data_vd = {
                'diskType': constants.DISK_TYPE_VIRTUAL_DISK,
                'size': 1024 * 1024 * int(disksz_val.get()),
                'shareable': False,
                'name': disk_val.get(),
            }
            job = self.client.jobs.wait_for_job(
                self.client.repository_virtual_disks(repo).create(disk_data_vd, sparse='true'))
            disk_id_vd = job['resultId']

            disk_id_cd = self.client.repository_virtual_disks(repo_id2).get_id_by_name(
                "0004fb000015000001f8f9c7264da700.iso (2)")  # 0004fb0000150000023792de438c8771.iso")
            # Create a VM
            vm_data = {
                'name': name_val.get(),
                'description': disk_val.get(),
                'bootOrder': ['CDROM', 'DISK'],
                'vmDomainType': constants.VM_DOMAIN_TYPE_XEN_HVM_PV_DRIVERS,
                'repositoryId': repo,
                'serverPoolId': pool_id,
                'serverId': server,
                'cpuCount': int(cpu_val.get()),
                'cpuCountLimit': int(cpu_val.get()),
                'hugePagesEnabled': False,
                'memory': int(ram_val.get()) * 1024,
                'memoryLimit': int(ram_val.get())* 1024,
                'osType': 'Oracle Linux 7',

            }

            job = self.client.jobs.wait_for_job(self.client.vms.create(vm_data))
            vm_id = job['resultId']

            # Map the virtual disk
            vm_disk_mapping_data_vd = {
                'virtualDiskId': disk_id_vd,
                'diskWriteMode': constants.DISK_WRITE_MODE_READ_WRITE,
                'emulatedBlockDevice': False,
                'storageElementId': None,
                'diskTarget': 0,
            }

            # Map the virtual CDROM
            vm_disk_mapping_data_cd = {
                'virtualDiskId': disk_id_cd,
                'diskWriteMode': constants.DISK_WRITE_MODE_READ_ONLY,
                'emulatedBlockDevice': False,
                'storageElementId': None,
                'diskTarget': 1,
            }
            job = self.client.jobs.wait_for_job(
                self.client.vm_disk_mappings(vm_id).create(vm_disk_mapping_data_vd))

            job = self.client.jobs.wait_for_job(
                self.client.vm_disk_mappings(vm_id).create(vm_disk_mapping_data_cd))

            # Add a vnic
            vnic_data = {
                'networkId': network_id,
            }

            self.client.jobs.wait_for_job(self.client.vm_virtual_nics(vm_id).create(vnic_data))

            # Retrieve the VM
            vm = self.client.vms.get_by_id(vm_id)

            if vm:
                print ("vm created")
            else:
                print ("vm creation failed")
            '''
            # Update the VM, e.g. setting a new name
            vm['name'] = 'chaitu_test2'
            client.jobs.wait_for_job(client.vms.update(vm_id, vm))
            '''
            # Start the VM
            fnl_url = Text(self.vm_dtl_frm, width=50, height=10)
            try:
                self.client.jobs.wait_for_job(self.client.vms.start(vm_id))
                fnl_url.insert(END, "https://192.168.1.21:7002/" + self.client.vms.get_console_url(vm_id))
                fnl_url.place(x=1100, y=400, anchor="center")
            except Exception as e:
                fnl_url.insert(END, e.message)
                fnl_url.place(x=1100, y=400, anchor="center")
            print "https://192.168.1.21:7002/" + self.client.vms.get_console_url(vm_id)

            time.sleep(5)

        crt_btn = ttk.Button(self.vm_dtl_frm, text="Create", width=25, command=create)
        crt_btn.place(x=700, y=550, anchor="center")
        vm_go_back = ttk.Button(self.vm_dtl_frm, width=20, text="Back", command=self.show_serv_frm)
        vm_go_back.place(x=500, y=550, anchor="center")
        self.vm_dtl_frm.tkraise()
        return

# END of class


# GUI info
root = Tk()
root.title("OVM Status Report")
root.minsize(width=1500, height=850)
# root.maxsize(width=666, height=666)
# font_style = ttk.style()
# font_style.config(font=("Verdana", 16))

obj = OvmStatusReport(root)
root.mainloop()
