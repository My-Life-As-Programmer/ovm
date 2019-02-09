import ovmclient
from ovmclient import constants
import requests
import ssl


# Disabling SSL certificate verification
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_NONE



print ("hello world")
'''
s=requests.Session()
s.auth=('admin','Hitachi123')
s.verify=False #disables SSL certificate verification
s.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json'})
'''
baseUri='https://192.168.1.21:7002/ovm/core/wsapi/rest'

client = ovmclient.Client(baseUri, 'admin', 'Hitachi123')

#vmm = ovmclient.VmManager(client)

repo_id2 = client.repositories.get_id_by_name('nfs_repo')
repo_id = client.repositories.get_id_by_name('localrepo_c3')

#print ("server pools =")
print(client.server_pools)
print (client.servers)
print (client.managers)
print (client.repositories)
print (" end")

#ovmclient.VmManager()  #takes 2 args

#print client.server_pools.get_all()

'''
#getting all server  pools
pools=client.server_pools.get_all()
for line in pools:
    print line["name"]
   # print line["vmIDs"]
'''

# getting all physical OVS
servers= client.servers.get_all()
'''
print ("Hostname  --- State   ------ Display Name ---- cluster \n ****************************************")
for line in servers:
    spool=line["serverPoolId"]
    if(spool["name"]):
        print (line["hostname"]+" -- "+line["serverRunState"]+"  --> "+line["name"]+" -- "+spool["name"]+" -----  "+line["manufacturer"]+"-- ovm version :"+line["ovmVersion"])
    else:
        print (line["hostname"] + " -- " + line["serverRunState"] + "  --> " + line["name"] + " -- NONE")
    #print (line["id"])
    #print (line["serverPoolId"])

'''
for line in servers:
    spool = line["serverPoolId"]
    if(spool["name"]== None):
        spool["name"]="none"
    print ("VMs in "+line["name"]+" of server pool :"+spool["name"])
    vms=line["vmIds"]
    #print (vms["name"])
    for vm in vms:
        print vm["name"]





spool=client.server_pools.get_id_by_name("cluster")

print spool["name"]


vmid=client.vms.get_id_by_name("cloudera_mgr") # chaitu_test2
print(vmid)

'''
repo_id = client.repositories.get_id_by_name('localrepo_c3')
pool_id = client.server_pools.get_id_by_name('cluster')
serv= client.servers.get_id_by_name("HDFS_Compute1")


vm_data = {
    'name': 'chaitu_test_new',
    'description': 'Created for Test purpose',
    'vmDomainType': constants.VM_DOMAIN_TYPE_XEN_HVM_PV_DRIVERS,
    'repositoryId': repo_id,
    'serverPoolId': pool_id,
    'server': serv,
    'cpuCount': 4,
    'cpuCountLimit': 4,
    'hugePagesEnabled': False,
    'memory': 1024,
    'memoryLimit': 1024,
    'osType': 'Oracle Linux 7',
}

client.vms.create(vm_data)
'''

print client.vms.__getattribute__

print client.vms.__class__
print client.vms.__doc__
print client.vms.__module__
'''
sysurl= client.vms.get_console_url(vmid)
totalurl="https://192.168.1.21:7002/"+sysurl
print totalurl

r = requests.get(totalurl)
print r.text
'''

suri=vmid["uri"]
print suri
#header = {'sslContext: context}
#r.headers=header

r=requests.get(suri,auth=('admin', 'Hitachi123'),json=True,verify=False)
print r.text
'''
rjs= r.json()
print rjs["generation"]
'''

print ("test starts here \n")
print client.vm_disk_mappings(vmid)
print(" vm all disks")
print client.vm_disk_mappings(vmid).get_all()
print(" server get test ")
print client.servers.get_id_by_name('HDFS_Compute1')

print("\n\n disk data \n\n")

print client.repository_virtual_disks(repo_id2).get_id_by_name("0004fb0000150000023792de438c8771.iso")#0004fb00001200003092de4b4e05032e.img")#hcchyd_os_team_d (4)")#'0004fb0000150000023792de438c8771.iso')
#print client.networks.get_all()

#print client.vm_disk_mappings(vmid).get_all()



print (" \n\n  test for disks \n\n")

disks = client.vm_disk_mappings(vmid).get_all()


for disk_id in disks:
    print disk_id["id"]