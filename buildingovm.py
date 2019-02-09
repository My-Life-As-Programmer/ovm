import requests
import time
import warnings

warnings.filterwarnings("ignore")

s=requests.Session()
s.auth=('admin','Hitachi123')
s.verify=False #disables SSL certificate verification
s.headers.update({'Accept': 'application/json', 'Content-Type': 'application/json'})
baseUri='https://192.168.1.21:7002/ovm/core/wsapi/rest'

def check_manager_state(baseUri,s):
	while True:
		r=s.get(baseUri+'/Manager')
		manager=r.json()
		if manager[0]['managerRunState'].upper() == 'RUNNING':
			return "OVM Manager is Running  ...... "
			#break
		time.sleep(1)
	return;

print check_manager_state(baseUri,s)
		
#''' listing servers
r=s.get(baseUri+'/Server')
for i in r.json():
	# do something with the content
	#print(i)
	print '{name} is {state}'.format(name=i['name'],state=i['serverRunState'])
	#print i["ip"]
#'''


''' discovering servers 
uri_params={'serverName':'1.example.com', 'takeOwnershipIfUnowned':'True'}
data='p4ssword'
r=s.post(baseUri+'/Server/discover', data, params=uri_params)
'''

'''
job=r.json()
print 'Job: {name} for {server}'.format(name=job['id']['name'],server='1.example.org')
joburi=job['id']['uri']
wait_for_job(joburi,s)
'''

'''
def wait_for_job(joburi,s):
        while True:
            time.sleep(1)
            r=s.get(joburi)
            job=r.json()
            if job['summaryDone']:
                print '{name}: {runState}'.format(name=job['name'], runState=job['jobRunState'])
                if job['jobRunState'].upper() == 'FAILURE':
                    raise Exception('Job failed: {error}'.format(error=job['error']))
                elif job['jobRunState'].upper() == 'SUCCESS':
                    if 'resultId' in job:
                        return job['resultId']
                    break
                else:
                    break  
					
'''