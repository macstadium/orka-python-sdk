from unittest.mock import patch
from test_orka_sdk import MockResponse
from orka_sdk.orka_sdk import OrkaSDK
import sample_data

@patch.object(OrkaSDK, '_get_token')
@patch('orka_sdk.nodes.requests.get')
def test_list(a_mock, b_mock):
	a_mock.return_value = MockResponse(sample_data.list_nodes_response)
	b_mock.return_value = 'fake-token'
	orka = OrkaSDK()
	r = orka.login('fake-user', 'fake-pass', 'fake-key')
	r = orka.nodes.list()
	assert r.data[0]['name'] == 'macpro-1'
	assert r.errors == []

@patch.object(OrkaSDK, '_get_token')
@patch('orka_sdk.nodes.requests.get')
def test_get_status(a_mock, b_mock):
	a_mock.return_value = MockResponse(sample_data.check_node_status_response)
	b_mock.return_value = 'fake-token'
	orka = OrkaSDK()
	r = orka.login('fake-user', 'fake-pass', 'fake-key')
	r = orka.nodes.get_status('macpro-1')
	assert r.data['status'] == 'READY'