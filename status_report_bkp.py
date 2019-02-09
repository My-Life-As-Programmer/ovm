import ovmclient
import Tkinter
import requests

'''
server_pool
    servers
        vms

    repo


'''

# common info
ovm_ip = '192.168.1.21'
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


def show_repo(repo):
    print "Repo details"
    for line in repo:
        print line["name"]
        ids = line["id"]
        #        r = requests.get(ids["uri"], auth=('admin', 'Hitachi123'), json=True, verify=False)
        fsid = line["fileSystemId"]
        r = requests.get(fsid["uri"], auth=('admin', 'Hitachi123'), json=True, verify=False, headers=hd)
        data = r.json()
        total_size_raw = int(data["size"])
        total_size_gb = total_size_raw / (1024 ** 3)
        used_space_raw = int(data["freeSize"])
        used_space_gb = used_space_raw / (1024 ** 3)
        print "total size of repo is " + str(total_size_gb) + "GB"
        print "free size of repo is " + str(used_space_gb) + "GB"
        print "used space of repo is " + str(total_size_gb - used_space_gb) + "GB"
        print '\n'


repo = client.repositories.get_all()
show_repo(repo)

spool = client.server_pools.get_all_ids()
show_server_pools(spool)

