import json
from unittest.mock import patch
import pytest
from orka_sdk import OrkaSDK

class MockResponse:
	def __init__(self):
		self._content = json.dumps({
						  "message": "",
						  "help": {},
						  "errors": [],
						  "virtual_machine_resources": [
						    {
						      "virtual_machine_name": "myorkavm",
						      "vm_deployment_status": "Deployed",
						      "status": [
						        {
						          "owner": "user@email.com",
						          "virtual_machine_name": "myorkavm",
						          "virtual_machine_id": "05ca969973999",
						          "node_location": "macpro-1",
						          "node_status": "UP",
						          "virtual_machine_ip": "10.221.188.4",
						          "vnc_port": "5999",
						          "screen_sharing_port": "5900",
						          "ssh_port": "8822",
						          "cpu": 12,
						          "vcpu": 12,
						          "gpu": "true",
						          "RAM": "30G",
						          "base_image": "Catalina.img",
						          "image": "myorkavm",
						          "configuration_template": "default",
						          "vm_status": "running",
						          "io_boost": "false",
						          "use_saved_state": "false",
						          "reserved_ports": [
						            {
						              "host_port": 5999,
						              "guest_port": 5999,
						              "protocol": "TCP"
						            },
						            {
						              "host_port": 5900,
						              "guest_port": 5900,
						              "protocol": "TCP"
						            },
						            {
						              "host_port": 8822,
						              "guest_port": 8821,
						              "protocol": "TCP"
						            }
						          ],
						          "creationTimestamp": "2020-07-28T11:09:25Z"
						        }
						      ]
						    },
						    {
						      "virtual_machine_name": "myorkavm1",
						      "vm_deployment_status": "Not Deployed",
						      "owner": "newUser@email.com",
						      "cpu": 12,
						      "vcpu": 12,
						      "base_image": "Catalina.img",
						      "image": "myorkavm1",
						      "io_boost": "false",
						      "use_saved_state": "false",
						      "gpu_passthrough": "false",
						      "configuration_template": "default"
						    }
						  ]
						}).encode('utf-8')

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
	a_mock.return_value = MockResponse()
	orka = OrkaSDK()
	orka.license_key = 'fake-key'
	r = orka.list_system_vms()
	assert r.errors == None
	assert type(r.data) == list
	assert r.data[0].name == 'myorkavm'






