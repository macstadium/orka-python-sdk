from orka_sdk import OrkaSDK

orka = OrkaSDK()

# should have an auth section in the docs to explain 
# orka-license-key
orka.login(
	user='jeff.d.vincent@gmail.com', 
	password='123456',
	license_key='Yq1nIWe7pwgPtAhzCatSeYqq')

vm_data = {
	'vm_name': 'fake-name',
	'orka_base_image': 'new-image.img',
	'core_count': '3',
	'vcpu_count': '3'
}

# r = orka.create_vm(vm_data)    # r is an instance of the class Result
# if r.success:
# 	vm = r.data    # vm is an instance of the class VM
# else:
# 	print(r.errors)

r = orka.list_session_vms()
if r.success:
	for vm in r.data:
		print(vm.name)

# # r = orka.save_vm_as_image('new-image.img', vm)    # r is an instance of the class Result
# # if r.success:
# # 	print('Successfully saved image.')
# # else:
# # 	print('Failed to save image.\nErrors:')
# # 	for e in r.errors:
# # 		print(f'{e}\n')

# cmd = 'export TEST_VALUE=success'
# r = vm.exec(cmd)
# if r.success:
# 	print(r.data['stdout'])
# else:
# 	print(r.data['stderr'])
# 	print(r.errors)


# r = orka.commit_vm_state_to_base_image(vm)

# r = orka.delete_vm(vm)
# print(r.errors)

# r = orka.create_vm(vm_data)    # r is an instance of the class Result
# if r.success:
# 	vm = r.data    # vm is an instance of the class VM
# else:
# 	print(r.errors)


# cmd = 'printenv'
# r = vm.exec(cmd)
# print(r.data['stdout'])

# r = orka.list_system_vms()
# if r.success:
# 	for vm in r.data:
# 		r = vm.exec('printenv')
# 		try:
# 			print(r.data['stdout'])
# 		except:
# 			print(f'VM {vm.name} is not deployed.\n')
# else:
# 	print(r.errors)


# r = orka.list_system_vms()
# for vm in r.data:
# 	try:
# 		r = vm.exec('printenv')
# 		print(r.data['stdout'])
# 	except:
# 		print(vm.name)
# 		pass

r = orka.get_vm_by_id('2db81bb93f67f')
if r.success:
	vm = r.data
	print(vm.id)