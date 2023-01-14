# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Variables*** 🔡


## **Description** 👀

`Variables` **store information** that varies with each host. `Variables` can be used to store information about a **host**, such as its `IP address`, `hostname`, or `operating system`. 

`Variables` **can also be used** to store information about a ***group of hosts***, such as the name of a database server or the name of a web server. 


<br />

## **Basics** 📝

* inventory variables

    ```yaml
    # inventory.yml
    [web]
    host1.example.com
    host2.example.com

    [web:vars]
    http_port=80
    maxRequestsPerChild=8080
    ```

    * `host1.example.com` and `host2.example.com` are both members of the `web` group
    * `http_port` and `maxRequestsPerChild` are variables that are defined for the `web` group

* playbook variables

    ```yaml
    # playbook.yml
    - name: Add a DNS server to /etc/resolv.conf 
      hosts: localhost
      # variables are stored under the `vars` key using the `key: value` format
      vars:
        dns_server: 10.1.250.10
      tasks:
        - lineinfile: 
            path: /etc/resolv.conf
            line: 'nameserver {{ dns_server }}'
    ```

* separate variables file

    ```yaml
    # vars.yml
    dns_server: '{{ dns_server }}'

    ```





<br />


## **Examples** 🧩

<br />

[↩️](../README.md)
