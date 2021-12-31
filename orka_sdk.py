import json
import requests
from result import Result
from vm import VM
from images import Images
from k8s import K8s
from nodes import Nodes


ORKA_IP = 'http://10.221.188.100'

class OrkaSDK:

	def __init__(self):
		self.orka_ip = ORKA_IP
		self.token = None
		self.user = None
		self.password = None
		self.license_key = None
		self.k8s = None
		self.images = None
		self.nodes = None

###################  Auth  ###################

	def login(self, user, password, license_key=None):
		errors = []
		self.user = user
		self.password = password
		self.license_key = license_key
		try:
			self.token = self._get_token(user, password)
			self.nodes = Nodes(self)
			self.images = Images(self)
			if self.license_key:
				self.k8s = K8s(self)
			else:
				# TODO: logging?
				print('Kubernetes functionality disabled. Requires Orka license-key.')
		except Exception as e:
			errors = [str(e)]

			return Result(errors=errors)

		return Result(errors=errors)

	def _get_token(self, user, password):
		headers = {'Content-Type': 'application/json'}
		data = json.dumps({'email': user, 'password': password})
		result = requests.post(f"{ORKA_IP}/token", data=data, headers=headers)
		content = json.loads(result._content.decode('utf-8'))

		return content['token']

	def revoke_token(self):
		pass

