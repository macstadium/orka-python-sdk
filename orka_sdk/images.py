import json
from orka_sdk.result import Result


class Images:

	def __init__(self, base_sdk):
		self.token = base_sdk.token
		self.user = base_sdk.user
		self.password = base_sdk.password
		self.license_key = base_sdk.license_key
		self.orka_ip = base_sdk.orka_ip

	def list(self):
		url = f'{self.orka_ip}/resources/image/list'
		headers = {
			'Authorization': f'Bearer {self.token}'
			}
		r = requests.get(url, headers=headers)
		content = json.loads(r._content.decode('utf-8'))
		errors = content.get('errors')
		if errors:

			return Result(errors=errors)
		data = content['image_attributes']
		
		return Result(errors=errors, data=data)

	def get(self, image_name):
		url = f'{self.orka_ip}/resources/image/list'
		headers = {
			'Authorization': f'Bearer {self.token}'
			}
		r = requests.get(url, headers=headers)
		content = json.loads(r._content.decode('utf-8'))
		errors = content.get('errors')
		if errors:

			return Result(errors=errors)
		data = content['image_attributes']

		for i in data:
			if i['image'] == image_name:
				image = i

		return Result(errors=None, data=image)

	def delete(self, image_name):
		url = f'{self.orka_ip}/resources/image/delete'
		headers = {
			'Authorization': f'Bearer {self.token}'
			}
		data = json.dumps({'image': image_name})
		r = requests.post(url, headers=headers, data=data)
		content = json.loads(r._content.decode('utf-8'))
		errors = content.get('errors')
		
		return Result(errors=errors)
		