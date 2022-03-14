# orka-python-sdk
An SDK for interacting with Orka clusters and the macOS VMs they run.

## Contents
 - [Installation](#installation)
 - [Authentication](#authentication)
 - [VM Management](#vm-management)
 	- [VM Instances](#vm-instances)
 		- [Properties](#vm-properties)
 		- [Methods](#vm-methods)
 - [Images](#image-management)
 - [Nodes](#node-management)
 - [k8s](#k8s-management)
 - [CI/CD Integrations](#cicd-integrations)
 	- [GitHub Actions](#github-actions-controller)

## Installation
```shell
pip install orka_sdk
```
## Authentication
#### Get token
```python
from orka_sdk.orka_sdk import OrkaSDK

orka = OrkaSDK()
orka.login(user='user@email.com', password='password',license_key='license-key')
```
#### Revoke token
```python
orka.revoke_token()
```
## VM Management
#### Define and create a VM
```python
# Define a VM
vm_data = {
	'vm_name': 'fake-name',
	'orka_base_image': 'my-image.img',
	'core_count': '3',
	'vcpu_count': '3'
	}

# Create a VM
r = orka.create_vm(vm_data)  
vm = r.data
```
#### Get VM by id
```python
r = orka.get_vm_by_id('<vm_id>')
vm = r.data
```
#### Get VM by name
```python
r = orka.get_vm_by_name('<vm_name>')
vm = r.data
```
#### Iterate over all VMs in system and execute a remote command on each
```python
r = orka.list_system_vms()
for vm in r.data:
	r = vm.exec('printenv')
```
#### Commit current state of deployed VM to base image and clean up
```python
orka.commit_vm_state_to_base_image(vm)
orka.purge_vm(vm)
```
#### Save a deployed VM's state as an Image
```python
r = orka.save_vm_as_image('new-image.img', vm)
```
#### Commit VM state to base image
```python
r = orka.commit_vm_state_to_base_image()
```
#### Purge VM
```python
r = orka.purge_vm(vm)
```
#### Delete VM
```python
r = orka.delete_vm(vm)
```
#### Start VM
```python
r = orka.start_vm(vm)
```
#### Stop VM
```python
r = orka.stop_vm(vm)
```
#### Suspend VM
```python
r = orka.suspend_vm(vm)
```
#### Resume VM
```python
r = orka.resume_vm(vm)
```
#### Revert VM
```python
r = orka.revert_vm(vm)
```
#### Get VM status
```python
r = orka.get_vm_status(vm)
```
## VM Instances
### VM Properties
|Name | Description|
|-----|------|
|`ip` | The ip address of the deployed VM|
|`name` | The VM's name|
|`ssh_port`| The VM's ssh port|
|`id`| The VM's unique id |
|`ram`| Available RAM |
|`vcpu`| Virtual CPU count |
|`cpu`| CPU count |
|`io_boost`| I/O boost enabled |
|`use_saved_state`| Used saved VM state at boot |
|`gpu_passthrough`| GPU passthrough to host Node GPU enabled |
|`screen_share_port`| The VM's screen share port |
|`vnc_port`| The VM's vnc port |
|`ssh_client`| [Paramiko](https://docs.paramiko.org/en/stable/) ssh client associated with the VM |
|`sftp_client`| [Paramiko](https://docs.paramiko.org/en/stable/) ssh client associated with the VM |
|`ssh_user`| The SSH user associated with the VM |
|`ssh_pass`| The SSH password associated with the VM |

### VM Methods
#### `upload()`
Upload a file to a deployed VM
```python
local_path = '/local/file/path'
dest_path = '/remote/file/path'

# Upload file
r = vm.upload(local_path, dest_path)

# Confirm success
r = vm.exec(f'cat {dest_path}')
print(r.data['stdout'])
```
#### `download()`
Download a file from a deployed VM
```python
remote_path = '/remote/file/path'
local_path = '/local/file/path'
r = vm.download(remote_path, local_path)
```
#### `exec()`
Execute a remote command on a deployed VM
```python
r = vm.exec('printenv')
print(r.data['stdout'])
```
#### `write_persistent_env_var()`
Write an env var export statement to a deployed VM's `.zshenv` or elsewhere
```python
data = {'FOO': 'bar'}
r = vm.write_persistent_env_var(data)
```
Alternatively, you can also pass a destination filepath, like so:
```python
dest = '/Users/admin/.bash_profile'
data = {'foo': 'bar'}
r = vm.write_persistent_env_var(data=data, dest=dest)
```
#### `enable_auto_login()`
Enable auto-login on a deployed VM
```python
r = vm.enable_auto_login()
```
#### `create_launch_daemon()`
Create a launch daemon that calls an executable at machine startup
```python
data = {'name':'my_launch_daemon', 'path_to_executable': '/path/to/executable'}
r = vm.create_launch_daemon(data)
```
#### `install_brew_packages()`
Install Homebrew packages listed in a Brewfile.
>NOTE: Homebrew must be installed on the VM
```python
file_path = '/path/to/Brewfile'
r = vm.install_brew_packages(file_path)
```
## K8s Management
#### Deploy a k8s service 
```python
orka.k8s.create_service('<path/to/yaml/definition>')
```
#### Delete a k8s service
```python
orka.k8s.delete_service('<service_name>')
```
### Create a k8s deployment
```python
orka.k8s.create_deployment('<path/to/yaml/definition>')
```
#### Delete a k8s deployment
```python
orka.k8s.delete_deployment('<deployment_name>')
```
## Image Management
#### List images
```python
r = orka.images.list()
```
#### Get image by name
```python
r = orka.images.get('<image_name>')
```
#### Delete image
```python
r = orka.images.delete('<image_name>')
```
## Node Management 
#### List nodes
```python
r = orka.nodes.list()
```
#### Get node status
```python
r = orka.nodes.get_status('<node_name>')
```

## CI/CD Integrations
### GitHub Actions Controller
```python
from orka_sdk.gha_controller import GHAController

controller = GHAController()

controller.spin_up()
controller.check_runner_status()
controller.tear_down()
```
