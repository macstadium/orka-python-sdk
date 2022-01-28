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