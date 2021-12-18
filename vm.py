import paramiko
import time

from result import Result

class VM():

	def __init__(self, data):
		self.ip = data['ip']
		self.name = data['name']
		self.ssh_port = data['ssh_port']
		self.id = data['id']
		self.ram = data['ram']
		self.vcpu = data['vcpu']
		self.cpu = data['cpu']
		self.io_boost = data['io_boost']
		self.use_saved_state = data['use_saved_state']
		self.gpu_passthrough = data['gpu_passthrough']
		self.screen_share_port = data['screen_share_port']
		self.vnc_port = data['vnc_port']
		self.ssh_client = paramiko.SSHClient()
		self.ssh_client.set_missing_host_key_policy(
			paramiko.AutoAddPolicy())
		self.ssh_user = 'admin'
		self.ssh_pass = 'admin'

	def exec(self, cmd):
		output = {}
		ssh_port = self.ssh_port
		ssh_user = self.ssh_user
		ssh_pass = self.ssh_pass

		time.sleep(15)

		try:
			self.ssh_client.connect(
				self.ip, username=self.ssh_user, 
				password=self.ssh_pass, 
				port=ssh_port, 
				look_for_keys=False, 
				timeout=60, 
				allow_agent=False
				)
		except Exception as e:
			return Result(errors=str(e))

		try:	
			stdin, stdout, stderr = \
				self.ssh_client.exec_command(cmd)
		except Exception as e:
			return Result(errors=str(e))
		
		output['stdout'] = stdout.read().decode("utf8")
		output['stderr'] = stderr.read().decode("utf8")
		
		stdin.close()
		stdout.close()
		stderr.close()

		return Result(errors=None, data=output)
