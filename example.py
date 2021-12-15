from orka_sdk import OrkaSDK

orka = OrkaSDK()
orka.login('jeff.d.vincent@gmail.com', '123456')
print(orka.token)

vm_data = {
	'vm_name': 'fake-name',
	'orka_base_image': '90GBigSurSSH.img',
	'core_count': '3',
	'vcpu_count': '3'
}

vm = orka.create_vm(vm_data)
print(vm.name)

image = vm.save_as_image('image_name')

cmd = 'echo Hello World'

output = vm.exec(cmd)
print(output['stdout'])
print(output['stderr'])

vm.delete()
orka.revoke_token()
