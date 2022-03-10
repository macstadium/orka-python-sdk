from unittest.mock import patch
from test_orka_sdk import MockResponse
from orka_sdk.orka_sdk import OrkaSDK
import sample_data


@patch.object(OrkaSDK, '_get_token')
@patch('orka_sdk.nodes.requests.get')
def test_list(a_mock, b_mock):
	pass

@patch.object(OrkaSDK, '_get_token')
@patch('orka_sdk.nodes.requests.get')
def test_get(a_mock, b_mock):
	pass 

@patch.object(OrkaSDK, '_get_token')
@patch('orka_sdk.nodes.requests.post')
def test_delete(a_mock, b_mock):
	pass