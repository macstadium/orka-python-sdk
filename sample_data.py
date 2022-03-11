list_vms_response = {
  "message": "",
  "help": {},
  "errors": [],
  "virtual_machine_resources": [
    {
      "virtual_machine_name": "myorkavm",
      "vm_deployment_status": "Deployed",
      "status": [
        {
          "owner": "user@email.com",
          "virtual_machine_name": "myorkavm",
          "virtual_machine_id": "05ca969973999",
          "node_location": "macpro-1",
          "node_status": "UP",
          "virtual_machine_ip": "10.221.188.4",
          "vnc_port": "5999",
          "screen_sharing_port": "5900",
          "ssh_port": "8822",
          "cpu": 12,
          "vcpu": 12,
          "gpu": "true",
          "RAM": "30G",
          "base_image": "Catalina.img",
          "image": "myorkavm",
          "configuration_template": "default",
          "vm_status": "running",
          "io_boost": "false",
          "use_saved_state": "false",
          "reserved_ports": [
            {
              "host_port": 5999,
              "guest_port": 5999,
              "protocol": "TCP"
            },
            {
              "host_port": 5900,
              "guest_port": 5900,
              "protocol": "TCP"
            },
            {
              "host_port": 8822,
              "guest_port": 8821,
              "protocol": "TCP"
            }
          ],
          "creationTimestamp": "2020-07-28T11:09:25Z"
        }
      ]
    },
    {
      "virtual_machine_name": "myorkavm1",
      "vm_deployment_status": "Not Deployed",
      "owner": "newUser@email.com",
      "cpu": 12,
      "vcpu": 12,
      "base_image": "Catalina.img",
      "image": "myorkavm1",
      "io_boost": "false",
      "use_saved_state": "false",
      "gpu_passthrough": "false",
      "configuration_template": "default"
    }
  ]
}

create_vm_config_response = {
  "message": "Successfully Created",
  "help": {
    "deploy_virtual_machine": "To deploy a VM, make sure you have a configuration created and use the endpoint http://10.221.188.100/resources/vm/deploy",
    "required_request_data_for_deploy": {
      "orka_vm_name": "myorkavm",
      "orka_node_name": "macpro-1"
    }
  },
  "errors": []
}

deploy_vm_config_response = {
  "message": "Successfully deployed VM",
  "help": {
    "start_virtual_machine": "To start a VM send rest request to http://10.221.188.100/resources/vm/exec/start",
    "stop_virtual_machine": "To stop a VM send rest request to http://10.221.188.100/resources/vm/exec/stop",
    "resume_virtual_machine": "To resume a VM send rest request to http://10.221.188.100/resources/vm/exec/resume",
    "suspend_virtual_machine": "To suspend a VM send rest request to http://10.221.188.100/resources/vm/exec/suspend",
    "data_for_virtual_machine_exec_tasks": {
      "orka_vm_name": "myorkavm"
    },
    "virtual_machine_vnc": "Once started and deployed, you can use VNC to access it via 10.221.188.4:6000"
  },
  "errors": [],
  "ram": "15G",
  "vcpu": "6",
  "host_cpu": "6",
  "ip": "10.221.188.4",
  "ssh_port": "8823",
  "screen_share_port": "5901",
  "vm_id": "05ca969973999",
  "port_warnings": [],
  "io_boost": "false",
  "use_saved_state": "false",
  "gpu_passthrough": "false",
  "vnc_port": "6000"
}

save_vm_as_image_response = {
  "message": "saved",
  "help": {},
  "errors": []
}

commit_vm_state_to_base_image_response = {
  "message": "committed",
  "help": {},
  "errors": []
}

check_node_status_response = {
  "message": "",
  "help": {},
  "errors": [],
  "node_status": {
    "status": "READY",
    "cpu": "24",
    "gpu": 1,
    "memory": "60G",
    "nodeName": "macpro-1",
    "sandbox": "false"
  }
}

