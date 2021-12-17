from orka_sdk import OrkaSDK

orka = OrkaSDK()

# should have an auth section in the docs to explain 
# orka-license-key
r = orka.login('jeff.d.vincent@gmail.com', '123456')
# print(r.errors)
# print(orka.token)

# vm_data = {
# 	'vm_name': 'fake-name',
# 	'orka_base_image': '90GBigSurSSH.img',
# 	'core_count': '3',
# 	'vcpu_count': '3'
# }

# vm = orka.create_vm(vm_data)

######################################################################
### Notes for docs: create_vm should get its own section in the docs. 
### it is a convenience wrapper for create_vm_config() and deploy_vm_config()
### and is one of two methods that returns a VM instance.
##########################################################################

# r = orka.save_vm_as_image('new-image-name1.img', vm)

# ### r is an instance of the class Result

# if r.success:
# 	print('Successfully saved image.')
# else:
# 	print('Failed to save image.\nErrors:\n ')
# 	for e in r.errors:
# 		print(f'{e}\n\n')

# cmd = 'printenv'
# output = vm.exec(cmd)

# print(output)

result = orka.list_session_vms()
print(result.errors)
if result.success:
	for vm in result.data:
		output = vm.exec('printenv')
		print(output)


