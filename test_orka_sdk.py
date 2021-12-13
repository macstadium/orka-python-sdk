from orka_sdk import OrkaSDK
import os

class TestOrkaSDK:

	def __init__(self):
		self.orka = OrkaSDK()
		self.user = os.environ.get('ORKA_USER')
		self.password = os.environ.get('ORKA_PASS')
		self.license_key = os.environ.get('ORKA_LICENSE_KEY')

	def test_login(self):
		self.orka.login()
		assert self.token
		assert self.user 
		assert self.password
		assert self.license_key

















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