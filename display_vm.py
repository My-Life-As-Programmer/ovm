import ovmclient
from ovmclient import constants
import requests
import ssl

hd={'Accept': 'application/json', 'Content-Type': 'application/json'}

baseUri='https://192.168.1.21:7002/ovm/core/wsapi/rest'

client = ovmclient.Client(baseUri, 'admin', 'Hitachi123')
'''
order = {'CDROM', 'DISK'}

vmid=client.vms.get_id_by_name("chaitu_test_new_disk_1") # chaitu_test2
print(vmid)
suri=vmid["uri"]
print suri
# header = {'sslContext: context}
# r.headers=header

r=requests.get(suri,auth=('admin', 'Hitachi123'),json=True,verify=False)
print r.text

vdata={
    'bootOrder': order,
}

client.vms.update(vmid, vdata)
client.vms.start(vmid)
# client.vms.c

'''

''' displaying repo info
def show_repo(repo):
    for line in repo:
        print line["name"]
        ids=line["id"]
#        r = requests.get(ids["uri"], auth=('admin', 'Hitachi123'), json=True, verify=False)
        fsid=line["fileSystemId"]
        r = requests.get(fsid["uri"], auth=('admin', 'Hitachi123'), json=True, verify=False,headers=hd)
        data = r.json()
        total_size_raw = int(data["size"])
        total_size_gb = total_size_raw/(1024**3)
        used_space_raw = int(data["freeSize"])
        used_space_gb=used_space_raw/(1024**3)
        print "total size of repo is "+str(total_size_gb)+"GB"
        print "free size of repo is " + str(used_space_gb) + "GB"
        print "used space of repo is "+str(total_size_gb-used_space_gb)+"GB"

        print '\n'


repo = client.repositories.get_all()
show_repo(repo)
'''

def show_server_pools(spool):
    for line in spool:
        if line["name"]:
            print "Server Pool : "+line["name"]+"\n"
        else:
            print "Server Pool : " + line["value"]+"\n"
        servers(line)
    return


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
            mem_gb = mem_raw/1024
            print "total RAM : "+str(mem_gb)+"GB"
            free_mem_raw = int(data["usableMemory"])
            free_mem_gb = free_mem_raw/1024
            print " used RAM : "+str(mem_gb-free_mem_gb)+"GB"
            print "Total free RAM : "+str(free_mem_gb)+"GB"
    print "\n"
    return



spool = client.server_pools.get_all_ids()
show_server_pools(spool)



