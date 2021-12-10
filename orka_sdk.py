import json
import requests

ORKA_IP = 'http://10.221.188.100'

class OrkaSDK:

	def __init__(self):
		self.token = None
		self.user = None
		self.password = None
		self.license_key = None

###############  Auth  ################

	def login(self, user, password, license_key=None):
		self.user = user
		self.password = password
		self.license_key = license_key
		self.token = self._get_token(user, password)

	def _get_token(self, user, password):
		data = {'email': user, 'password': password}
		result = requests.post(f"{ORKA_IP}/token", data=data)
		content = json.loads(result._content.decode('utf-8'))
		self.token = content['token']

################  VM Management  ###################

	def create_vm(self, vm_data):
		self.create_vm_config(vm_data)
		r = self.deploy_vm_config(vm_data.vm_name)

		return r

	def create_vm_config(self, vm_data):
		url = f"{ORKA_IP}/resources/vm/create"
		headers = {
			'Content-Type': 'application/json', 
			'Authorization': f"Bearer {self.token}"
			}
		data = {
			'orka_vm_name': vm_data['vm_name'],
			'orka_base_image': vm_data['orka_base_image'],
			'orka_image': vm_data['vm_name'],
			'orka_cpu_core': int(vm_data['core_count']),
			'vcpu_count': int(vm_data['vcpu_count'])
			}
		r = requests.post(url, data=json.dumps(data), headers=headers)

		return r
        
	def deploy_vm_config(self, vm_name):
		url = f"{ORKA_IP}/resources/vm/deploy"
		headers = {
			'Content-Type': 'application/json', 
			'Authorization': f"Bearer {self.token}"
			}
		data =  {'orka_vm_name': vm_name}
		r = requests.post(url, data=json.dumps(data), headers=headers)

		return r

	def list_session_vms(self):
		url = f"{ORKA_IP}/resources/vm/list"
		headers = {
			'Content-Type': 'application/json', 
			'Authorization': f"Bearer {self.token}"
			}
		r = requests.post(url, headers=headers)

		return r

	def list_user_vms(self, user=self.user):
		if self.license_key:
			url = f"{ORKA_IP}/resources/vm/list/{user}"
				headers = {
					'Content-Type': 'application/json', 
					'Authorization': f"Bearer {self.token}",
					'orka-licensekey': self.license_key
					}
			r = requests.post(url, headers=headers)

			return r
		else:
			return 'Error: This method requires an orka license_key'

	def list_system_vms(self):
		if self.license_key:
			url = f"{ORKA_IP}/resources/vm/list/all"
				headers = {
					'Content-Type': 'application/json', 
					'Authorization': f"Bearer {self.token}",
					'orka-licensekey': self.license_key
					}
			r = requests.post(url, headers=headers)

			return r
		else:
			return 'This method requires an orka license_key'
		
	def delete_vm(self):
		pass

##################################
import os

user = os.environ.get('ORKA_USER')
password = os.environ.get('ORKA_PASS')
license_key = os.environ.get('ORKA_LICENSE_KEY')

orka = OrkaSDK()
orka.login(user, password, license_key)
print(orka.__dict__)

vm_data = {
	'vm_name':'fake_name',
	'orka_base_image': '90GBigSurSSH.img',
	'core_count': '3',
	'vcpu_count': '3'
}

config = orka.create_vm_config(vm_data)
vm = orka.deploy_vm_config(vm_data.vm_name)
print(vm)



