from unittest.mock import patch
from test_orka_sdk import MockResponse
from orka_sdk.orka_sdk import OrkaSDK
import sample_data


@patch.object(OrkaSDK, '_get_token')
@patch('orka_sdk.nodes.requests.get')
def test_list(a_mock, b_mock):
	a_mock.return_value = MockResponse(sample_data.list_images_response)
	b_mock.return_value = 'fake-token'
	orka = OrkaSDK()
	r = orka.login('fake-user', 'fake-pass', 'fake-key')
	r = orka.images.list()
	assert r.data[0]['image'] == 'Monterey.orkasi'

@patch.object(OrkaSDK, '_get_token')
@patch('orka_sdk.nodes.requests.get')
def test_get(a_mock, b_mock):
	a_mock.return_value = MockResponse(sample_data.list_images_response)
	b_mock.return_value = 'fake-token'
	orka = OrkaSDK()
	r = orka.login('fake-user', 'fake-pass', 'fake-key')
	r = orka.images.get('Monterey.orkasi')
	assert r.data['image'] == 'Monterey.orkasi'
	assert r.data['image_size'] == '90G'

@patch.object(OrkaSDK, '_get_token')
@patch('orka_sdk.nodes.requests.post')
def test_delete(a_mock, b_mock):
	a_mock.return_value = MockResponse(sample_data.delete_image_response)
	b_mock.return_value = 'fake-token'
	orka = OrkaSDK()
	r = orka.login('fake-user', 'fake-pass', 'fake-key')
	r = orka.images.delete('Catalina.img')
	assert r.errors == []
