import ovmclient
from ovmclient import constants

client = ovmclient.Client(
    'https://192.168.1.21:7002/ovm/core/wsapi/rest', 'admin', 'Hitachi123')

repo_id = client.repositories.get_id_by_name('localrepo_c3')

vmid=client.vms.get_id_by_name("chaitu_test_new_disk_1") # chaitu_test2
print(vmid)



disks = client.vm_disk_mappings(vmid).get_all()


for disk_id in disks:
# Delete the virtual disk
    client.jobs.wait_for_job(client.repository_virtual_disks(repo_id).delete(disk_id["id"]))

# Kill the VM
client.jobs.wait_for_job(client.vms.kill(vmid))

#time.sleep(5)

# Delete the VM
client.jobs.wait_for_job(client.vms.delete(vmid))


print (" vm deleted ")