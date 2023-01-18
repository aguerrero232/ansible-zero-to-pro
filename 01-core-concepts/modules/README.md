# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Modules*** ⚙️

## **Description** 👀

Ansible contains several modules grouped in different categories.

Some categories are:

* **system** - actions to be performed at a system level
  * modifying users, groups, iptables, firewall configs
  * working with services

* **commands** - used to execute commands or scripts on a host
  * simple commands using the `command` module
  * interactive execution using the `expect` module by responding to prompts
  * run scripts on the host using the `script` module

* **files** - helps work with files
  * use the `archive` and `un-archive` modules to archive and unarchive files...
  * use `find`, `inlinefile`, and `replace` to modify file contents

* and **many** others..

<br />

## **Basics** 📝

* ***command module*** `parameters`
  * `chdir` - change directory before executing the command
  * `creates` - a filename, when it already exists, this step will be skipped
  * `executable` - change the shell used to execute the command, should be an absolute path
  * `free_form` - the command module takes a free form command to run
  * `removes` - remove the file after execution if it exists
  * `warn` - warn when the command changes things 

* **script module**
  1. copy scripts to the remote systems
  2. execute scripts on remote systems

  ```yml
  - 
    name: <play-name>
    hosts: <host-pattern>
    tasks:
    - name: <task-name>
      script: <path-to/script.sh> <script-args>
  ```

* **service module**
  * manage services - **start**, **stop**, **restart**

  ```yml
  - 
    name: <play-name>
    hosts: <host-pattern>
    tasks:
    - name: <task-name>
      service: name=<service-name> state=<service-state>
  ```

  * *alternate* method of creation using yml dictionary

    ```yml
    - 
      name: <play-name>
      hosts: <host-pattern>
      tasks:
      - name: <task-name>
        <module>:
          name: <service-name>
          state: <service-state>
    ```

    * they are one and the same

<br />

## **Examples** 🧩

* command module 

<br />

* **script module** `play`

  ```yml
  - 
    name: Sample Script Play - Create Target Log Directory
    hosts: localhost
    tasks:
    - name: create the target log directory
      script: create_script.sh 
  ```

* **service module** `play`

  ```yml
  - 
    name: Samlple Service Play - Start Postgres Service
    hosts: localhost
    tasks:
    - name: Start postgres service
      service: name=postgresql state=started
  ```

  * why is the state `started`, and not **start**?
    * if the service is already running, the state `started` will not cause any changes, this is called ***idempotent***
  * **started**, **stopped**, **restarted** ensure that the service is in the desired state

<br/>

[↩️](../README.md)
