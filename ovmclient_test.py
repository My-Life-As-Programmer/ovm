import ovmclient
from ovmclient import constants
import time

client = ovmclient.Client(
    'https://192.168.1.21:7002/ovm/core/wsapi/rest', 'admin', 'Hitachi123')

# Make sure the manager is running
client.managers.wait_for_manager_state()

repo_id = client.repositories.get_id_by_name('localrepo_c3')
repo_id2 = client.repositories.get_id_by_name('nfs_repo')
pool_id = client.server_pools.get_id_by_name('cluster')
network_id = client.networks.get_id_by_name('192.168.1.0') #c0a80100--id /management - default in example
#server_id=client.servers.get_id_by_name('HDFS_Compute1')
# Create a virtual disk
disk_data_vd = {
    'diskType': constants.DISK_TYPE_VIRTUAL_DISK,
    'size': 1024 * 1024 * 1024,
    'shareable': False,
    'name': 'disk_test_1.img',
}

# Create a virtual cd rom
disk_data_cd = {
    'diskType': constants.DISK_TYPE_VIRTUAL_CDROM,
    'size': 4096 * 1024 * 1024,
    'shareable': False,
    'name': 'iso.img',
}

job = client.jobs.wait_for_job(
    client.repository_virtual_disks(repo_id).create(disk_data_vd, sparse='true'))
disk_id_vd = job['resultId']
'''
job = client.jobs.wait_for_job(
    client.repository_virtual_disks(repo_id).create(disk_data_cd, sparse='false'))
disk_id_cd = job['resultId']
'''

disk_id_cd = client.repository_virtual_disks(repo_id2).get_id_by_name("0004fb000015000001f8f9c7264da700.iso (2)")#0004fb0000150000023792de438c8771.iso")
# Create a VM
vm_data = {
    'name': 'chaitu_test_new_disk_1',
    'description': 'Created for Test purpose',
    'bootOrder':['CDROM','DISK'],
    'vmDomainType': constants.VM_DOMAIN_TYPE_XEN_HVM_PV_DRIVERS,
    'repositoryId': repo_id,
    'serverPoolId': pool_id,
    'cpuCount': 4,
    'cpuCountLimit': 4,
    'hugePagesEnabled': False,
    'memory': 1024,
    'memoryLimit': 1024,
    'osType': 'Oracle Linux 7',

}

job = client.jobs.wait_for_job(client.vms.create(vm_data))
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
job = client.jobs.wait_for_job(
    client.vm_disk_mappings(vm_id).create(vm_disk_mapping_data_vd))

job = client.jobs.wait_for_job(
    client.vm_disk_mappings(vm_id).create(vm_disk_mapping_data_cd))

# Add a vnic
vnic_data = {
    'networkId': network_id,
}

client.jobs.wait_for_job(client.vm_virtual_nics(vm_id).create(vnic_data))

# Retrieve the VM
vm = client.vms.get_by_id(vm_id)

if vm :
    print ("vm created")
else:
    print ("vm creation failed")
'''
# Update the VM, e.g. setting a new name
vm['name'] = 'chaitu_test2'
client.jobs.wait_for_job(client.vms.update(vm_id, vm))
'''
# Start the VM
client.jobs.wait_for_job(client.vms.start(vm_id))

print "https://192.168.1.21:7002/"+client.vms.get_console_url(vm_id)

time.sleep(5)

# Kill the VM
#client.jobs.wait_for_job(client.vms.kill(vm_id))

#time.sleep(5)

# Delete the VM
#client.jobs.wait_for_job(client.vms.delete(vm_id))

# Delete the virtual disk
#client.jobs.wait_for_job(
#   client.repository_virtual_disks(repo_id).delete(disk_id))
