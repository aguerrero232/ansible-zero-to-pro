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
    ```

    * use **loops** to create arrays
        * when looping over an array of dictionaries you are able to use dot notation for the nested items
        * arrays of dictionaries can also be represented in a json format

        ```yml
        ---
        -
            name: Create Users
            hosts: localhost
            var:
                num_users: 6
            tasks:        
                -
                    name: Create Users
                    user:
                        name: '{{item.name}}'
                        id: '{{item.id}}'
                        state: present
                    loop:
                        - name: user_1
                          id: 1
                        - name: user_2 
                          id: 2
                        - name: user_3
                          id: 3
                        - name: user_4
                          id: 4
                        - name: user_5
                          id: 5
                        - name: user_6
                          id: 6

                -
                    name: Create Users (json)
                    user:
                        name: '{{item.name}}'
                        id: '{{item.id}}'
                        state: present
                    loop:
                        - {name: user_1, id: 1}
                        - {name: user_2, id: 2}
                        - {name: user_3, id: 3}
                        - {name: user_4, id: 4}
                        - {name: user_5, id: 5}
                        - {name: user_6, id: 6}

        ```

    * **with_\*** directive lets you loop over a list of items
        * `with_items` is the most common
        * `with_dict` is used to loop over a dictionary
        * `with_file` is used to loop over a file
        * `with_url` is used to loop over urls
        * `With_k8s` is used to loop over kubernetes resources
        * `With_inventory_hostnames` is used to loop over inventory hostnames

        ```yml
        ---
        -
            name: Create Users
            hosts: localhost
            var:
                num_users: 6
            tasks:        
                -
                    name: Create Users (with_items)
                    user:
                        name: '{{item.name}}'
                        id: '{{item.id}}'
                        state: present
                    with_items:
                        - name: user_1
                          id: 1
                        - name: user_2 
                          id: 2
                        - name: user_3
                          id: 3
                        - name: user_4
                          id: 4
                        - name: user_5
                          id: 5
                        - name: user_6
                          id: 6

                -
                    name: View Config Files (with_file)
                    debug: var=item
                    with_file:
                        - '/etc/hosts'
                        - '/etc/resolv.conf'
                        - '/etc/ntp.conf'

                -
                    name: Get From URLS (with_url)
                    debug: var=item
                    with_url:
                        - 'https://www.dell.com'
                        - 'https://www.google.com'
                        - 'https://www.amazon.com'
        ```




<br />

[↩️](../README.md)
