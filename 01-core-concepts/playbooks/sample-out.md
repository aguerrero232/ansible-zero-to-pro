# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Playbooks***: `Sample Output` ▶️

* **run** the `playbook`

```shell
 🚀  ansible-zero-to-pro/01-core-concepts/playbooks ➜ ansible-playbook playbook.yaml -i inventory.txt  
```

* **`output`**

    ```shell
    PLAY [dir setup] ********************************************************************************************************************************************************************
    TASK [Gathering Facts] **************************************************************************************************************************************************************ok: [ansible_inventory_target_3]
    ok: [ansible_inventory_target_4]
    ok: [ansible_inventory_target_1]
    ok: [ansible_inventory_target_2]
    ok: [ansible_inventory_controller_1]

    TASK [create target dir] ************************************************************************************************************************************************************changed: [ansible_inventory_target_2]
    changed: [ansible_inventory_target_4]
    changed: [ansible_inventory_target_1]
    changed: [ansible_inventory_controller_1]
    changed: [ansible_inventory_target_3]

    TASK [set env variable] *************************************************************************************************************************************************************ok: [ansible_inventory_target_1]
    ok: [ansible_inventory_target_2]
    ok: [ansible_inventory_target_3]
    ok: [ansible_inventory_target_4]
    ok: [ansible_inventory_controller_1]

    TASK [finishing dir setup] **********************************************************************************************************************************************************skipping: [ansible_inventory_target_1]
    skipping: [ansible_inventory_target_2]
    skipping: [ansible_inventory_target_3]
    skipping: [ansible_inventory_target_4]
    skipping: [ansible_inventory_controller_1]

    PLAY [commanders setup] *************************************************************************************************************************************************************
    TASK [Gathering Facts] **************************************************************************************************************************************************************ok: [ansible_inventory_controller_1]

    TASK [create commander file] ********************************************************************************************************************************************************changed: [ansible_inventory_controller_1]

    TASK [set env variable] *************************************************************************************************************************************************************ok: [ansible_inventory_controller_1]

    TASK [finishing commanders setup] ***************************************************************************************************************************************************skipping: [ansible_inventory_controller_1]

    PLAY [ships setup] ******************************************************************************************************************************************************************
    TASK [Gathering Facts] **************************************************************************************************************************************************************ok: [ansible_inventory_target_1]
    ok: [ansible_inventory_target_4]
    ok: [ansible_inventory_target_2]
    ok: [ansible_inventory_target_3]

    TASK [create ship file] *************************************************************************************************************************************************************changed: [ansible_inventory_target_3]
    changed: [ansible_inventory_target_2]
    changed: [ansible_inventory_target_1]
    changed: [ansible_inventory_target_4]

    TASK [set env variable] *************************************************************************************************************************************************************ok: [ansible_inventory_target_1]
    ok: [ansible_inventory_target_2]
    ok: [ansible_inventory_target_3]
    ok: [ansible_inventory_target_4]

    TASK [finishing ships setup] ********************************************************************************************************************************************************skipping: [ansible_inventory_target_1]
    skipping: [ansible_inventory_target_2]
    skipping: [ansible_inventory_target_3]
    skipping: [ansible_inventory_target_4]

    PLAY [commander logs] ***************************************************************************************************************************************************************
    TASK [Gathering Facts] **************************************************************************************************************************************************************ok: [ansible_inventory_controller_1]

    TASK [writing commander logs...] ****************************************************************************************************************************************************changed: [ansible_inventory_controller_1]

    TASK [reading commander logs...] ****************************************************************************************************************************************************changed: [ansible_inventory_controller_1]

    TASK [printing commander logs...] ***************************************************************************************************************************************************ok: [ansible_inventory_controller_1] => {
        "msg": {
            "changed": true,
            "cmd": [
                "cat",
                "/target_logs/ansible_inventory_controller_1-commander.txt"
            ],
            "delta": "0:00:00.003176",
            "end": "2023-01-10 19:57:28.505278",
            "failed": false,
            "msg": "",
            "rc": 0,
            "start": "2023-01-10 19:57:28.502102",
            "stderr": "",
            "stderr_lines": [],
            "stdout": "inventory_hostname: ansible_inventory_controller_1, host-name: ba95e4713698, date: 2023-01-10, time: 19:57:26, secret: 'da wey'",
            "stdout_lines": [
                "inventory_hostname: ansible_inventory_controller_1, host-name: ba95e4713698, date: 2023-01-10, time: 19:57:26, secret: 'da wey'"
            ]
        }
    }

    PLAY [ship logs] ********************************************************************************************************************************************************************
    TASK [Gathering Facts] **************************************************************************************************************************************************************ok: [ansible_inventory_target_1]
    ok: [ansible_inventory_target_2]
    ok: [ansible_inventory_target_3]
    ok: [ansible_inventory_target_4]

    TASK [writing ship logs...] *********************************************************************************************************************************************************changed: [ansible_inventory_target_3]
    changed: [ansible_inventory_target_1]
    changed: [ansible_inventory_target_2]
    changed: [ansible_inventory_target_4]

    TASK [reading ship logs...] *********************************************************************************************************************************************************changed: [ansible_inventory_target_1]
    changed: [ansible_inventory_target_2]
    changed: [ansible_inventory_target_4]
    changed: [ansible_inventory_target_3]

    TASK [printing ship logs...] ********************************************************************************************************************************************************ok: [ansible_inventory_target_1] => {
        "msg": {
            "changed": true,
            "cmd": [
                "cat",
                "/target_logs/ansible_inventory_target_1-ship.txt"
            ],
            "delta": "0:00:00.004766",
            "end": "2023-01-10 19:57:34.562059",
            "failed": false,
            "msg": "",
            "rc": 0,
            "start": "2023-01-10 19:57:34.557293",
            "stderr": "",
            "stderr_lines": [],
            "stdout": "inventory_hostname: ansible_inventory_target_1, host-name: 62ce00ad6c36, date: 2023-01-10, time: 19:57:29",
            "stdout_lines": [
                "inventory_hostname: ansible_inventory_target_1, host-name: 62ce00ad6c36, date: 2023-01-10, time: 19:57:29"
            ]
        }
    }
    ok: [ansible_inventory_target_2] => {
        "msg": {
            "changed": true,
            "cmd": [
                "cat",
                "/target_logs/ansible_inventory_target_2-ship.txt"
            ],
            "delta": "0:00:00.004265",
            "end": "2023-01-10 19:57:34.821412",
            "failed": false,
            "msg": "",
            "rc": 0,
            "start": "2023-01-10 19:57:34.817147",
            "stderr": "",
            "stderr_lines": [],
            "stdout": "inventory_hostname: ansible_inventory_target_2, host-name: fc5607898e35, date: 2023-01-10, time: 19:57:30",
            "stdout_lines": [
                "inventory_hostname: ansible_inventory_target_2, host-name: fc5607898e35, date: 2023-01-10, time: 19:57:30"
            ]
        }
    }
    ok: [ansible_inventory_target_4] => {
        "msg": {
            "changed": true,
            "cmd": [
                "cat",
                "/target_logs/ansible_inventory_target_4-ship.txt"
            ],
            "delta": "0:00:00.005692",
            "end": "2023-01-10 19:57:34.885462",
            "failed": false,
            "msg": "",
            "rc": 0,
            "start": "2023-01-10 19:57:34.879770",
            "stderr": "",
            "stderr_lines": [],
            "stdout": "inventory_hostname: ansible_inventory_target_4, host-name: bc5bf8f3cb2e, date: 2023-01-10, time: 19:57:30",
            "stdout_lines": [
                "inventory_hostname: ansible_inventory_target_4, host-name: bc5bf8f3cb2e, date: 2023-01-10, time: 19:57:30"
            ]
        }
    }
    ok: [ansible_inventory_target_3] => {
        "msg": {
            "changed": true,
            "cmd": [
                "cat",
                "/target_logs/ansible_inventory_target_3-ship.txt"
            ],
            "delta": "0:00:00.009040",
            "end": "2023-01-10 19:57:34.899401",
            "failed": false,
            "msg": "",
            "rc": 0,
            "start": "2023-01-10 19:57:34.890361",
            "stderr": "",
            "stderr_lines": [],
            "stdout": "inventory_hostname: ansible_inventory_target_3, host-name: a9808a26f2db, date: 2023-01-10, time: 19:57:30",
            "stdout_lines": [
                "inventory_hostname: ansible_inventory_target_3, host-name: a9808a26f2db, date: 2023-01-10, time: 19:57:30"
            ]
        }
    }

    PLAY [commander google nslookup] ****************************************************************************************************************************************************
    TASK [Gathering Facts] **************************************************************************************************************************************************************ok: [ansible_inventory_controller_1]

    TASK [printing nslookup test...] ****************************************************************************************************************************************************ok: [ansible_inventory_controller_1] => {
        "msg": "attempting nslookup of google.com..."
    }

    TASK [nslookup test...] *************************************************************************************************************************************************************fatal: [ansible_inventory_controller_1]: FAILED! => {"changed": false, "cmd": "nslookup google.com", "msg": "[Errno 2] No such file or directory: b'nslookup'", "rc": 2, "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}
    ...ignoring

    TASK [shell] ************************************************************************************************************************************************************************changed: [ansible_inventory_controller_1]

    TASK [saving provides command result] ***********************************************************************************************************************************************changed: [ansible_inventory_controller_1]

    TASK [printing provides command result] *********************************************************************************************************************************************ok: [ansible_inventory_controller_1] => {
        "msg": " 📦 found bind-utils-32:9.18.7, attempting to install..."
    }

    TASK [installing command package] ***************************************************************************************************************************************************changed: [ansible_inventory_controller_1]

    TASK [retry nslookup after fail and install] ****************************************************************************************************************************************changed: [ansible_inventory_controller_1]

    TASK [print nslookup result] ********************************************************************************************************************************************************ok: [ansible_inventory_controller_1] => {
        "msg": {
            "changed": true,
            "cmd": [
                "nslookup",
                "google.com"
            ],
            "delta": "0:00:00.098434",
            "end": "2023-01-10 19:57:45.249730",
            "failed": false,
            "msg": "",
            "rc": 0,
            "start": "2023-01-10 19:57:45.151296",
            "stderr": "",
            "stderr_lines": [],
            "stdout": "Server:\t\t127.0.0.11\nAddress:\t127.0.0.11#53\n\nNon-authoritative answer:\nName:\tgoogle.com\nAddress: 142.250.114.139\nName:\tgoogle.com\nAddress: 142.250.114.102\nName:\tgoogle.com\nAddress: 142.250.114.113\nName:\tgoogle.com\nAddress: 142.250.114.100\nName:\tgoogle.com\nAddress: 142.250.114.138\nName:\tgoogle.com\nAddress: 142.250.114.101\nName:\tgoogle.com\nAddress: 2607:f8b0:4023:1004::64\nName:\tgoogle.com\nAddress: 2607:f8b0:4023:1004::65\nName:\tgoogle.com\nAddress: 2607:f8b0:4023:1004::66\nName:\tgoogle.com\nAddress: 2607:f8b0:4023:1004::71",
            "stdout_lines": [
                "Server:\t\t127.0.0.11",
                "Address:\t127.0.0.11#53",
                "",
                "Non-authoritative answer:",
                "Name:\tgoogle.com",
                "Address: 142.250.114.139",
                "Name:\tgoogle.com",
                "Address: 142.250.114.102",
                "Name:\tgoogle.com",
                "Address: 142.250.114.113",
                "Name:\tgoogle.com",
                "Address: 142.250.114.100",
                "Name:\tgoogle.com",
                "Address: 142.250.114.138",
                "Name:\tgoogle.com",
                "Address: 142.250.114.101",
                "Name:\tgoogle.com",
                "Address: 2607:f8b0:4023:1004::64",
                "Name:\tgoogle.com",
                "Address: 2607:f8b0:4023:1004::65",
                "Name:\tgoogle.com",
                "Address: 2607:f8b0:4023:1004::66",
                "Name:\tgoogle.com",
                "Address: 2607:f8b0:4023:1004::71"
            ]
        }
    }

    TASK [debug] ************************************************************************************************************************************************************************skipping: [ansible_inventory_controller_1]

    TASK [debug] ************************************************************************************************************************************************************************ok: [ansible_inventory_controller_1] => {
        "msg": " 🔎  status changed..."
    }

    TASK [debug] ************************************************************************************************************************************************************************skipping: [ansible_inventory_controller_1]

    TASK [debug] ************************************************************************************************************************************************************************ok: [ansible_inventory_controller_1] => {
        "msg": " ✔️  command succeeded..."
    }

    TASK [logging commander event] ******************************************************************************************************************************************************changed: [ansible_inventory_controller_1]

    PLAY RECAP **************************************************************************************************************************************************************************ansible_inventory_controller_1 : ok=22   changed=9    unreachable=0    failed=0    skipped=4    rescued=0    ignored=1   
    ansible_inventory_target_1 : ok=10   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
    ansible_inventory_target_2 : ok=10   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
    ansible_inventory_target_3 : ok=10   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
    ansible_inventory_target_4 : ok=10   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
    ```

[**view playbook**](sample-playbook.md)
<br />

[↩️](README.md)
