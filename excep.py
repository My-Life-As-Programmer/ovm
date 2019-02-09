import ovmclient
import requests

'''
try:
    ip = ip_val.get()
    usr = unm_val.get()
    pwd = pw_val.get()
    r = requests.get('https://'+ip+':7002/ovm/core/wsapi/rest/', auth=(usr, pwd))
except Exception :
    print Exception
'''

ovm_ip = "192.168.1.21"
baseUri = 'https://' + ovm_ip + ':7002/ovm/core/wsapi/rest'
uname = 'admin'
pwd = 'Hitachi123'#'ZAQ12wsx'
hd = {'Accept': 'application/json', 'Content-Type': 'application/json'}
client = ovmclient.Client(baseUri, uname, pwd)
for line in  client.servers.get_all():
    print line["serverPoolId"]

client.servers.get_by_id()