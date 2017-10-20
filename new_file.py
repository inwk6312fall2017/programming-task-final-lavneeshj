#import certifi
#import urllib3
#http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where()
 

# import requests library
import requests

#import json library
import json

#controller='sandboxapic.cisco.com'
controller='devnetapi.cisco.com/sandbox/apic_em'

def getTicket():
	# put the ip address or dns of your apic-em controller in this url
	url = "https://" + controller + "/api/v1/ticket"

	#the username and password to access the APIC-EM Controller
	payload = {"username":"devnetuser","password":"Cisco123!"}

	#Content type must be included in the header
	header = {"content-type": "application/json"}

	#Performs a POST on the specified url to get the service ticket
	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

	print (response)

	#convert response to json format
	r_json=response.json()

	#parse the json to get the service ticket
	ticket = r_json["response"]["serviceTicket"]

	return ticket

###now create the required function 

def get_networkDevices_count(ticket):

# URL for network-device REST API call to get a count of network devices.
	url = "https://" + controller + "/api/v1/network-device/config/count"

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a GET on the specified network device url
	response = requests.get(url, headers=header, verify=False)

	print ("Network Devices Count = ")
	print(response)
	

theTicket=getTicket()
get_networkDevices_count(theTicket)

