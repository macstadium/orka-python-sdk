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
			try:
				config.load_kube_config(config_path)
				self.client = client.AppsV1Api()

				return None
			except Exception as e:
				errors = [str(e)]
				print('Failed to create Kubernetes client.')
				print(errors[0])
				self.client = None
				
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
			try:
				r = self.client.create_namespaced_deployment(
					body=deployment, namespace='sandbox')
			except Exception as e:
				errors = [str(e)]

				return Result(errors=errors)
			
			return r

	def delete_deployment(self, name):
		try:
			r = self.client.delete_namespaced_deployment(
				name=name,
				namespace="sandbox",
				body=client.V1DeleteOptions(
					propagation_policy="Foreground",
					grace_period_seconds=5
				)
		  	)
		except Exception as e:
			errors = [str(e)]

			return Result(errors=errors)

		return r

	def create_service(self, yaml_path):
		with open(yaml_path) as f:
			service = yaml.safe_load(f)
			try:
				r = self.client.create_namespaced_service(
					body=service, namespace='sandbox')
			except Exception as e:
				errors = [str(e)]

				return Result(errors=errors)
			
			return r

	def delete_service(self, name):
		try:
			r = self.client.delete_namespaced_service(
				name=name,
				namespace="sandbox",
				body=client.V1DeleteOptions(
					propagation_policy="Foreground",
					grace_period_seconds=5
				)
		  	)
		except Exception as e:
			errors = [str(e)]

			return Result(errors=errors)

		return r