list_nodes_response = {
  "message": "",
  "help": {
    "check_orka_node_status": "To check orka node status for a single node use endpoint http://10.221.188.100/resources/node/status/<NODE_NAME>",
    "create_virtual_machine_configuration": "To create a virtual machine configuration, please use the endpoint http://10.221.188.100/resources/vm/create",
    "required_request_data_for_create": {
      "orka_vm_name": "<ORKA_VM_NAME>",
      "orka_base_img": "<ORKA_BASE_IMG>",
      "orka_image": "<ORKA_IMAGE>"
    },
    "deploy_virtual_machine": "To deploy a virtual machine node, make sure you have a configuration created and use the endpoint http://10.221.188.100/resources/vm/deploy",
    "required_request_data_for_deploy": {
      "orka_vm_name": "<ORKA_VM_NAME>",
      "orka_node_name": "<ORKA_NODE_NAME>"
    }
  },
  "errors": [],
  "nodes": [
    {
      "name": "macpro-1",
      "host_name": "macpro-1",
      "address": "10.221.188.4",
      "hostIP": "10.221.188.4",
      "available_cpu": 17,
      "allocatable_cpu": 24,
      "available_gpu": "1",
      "allocatable_gpu": "1",
      "available_memory": "47.49G",
      "total_cpu": 24,
      "total_memory": "62.92G",
      "state": "READY",
      "orka_tags": []
    },
    {
      "name": "macpro-2",
      "host_name": "macpro-2",
      "address": "10.221.188.5",
      "hostIP": "10.221.188.5",
      "available_cpu": 23,
      "allocatable_cpu": 24,
      "available_gpu": "1",
      "allocatable_gpu": "1",
      "available_memory": "62.23G",
      "total_cpu": 24,
      "total_memory": "62.92G",
      "state": "READY",
      "orka_group": "myUserGroup",
      "orka_tags": []
    },
    {
      "name": "macpro-3",
      "host_name": "macpro-3",
      "address": "10.221.188.6",
      "hostIP": "10.221.188.6",
      "available_cpu": 12,
      "allocatable_cpu": 24,
      "available_gpu": "1",
      "allocatable_gpu": "1",
      "available_memory": "23.72G",
      "total_cpu": 24,
      "total_memory": "62.92G",
      "state": "READY",
      "orka_group": "myUserGroup",
      "orka_tags": []
    },
    {
      "name": "mini-arm-15",
      "host_name": "mini-arm-15",
      "address": "10.221.188.15",
      "hostIP": "10.221.188.15",
      "available_cpu": 8,
      "allocatable_cpu": 8,
      "available_gpu": "N/A",
      "allocatable_gpu": "N/A",
      "available_memory": "15.39G",
      "total_cpu": 8,
      "total_memory": "15.39G",
      "state": "READY",
      "orka_tags": []
    },
    {
      "name": "mini-arm-16",
      "host_name": "mini-arm-16",
      "address": "10.221.188.16",
      "hostIP": "10.221.188.16",
      "available_cpu": 8,
      "allocatable_cpu": 8,
      "available_gpu": "N/A",
      "allocatable_gpu": "N/A",
      "available_memory": "15.39G",
      "total_cpu": 8,
      "total_memory": "15.39G",
      "state": "READY",
      "orka_tags": []
    }
  ]
}

list_images_response = {
  "message": "",
  "help": {},
  "errors": [],
  "image_attributes": [
    {
      "image": "Monterey.orkasi",
      "image_size": "90G",
      "modified": "2022-02-10T10:54:28.842Z",
      "date_added": "2022-01-28T15:44:32.156Z",
      "owner": "all"
    },
    {
      "image": "Mojave-Clean.img",
      "image_size": "17G",
      "modified": "2019-09-16T14:49:48.088Z",
      "date_added": "2019-11-11T23:03:58.560Z",
      "owner": "all"
    },
    {
      "image": "Mojave-Jenkins.img",
      "image_size": "17G",
      "modified": "2019-08-11T06:09:56.821Z",
      "date_added": "2019-11-11T23:03:58.564Z",
      "owner": "all"
    },
    {
      "image": "Mojave.img",
      "image_size": "17G",
      "modified": "2019-08-14T14:25:44.282Z",
      "date_added": "2019-11-11T23:03:58.567Z",
      "owner": "all"
    },
    {
      "image": "empty.img",
      "image_size": "193k",
      "modified": "2019-11-22T10:37:49.000Z",
      "date_added": "2019-11-22T10:37:50.154Z",
      "owner": "all"
    }
  ],
  "images": [
    "Monterey.orkasi",
    "Mojave-Clean.img",
    "Mojave-Jenkins.img",
    "Mojave.img",
    "empty.img"
  ]
}

delete_image_response = {
  "message": "Successfully deleted: Catalina.img",
  "help": {},
  "errors": []
}