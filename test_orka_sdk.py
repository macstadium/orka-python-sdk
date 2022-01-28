import json
from unittest.mock import patch
import pytest
from orka_sdk import OrkaSDK
import sample_data

class MockResponse:
	def __init__(self, content):
		self._content = json.dumps(content).encode('utf-8')


@patch.object(OrkaSDK, '_get_token')
def test_login(a_mock):
	a_mock.return_value = 'fake-token'
	orka = OrkaSDK()
	user = 'user'
	password = 'password'
	license_key = 'license-key'
	r = orka.login(user, password, license_key)
	assert orka.token == 'fake-token'
	assert r.success == True

@patch('orka_sdk.requests.get')
def test_list_system_vms(a_mock):
	a_mock.return_value = MockResponse(sample_data.list_vms_response)
	orka = OrkaSDK()
	orka.license_key = 'fake-key'
	r = orka.list_system_vms()
	assert r.errors == None
	assert type(r.data) == list
	assert r.data[0].name == 'myorkavm'

@patch('orka_sdk.requests.get')
def test_get_vm_by_id(a_mock):
	a_mock.return_value = MockResponse(sample_data.list_vms_response)
	orka = OrkaSDK()
	orka.license_key = 'license-key'
	r = orka.get_vm_by_id('05ca969973999')
	assert r.errors == None
	assert r.data.name == 'myorkavm'

@patch('orka_sdk.requests.post')
def test_create_vm_config(a_mock):
	a_mock.return_value = MockResponse(sample_data.create_vm_config_response)
	orka = OrkaSDK()
	orka.license_key = 'license-key'
	config_data = {
	'vm_name': 'myorkavm',
	'orka_base_image': 'fake.img',
	'core_count': '6',
	'vcpu_count': '6'
	}
	r = orka.create_vm_config(config_data)
	assert r.success == True
	assert not r.errors

@patch('orka_sdk.requests.post')
def test_deploy_vm_config(a_mock):
	a_mock.return_value = MockResponse(sample_data.deploy_vm_config_response)
	orka = OrkaSDK()
	orka.license_key = 'license-key'
	vm_name = 'myorkavm'
	vm_metadata = {'sample_data': 'stuff'}
	r = orka.deploy_vm_config(vm_name, vm_metadata)
	assert r.success == True
	assert not r.errors
	assert r.data.name == 'myorkavm'

@patch('orka_sdk.requests.get')
@patch('orka_sdk.requests.post')
def test_save_vm_as_image(post_mock, get_mock):
	post_mock.return_value = MockResponse(sample_data.save_vm_as_image_response)
	get_mock.return_value = MockResponse(sample_data.list_vms_response)
	orka = OrkaSDK()
	orka.license_key = 'license-key'
	r = orka.list_system_vms()
	vm = r.data[0]
	image_name = 'fake.img'
	r = orka.save_vm_as_image(image_name, vm)
	assert r.success == True
	assert not r.errors

@patch('orka_sdk.requests.get')
@patch('orka_sdk.requests.post')
def test_commit_vm_state_to_base_image(post_mock, get_mock):
	post_mock.return_value = MockResponse(sample_data.commit_vm_state_to_base_image_response)
	get_mock.return_value = MockResponse(sample_data.list_vms_response)
	orka = OrkaSDK()
	orka.license_key = 'license-key'
	r = orka.list_system_vms()
	vm = r.data[0]
	r = orka.commit_vm_state_to_base_image(vm)
	assert r.success == True
	assert not r.errors
