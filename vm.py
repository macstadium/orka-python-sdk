import paramiko
import time

from result import Result

class VM():

	def __init__(self, data):
		time.sleep(15)
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
		self.sftp_client = None
		self.ssh_user = 'admin'
		self.ssh_pass = 'admin'

	def _connect_ssh_client(self):
		self.ssh_client.connect(
		self.ip, username=self.ssh_user, 
		password=self.ssh_pass, 
		port=self.ssh_port, 
		look_for_keys=False, 
		timeout=60, 
		allow_agent=False)

	def exec(self, cmd):
		output = {}
		try:
			self._connect_ssh_client()
		except Exception as e:

			return Result(errors=[str(e)])
		try:	
			stdin, stdout, stderr = \
				self.ssh_client.exec_command(cmd)
			stdin.write(f'{self.ssh_pass}\n')
			stdin.flush()
		except Exception as e:

			return Result(errors=[str(e)])

		output['stdout'] = stdout.read().decode("utf8")
		output['stderr'] = stderr.read().decode("utf8")
		stdin.close()
		stdout.close()
		stderr.close()

		return Result(errors=None, data=output)

	def _create_sftp_client(self):
		# only to be called after _connect_ssh_client()
		self.sftp_client = self.ssh_client.open_sftp()

	def upload(self, local_path, dest_path):
		try:
			self._connect_ssh_client()
			self._create_sftp_client()
		except Exception as e:

			return Result(errors=[str(e)])
		try:
			self.sftp_client.put(
				local_path, dest_path)
		except Exception as e:

			return Result(errors=[str(e)])

		return Result(errors=None)

	def download(self, dest_path, local_path):
		try:
			self._connect_ssh_client()
			self._create_sftp_client()
		except Exception as e:

			return Result(errors=[str(e)])
		try:
			self.sftp_client.get(
				dest_path, local_path)
		except Exception as e:

			return Result(errors=[str(e)])

		return Result(errors=None)

	def write_persistent_env_var(self, data, dest=None):
		dest_text = ''
		exports = []
		if not dest:
			dest = '/Users/admin/.bash_profile'

		for var, value in data.items():
			export = f'export {var}={value}\n'
			exports.append(export)

		# if the file exists already, read its contents
		r = self.exec(f'cat {dest}')
		if r.errors:

			return r
		if r.data['stdout']:
			dest_text = r.data['stdout']

		# write the temp file locally
		with open('environment.temp', 'w') as temp_file:
			temp_file.write(dest_text)
			# sloppily append exports to end for now
			for export in exports:
				temp_file.write(export)
		r = self.upload('environment.temp', dest)

		return r

	def enable_auto_login(self):
		cmd = (f'sudo -S -p "" defaults write' 
			f' /Library/Preferences/com.apple.loginwindow.plist' 
			f' autoLoginUser {self.ssh_user}')
		r = self.exec(cmd)
		if r.errors:

			return r
		cmd = (f'sudo -S -p "" plutil -replace autoLoginUser -string'
			f' {self.ssh_user} /Library/Preferences/com.apple.loginwindow.plist')
		r = self.exec(cmd)
		if r.errors:

			return r
		cmd = (f'sudo -S -p "" /usr/libexec/PlistBuddy -c "Set autoLoginUser' 
			f' {self.ssh_user}" /Library/Preferences/com.apple.loginwindow.plist')
		r = self.exec(cmd)

		return r