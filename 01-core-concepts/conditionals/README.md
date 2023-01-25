# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Conditionals*** 🔛


## **Description** 👀

`Conditionals` are used to **control the flow of execution** of tasks in `Ansible`. They are used to c**heck the state of a system** and then **execute a task based on the result** of the check.


<br />

<!-- ## **Basic** `Commands` 📝

<br />
 -->

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


* **loop** example; installs packages based on requirement over an array of packages

    ```yml
    ---
    -
        name: Install Packages
        hosts: all
        vars:
            packages:
                - name: nginx
                required: True
                - name: httpd
                required: False
                - name: apache2
                required: False
        tasks:
            - 
                name: Install {{item.name}} (using apt)
                apt:
                    name: "{{ item.name }}"
                    state: present
                when: item.required == True
                loop: "{{ packages }}"

    ```


* **record** output of tasks; mail if service is not running (first checking the service)

    ```yml
    ---
    - 
        name: Check Status of Services
        hosts: localhost
        tasks:
            -
                name: Check HTTPD Status
                command: service httpd status
                register: httpd_status
            
            -
                name: Mail HTTPD Status if not running

                mail:
                    to: someone@job.com
                    subject: "HTTPD is not running"
                    body: "{{ httpd_status.stdout }}"
                when: httpd_status.stdout.find("down") != -1



<br />

[↩️](../README.md)