###############  VM Management  ###############

	def create_vm(self, vm_data):
		self.create_vm_config(vm_data)

		return self.deploy_vm_config(vm_data['vm_name'])

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
		content = json.loads(r._content.decode('utf-8'))
		errors = content.get('errors')
		
		return Result(errors=errors)
        
	def deploy_vm_config(self, vm_name):
		url = f"{ORKA_IP}/resources/vm/deploy"
		headers = {
			'Content-Type': 'application/json', 
			'Authorization': f"Bearer {self.token}"
			}
		data =  {'orka_vm_name': vm_name}
		r = requests.post(url, data=json.dumps(data), headers=headers)
		content = json.loads(r._content.decode('utf-8'))
		errors = content.get('errors')
		if errors:

			return Result(errors=errors)

		try:
			data = self._parse_config_response(content)
			vm = VM(data)
		except Exception as e:
			errors = [str(e)]

			return Result(errors=errors)
		
		return Result(errors=errors, data=vm)

	def _parse_config_response(self, content):
		data = {}
		data['ip'] = content['ip']
		data['id'] = content['vm_id']
		data['ssh_port'] = content['ssh_port']
		data['name'] = \
			content['help']['data_for_virtual_machine_exec_tasks']['orka_vm_name']
		data['ram'] = content['ram']
		data['vcpu'] = content['vcpu']
		data['cpu'] = content['host_cpu']
		data['io_boost'] = content['io_boost']
		data['use_saved_state'] = content['use_saved_state']
		data['gpu_passthrough'] = content['gpu_passthrough']
		data['screen_share_port'] = content['screen_share_port']
		data['vnc_port'] = content['vnc_port']

		return data

	def list_session_vms(self):
		url = f"{ORKA_IP}/resources/vm/list"
		headers = {
			'Content-Type': 'application/json', 
			'Authorization': f"Bearer {self.token}"
			}
		r = requests.get(url, headers=headers)
		content = json.loads(r._content.decode('utf-8'))
		errors = content.get('errors')
		if errors:
		
			return Result(errors=errors)
		vm_instances = self._instantiate_vms(content)

		return Result(errors=None, data=vm_instances)

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
			r = requests.get(url, headers=headers)
			content = json.loads(r._content.decode('utf-8'))
			errors = content.get('errors')
			if errors:

				return Result(errors=errors)
			try:
				vm_instances = self._instantiate_vms(content)
			except Exception as e:
				errors = [f'Failed to instantiate VMs, missing key {str(e)}']

				return Result(errors=errors)

			return Result(errors=errors, data=vm_instances)
		else:
			errors = ['This method requires an orka license_key']

			return Result(errors=errors)

	def list_system_vms(self):
		if self.license_key:
			url = f"{ORKA_IP}/resources/vm/list/all"
			headers = {
				'Content-Type': 'application/json', 
				'Authorization': f"Bearer {self.token}",
				'orka-licensekey': self.license_key
				}
			r = requests.get(url, headers=headers)
			content = json.loads(r._content.decode('utf-8'))
			errors = content.get('errors')
			if errors:

				return Result(errors=errors)
			try:
				vm_instances = self._instantiate_vms(content)
			except Exception as e:
				errors = [f'Failed to instantiate VMs, missing key {str(e)}']

				return Result(errors=errors)

			return Result(errors=None, data=vm_instances)
		else:
			errors = ['This method requires an orka license_key']

			return Result(errors=errors)

	def _instantiate_vms(self, content):
		vm_instances = []
		for vm in content['virtual_machine_resources']:
			if vm['vm_deployment_status'] == 'Deployed':
				data = {}
				data['ssh_port'] = vm['status'][0]['ssh_port']
				data['ip'] = vm['status'][0]['virtual_machine_ip']
				data['id'] = vm['status'][0]['virtual_machine_id']
				data['name'] = vm['virtual_machine_name']
				data['ram'] = vm['status'][0]['RAM']
				data['vcpu'] = vm['status'][0]['vcpu']
				data['cpu'] = vm['status'][0]['cpu']
				data['io_boost'] = vm['status'][0]['io_boost']
				data['use_saved_state'] = vm['status'][0]['use_saved_state']
				data['gpu_passthrough'] = vm['status'][0]['gpu']
				data['screen_share_port'] = vm['status'][0]['screen_sharing_port']
				data['vnc_port'] = vm['status'][0]['vnc_port']
				data['deployed'] = True
				vm = VM(data)
				vm_instances.append(vm)
			else:
				data = {}
				data['ssh_port'] = None
				data['ip'] = None
				data['id'] = None
				data['name'] = vm['virtual_machine_name']
				data['ram'] = None
				data['vcpu'] = vm['vcpu']
				data['cpu'] = vm['cpu']
				data['io_boost'] = vm['io_boost']
				data['use_saved_state'] = vm['use_saved_state']
				data['gpu_passthrough'] = vm['gpu_passthrough']
				data['screen_share_port'] = None
				data['vnc_port'] = None
				data['deployed'] = False
				vm = VM(data)
				vm_instances.append(vm)

		return vm_instances

	def get_vm_by_id(self, _id):
		r = self.list_session_vms()
		if r.errors:

			return Result(errors=r.errors)

		for vm in r.data:
			if vm.id == _id:
				data = vm
			else:
				errors = f'VM with id: {_id} not found'

				return Result(errors=errors)

		return Result(errors=None, data=data)

	def get_vm_by_name(self, name):
		pass

	def delete_vm(self, vm):
		url = f'{ORKA_IP}/resources/vm/delete'

		data = json.dumps({
		  "orka_vm_name": f"{vm.name}",
		})
		headers = {
		  'Content-Type': 'application/json',
		  'Authorization': f'Bearer {self.token}'
		}

		r = requests.delete(url, headers=headers, data=data)
		content = json.loads(r._content.decode('utf-8'))
		errors = content.get('errors')
		
		return Result(errors=errors)


############# Image Management ###############

	def save_vm_as_image(self, image_name, vm):
		url = f"{ORKA_IP}/resources/image/save"
		headers = {
			'Content-Type': 'application/json', 
			'Authorization': f"Bearer {self.token}"
			}
		data = json.dumps({
			'orka_vm_name': vm.id,
			'new_name': image_name
		})
		r = requests.post(url, headers=headers, data=data)
		content = json.loads(r._content.decode('utf-8'))
		errors = content.get('errors')
		
		return Result(errors=errors)

	def commit_vm_state_to_base_image(self, vm):
		url = f'{ORKA_IP}/resources/image/commit'
		data = json.dumps({
		  "orka_vm_name": f"{vm.id}"
		})
		headers = {
		  'Content-Type': 'application/json',
		  'Authorization': f'Bearer {self.token}'
		}
		r = requests.post(url, headers=headers, data=data)
		content = json.loads(r._content.decode('utf-8'))
		errors = content.get('errors')
		
		return Result(errors=errors)
