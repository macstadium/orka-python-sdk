import os
from gha_controller import GHAController
from orka_sdk import OrkaSDK

ORKA_USER = os.environ.get('ORKA_USER')
ORKA_PASS = os.environ.get('ORKA_PASS')
ORKA_LICENSE_KEY = os.environ.get('ORKA_LICENSE_KEY')

orka = OrkaSDK()
orka.login(
	user=ORKA_USER,
	password=ORKA_PASS,
	license_key=ORKA_LICENSE_KEY)

# # Spin up a runner
controller = GHAController()
controller.spin_up()

# # Store the ID of the host VM
vm_id = controller.vm.id

# # Wait for the runner to register
controller.check_runner_status()
print('It\'s alive!')

##########################
# # Imaginary Job runs # #
##########################

# Get the VM by its ID
r = orka.get_vm_by_id(vm_id)
vm = r.data

controller2 = GHAController()
controller2.vm = vm
controller2.vm_name = vm.name

controller2.tear_down()
