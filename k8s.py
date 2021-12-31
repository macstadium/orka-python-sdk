import os
import requests
import yaml
from pathlib import Path
from kubernetes import client, config
from result import Result


class K8s:

	def __init__(self, base_sdk, config_path=None):
		self.token = base_sdk.token
		self.user = base_sdk.user
		self.password = base_sdk.password
		self.license_key = base_sdk.license_key
		self.orka_ip = base_sdk.orka_ip
		if config_path:
			config.load_kube_config(config_path)
			self.client = client.AppsV1Api()
			
			return None
		home = str(Path.home())
		config_path = \
			os.path.join(home, 'kubeconfig-orka')
		if os.path.exists(config_path):
			config.load_kube_config(config_path)
			self.client = client.AppsV1Api()
		else:
			self.client = None

	def create_deployment(self, yaml_path):
		with open(yaml_path) as f:
			deployment = yaml.safe_load(f)
			r = self.client.create_namespaced_deployment(
				body=deployment, namespace='sandbox')
