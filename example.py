from orka_sdk import OrkaSDK

orka = OrkaSDK()
orka.login(
	user='user@email.com', 
	password='password',
	license_key='license-key')

# Define a VM
vm_data = {
	'vm_name': 'fake-name',
	'orka_base_image': 'new-image.img',
	'core_count': '3',
	'vcpu_count': '3'
}

# Create a VM
r = orka.create_vm(vm_data)    # r is an instance of the class Result
if r.success:
	vm = r.data    # vm is an instance of the class VM
else:
	print(r.errors)

that_one_vms_id = vm.id

# Upload a file to a deployed VM
local_path = '/home/jeffdvincent/orka-python-sdk/example.py'
dest_path = '/Users/admin/example.py'

r = vm.upload(local_path, dest_path)

if r.success:
	r = vm.exec(f'cat {dest_path}')
	print(r.data['stdout'])

# Print the name of all VMs in the system
r = orka.list_session_vms()
if r.success:
	for vm in r.data:
		print(vm.name)

# Save a deployed VM's state as an Image
r = orka.save_vm_as_image('new-image.img', vm)

# Execute a remote command on a deployed VM
cmd = 'export TEST_VALUE=success'
r = vm.exec(cmd)

# Commit current state of deployed VM to base image
r = orka.commit_vm_state_to_base_image(vm)

r = orka.delete_vm(vm)
print(r.errors)

r = orka.create_vm(vm_data)    # r is an instance of the class Result
if r.success:
	vm = r.data    # vm is an instance of the class VM
else:
	print(r.errors)

# Iterate over all VMs in system
# and execute a remote command on each
r = orka.list_system_vms()
if r.success:
	for vm in r.data:
		r = vm.exec('printenv')
else:
	print(r.errors)

# Get VM by id
r = orka.get_vm_by_id(that_one_vms_id)
if r.success:
	vm = r.data
	print(vm.id)