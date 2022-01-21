import json
import os
import random
import requests
import string
import time
from orka_sdk import OrkaSDK

class GHAController:

	def __init__(self):
		self.orka_user = os.environ.get('ORKA_USER')
		self.password = os.environ.get('ORKA_PASS')
		self.license_key = os.environ.get('ORKA_LICENSE_KEY')
		self.github_user = os.environ.get('GH_USER')
		self.github_pat = os.environ.get('GH_PAT')
		self.github_repo_name = os.environ.get('GH_REPO')
		self.core_count = os.environ.get('CORE_COUNT')
		self.vcpu_count = os.environ.get('VCPU_COUNT')
		self.gh_session = requests.Session()
		self.gh_session.auth = (self.github_user, self.github_pat)
		self.orka = OrkaSDK()
		self.orka.login(
			user=self.orka_user, 
			password=self.password, 
			license_key=self.license_key)
		self.vm = None
		self.vm_name = None
		self.runner_id = None

	def _generate_runner_name(self):
		pool = string.ascii_lowercase
		self.vm_name = ''.join(random.choice(pool) for i in range(10))

	def spin_up(self):
		self._generate_runner_name()
		if not self.core_count:
			self.core_count = '6'
		if not self.vcpu_count:
			self.vcpu_count = '6'
		vm_data = {
			'vm_name': self.vm_name,
			'orka_base_image': 'gha.img',
			'core_count': self.core_count,
			'vcpu_count': self.vcpu_count
		}

		vm_metadata = {
			'github_user': self.github_user,
			'github_pat': self.github_pat,
			'github_repo_name': self.github_repo_name,
		}

		r = self.orka.create_vm_config(vm_data)
		if r.errors:
			for e in r.errors:
				print(e)
		r = self.orka.deploy_vm_config(
			vm_name=vm_data['vm_name'], 
			vm_metadata=vm_metadata)
		if r.errors:
			for e in r.errors:
				print(e)
		self.vm = r.data

	def check_runner_status(self):
		headers = {'Accept':'application/vnd.github.v3+json'}
		url = (f'https://api.github.com/repos/'
			f'{self.github_user}/{self.github_repo_name}/actions/runners')
		result = self.gh_session.get(url, headers=headers)
		content = json.loads(result._content.decode('utf-8'))
		for item in content['runners']:
			if self.vm_name in item['name']:
				return True
		else:
			time.sleep(4)
			# relay logs
			r = self.vm.exec('cat /Users/admin/runner-connect.log')
			print(r.data['stdout'])
			self.check_runner_status()

	def tear_down(self):
		self.orka.delete_vm(self.vm)
		self._get_runner_id()
		self._remove_runner_from_gh()

	def _get_runner_id(self):
		headers = {'Accept':'application/vnd.github.v3+json'}
		url = (f'https://api.github.com/repos/{self.github_user}'
			f'/{self.github_repo_name}/actions/runners')
		result = self.gh_session.get(url, headers=headers)
		content = json.loads(result._content.decode('utf-8'))
		for item in content['runners']:
			if self.vm_name in item['name']:
				self.runner_id = item['id']

	def _remove_runner_from_gh(self):
		headers = {'Accept':'application/vnd.github.v3+json'}
		url = (f'https://api.github.com/repos/{self.github_user}'
			f'/{self.github_repo_name}/actions/runners/{self.runner_id}')
		self.gh_session.delete(url,headers=headers)
