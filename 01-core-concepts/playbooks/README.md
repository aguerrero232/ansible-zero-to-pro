# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Playbooks*** ▶️

## **Description** 👀
`Playbooks` are written in `yaml`, and are the ***main*** way to automate `Ansible`.

* `play`: defines the set of activities (tasks) to be run on hosts
* `task`: an action to be performed on the host
  * *i.e*: execute a command, run a script, install a package

<br />

## **Basic** `Commands` 📝

* execute an ansible playbook

    ```shell
    ansible-playbook <path-to/playbook.yml> -i <path-to/inventory.txt>
    ```


<br />


## **Examples** 🧩

* sample playbook

    ```yaml
    -
        name: Play 1
        hosts: all
        tasks:
            - name: execute command 'date'
              command: date
            - name: execute script on server
              command: test_script.sh
            - name: install httpd service
              yum:
                name: httpd
                state: present
            - name: start web server
              service: 
                name: httpd
                state: started
    ```

<br />

[↩️](../README.md)