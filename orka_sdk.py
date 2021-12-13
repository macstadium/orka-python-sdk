import json
import requests

from vm import VM

ORKA_IP = 'http://10.221.188.100'

class OrkaSDK:

	def __init__(self):
		self.token = None
		self.user = None
		self.password = None
		self.license_key = None

###################  Auth  ###################

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

###############  VM Management  ###############

	def create_vm(self, vm_data):
		self.create_vm_config(vm_data)
		r = self.deploy_vm_config(vm_data.vm_name)
		vm = VM(r)

		return vm

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
		requests.post(url, data=json.dumps(data), headers=headers)

		return 0
        
	def deploy_vm_config(self, vm_name):
		url = f"{ORKA_IP}/resources/vm/deploy"
		headers = {
			'Content-Type': 'application/json', 
			'Authorization': f"Bearer {self.token}"
			}
		data =  {'orka_vm_name': vm_name}
		r = requests.post(url, data=json.dumps(data), headers=headers)
		vm = VM(r)

		return vm

	def list_session_vms(self):
		url = f"{ORKA_IP}/resources/vm/list"
		headers = {
			'Content-Type': 'application/json', 
			'Authorization': f"Bearer {self.token}"
			}
		r = requests.post(url, headers=headers)

		return r

	def list_user_vms(self, user=None):
		if self.license_key:
			if not user:
				user = self.user
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
			return 'Error: This method requires an orka license_key'
		




