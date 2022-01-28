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