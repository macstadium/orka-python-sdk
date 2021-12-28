import yaml
from kubernetes import client, config
from result import Result


class K8s:

	def __init__(self):
		# Configs can be set in Configuration class directly or using helper
    	# utility. If no argument provided, the config will be loaded from
    	# default location.
		try:
			self.config = config.load_kube_config()
		except Exception as e:

			return None

	def create_deployment(self, filepath):
		with open(filepath) as f:
			deployment = yaml.safe_load(f)
			k8s_apps_v1 = client.AppsV1Api()
			r = k8s_apps_v1.create_namespaced_deployment(
				body=deployment, namespace="default")
