import os
from gha_controller import GHAController


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
r = controller.orka.get_vm_by_id(vm_id)
vm = r.data

controller2 = GHAController()
controller2.vm = vm

controller2.tear_down()
