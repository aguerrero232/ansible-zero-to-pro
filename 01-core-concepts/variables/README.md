# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Variables*** 🔡


## **Description** 👀

`Variables` **store information** that varies with each host. `Variables` can be used to store information about a **host**, such as its `IP address`, `hostname`, or `operating system`. 

`Variables` **can also be used** to store information about a ***group of hosts***, such as the name of a database server or the name of a web server. 


To use a `variable`, you must enclose the variable name in double curly braces 

* i.e
  ```yaml
  {{<variable-name>}}
  ```

<br />

## **Basics** 📝

* inventory variables

    ```yml
    # inventory.txt
    [<group-name>]
    <host>

    [<group-name>:vars]
    <variableX>=<valueY>
    ```

* playbook variables

    ```yml
    # playbook.yml
    - name: <play name> 
      hosts: <host-pattern>
      # variables are stored under the `vars` key using the `key: value` format
      vars:
        <variableX>: <valueY>
      tasks:
        - <module>:
            <key>: <value>
    ```

* separate variables file

    ```yml
    # vars.yml
    <variableX>: <valueY>
    ```

  * variable files named after **hosts/groups** allows ansible to load the variables when the **host/group** is referenced

<br />


## **Examples** 🧩

* inventory variables

    ```yml
    # inventory.txt
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

    ```yml
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

    ```yml
    # vars.yml
    variable1: value1
    variable2: value2
    ```


* playbook using variables in variables file


    ```yml
    # inventory.txt
    [web]
    host1.example.com
    host2.example.com
    ```

    ```yml
    # web.yml
    http_port: 80
    snmp_port: 161-162
    inter_ip_range: 192.0.2.0
    ```

    * can be used whenever the host is part of the `web` group

    ```yml
    # playbook.yml
    -
      name: Set Firewall Configuration
      hosts: web
      tasks:

        - firewalld:
            service: https
            permanent: true
            state: enabled

        - firewalld:
            port: "{{ http_port }}/tcp"
            permanent: true
            state: disabled

        - firewalld:
            port: "{{ snmp_port }}/udp"
            permanent: true
            state: enabled

        - firewalld:
            source: "{{inter_ip_range}}/24"
            Zone: internal
            state: enabled
    ```

<br />

[↩️](../README.md)
