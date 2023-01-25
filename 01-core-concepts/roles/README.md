# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Roles*** 📜


## **Description** 👀

Roles are a way of ***automatically loading related vars_files, tasks, and handlers*** based on a known file structure. They can **also help you better organize your files**, especially if you’re using Ansible to deploy multiple apps or systems that have similar roles. Roles are a way of grouping **variables**, **tasks**, **files**, **templates**, and **modules** in a way that makes your infrastructure ***easier*** to manage.



Roles introduce a set of best practices that must be followed.

* **tasks** are to go in the `tasks/` directory
* **vars** are to go in the `vars/` directory
* **defaults** are to go in the `defaults/` directory
* **handlers** are to go in the `handlers/` directory
* **templates** are to go in the `templates/` directory

<br />

## **Basics** 📝

* **create** a role

    ```bash
    ansible-galaxy init <role-name>
    ```

    ```yml
    # generated role directory structure
    <role-name>/
        ├── defaults
        │   └── main.yml
        ├── files
        ├── handlers
        │   └── main.yml
        ├── meta
        │   └── main.yml
        ├── tasks
        │   └── main.yml
        ├── templates
        ├── tests
        │   ├── inventory
        │   └── test.yml
        └── vars
        │   └── main.yml
        ├── README.md
    ```

    * how does my playbook know where to find the role?
      * add a roles directory to the playbook directory
      * add the role to the `/etc/ansible/roles` directory 
        * this is the default location ansible looks for roles defined in the `/etc/ansible/ansible.cfg` file


* **search** for existing community roles

    ```bash
    ansible-galaxy search <role-name>
    ```


<br />

[↩️](../README.md)
