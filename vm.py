from paramiko import SSHClient


class VM():

	def __init__(self, content):
		self.ip = content['ip']
		self.name = content['help']['data_for_virtual_machine_exec_tasks']['orka_vm_name']
		self.ssh_client = SSHClient()
		self.ssh_user = 'admin'
		self.ssh_pass = 'admin'


	def exec(self, cmd):
		output = {}
		ssh_user = self.ssh_user
		ssh_pass = self.ssh_pass
		self.ssh_client.connect(self.ip, username=ssh_user, password=ssh_pass)
		stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
		output['stdout'] = stdout.read().decode("utf8")
		output['stderr'] = stderr.read().decode("utf8")
		stdin.close()
		stdout.close()
		stderr.close()

		return output


	def save_as_image(self, image_name):
		pass

	def commit_to_base_image(self):
		pass

	def delete(self):
		pass
