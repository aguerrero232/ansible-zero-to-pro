# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Conditionals*** 🔛


## **Description** 👀

<br />

## **Basic** `Commands` 📝

<br />


## **Examples** 🧩

* **when** example; installs `nginx` on `Debian` and `RedHat` based systems

    ```yml
    ---
    - 
        name: install nginx
        hosts: all
        tasks:
            - 
                name: install nginx
                apt:
                    name: nginx
                    state: present
                when: ansible_os_family == "Debian"
            - 
                name: install nginx
                yum:
                    name: nginx
                    state: present
                when: ansible_os_family == "RedHat"
    ``` 




<br />

[↩️](../README.md)
