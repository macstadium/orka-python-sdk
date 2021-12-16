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

