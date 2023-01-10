# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Inventory*** 🧳

## **Description** 👀

`Ansible` can work with one or more systems in your infrastructure ***at the same time***. In order to work with multiple servers `Ansible` needs to establish a connection to those servers. This is done with SSH on linux, and Powershell Remoting for Windows. Most of the pitfalls for other orchestration tools is that you are required to set up an agent on the target machines before you can invoke any automation. This is not the case with `Ansible`. `Ansible` is agentless, meaning no additional software is needed on the target machines to be able to work with `Ansible`.

Information about the target machines is stored in an `inventory`. The `inventory` is a file that contains a list of hosts and groups of hosts. The `inventory` file is located in the `/etc/ansible/hosts` directory by default.

<br />

## **Basic** `Commands` 📝


* **ping** to test `inventory`

    ```shell
    ansible <host-or-group> -m ping -i <inventory-config-file>
    ```

<br />

## **Examples** 🧩

* **basic** inventory file

    ```yaml
    server1.company.com
    server2.company.com
    server3.company.com
    server4.company.com
    ```

* **basic** inventory file with aliases

    ```yaml
    web ansible_host=server1.company.com
    db ansible_host=server2.company.com
    mail ansible_host=server3.company.com
    web2 ansible_host=server4.company.com
    ```

  * some other inventory parameters that can be used:

    ```yaml
    ansible_port=22
    ansible_user=ansible
    ansible_ssh_pass=ansible
    ansible_connection=ssh 
    ```

    * by default the ansible port is set to 22
    * by default the ansible user is set to root (on linux)
    * if you dont have any other hosts to connect to then you can use localhost instead

        ```yaml
        localhost ansible_connection=localhost
        ```

* **basic** inventory file with groups
  
    ```yaml
    [web]
    server1.company.com
    server2.company.com

    [db]
    server3.company.com
    server4.company.com
    ```

* inventory file with linux web servers and windows db servers

    ```yaml
    web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
    web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
    web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
    db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=ansible_password=Password123!
    ```

    * grouping the servers

        ```yaml
        # -- servers
        # web servers
        web1 ansible_host=server1.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
        web2 ansible_host=server2.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
        web3 ansible_host=server3.company.com ansible_connection=ssh ansible_user=root ansible_ssh_pass=Password123!
        # db servers
        db1 ansible_host=server4.company.com ansible_connection=winrm ansible_user=administrator ansible_password=Password123!

        # -- groups --
        # all web servers
        [web_servers] 
        web1
        web2
        web3
        # all db servers
        [db_servers] 
        db1
        # all servers (using web and db server groups to make a new group)
        [all_servers:children] 
        web_servers
        db_servers
        ```


<br />

## **Testing** 🧪

**refer to this** [**link**](../../00-resources/README.md#helpful-content-) to get up and running

* `inventory.txt` containing **two** groups and **four** targets.
  
    ```yaml
  [group1]
  inventory_target_1 ansible_connection=community.docker.docker
  inventory_target_2 ansible_connection=community.docker.docker

  [group2]
  inventory_target_3 ansible_connection=community.docker.docker
  inventory_target_4 ansible_connection=community.docker.docker
    ```

* `ping` **all** the inventory targets

  ```shell
  ansible -m ping all -i inventory.txt
  ```

  * output

    ````bash
    inventory_target_3 | SUCCESS => {
        "ansible_facts": {
            "discovered_interpreter_python": "/usr/bin/python3"
        },
        "changed": false,
        "ping": "pong"
    }
    inventory_target_2 | SUCCESS => {
        "ansible_facts": {
            "discovered_interpreter_python": "/usr/bin/python3"
        },
        "changed": false,
        "ping": "pong"
    }
    inventory_target_1 | SUCCESS => {
        "ansible_facts": {
            "discovered_interpreter_python": "/usr/bin/python3"
        },
        "changed": false,
        "ping": "pong"
    }
    inventory_target_4 | SUCCESS => {
        "ansible_facts": {
            "discovered_interpreter_python": "/usr/bin/python3"
        },
        "changed": false,
        "ping": "pong"
    }
    ````


* ping `group1` inventory targets

  ```shell
  ansible -m ping group1 -i inventory.txt
  ```

  * output

    ```bash
    inventory_target_2 | SUCCESS => {
          "ansible_facts": {
              "discovered_interpreter_python": "/usr/bin/python3"
          },
          "changed": false,
          "ping": "pong"
      }
      inventory_target_1 | SUCCESS => {
          "ansible_facts": {
              "discovered_interpreter_python": "/usr/bin/python3"
          },
          "changed": false,
          "ping": "pong"
      }
      ```




<br />

[↩️](../README.md)
