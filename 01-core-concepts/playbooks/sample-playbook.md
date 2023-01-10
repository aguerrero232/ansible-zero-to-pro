# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Playbooks***: `Sample Playbook` ▶️

## ***Ships & Commanders*** `Example` 🚢🎖️

* setting up ships

    ```yaml
    -
        name: ships setup
        hosts: ships
        vars:
            play_name: "{{ ansible_play_name }}"
            log_dir: "/target_logs"
        tasks:
        - name: create ship file
          command: "touch {{log_dir}}/{{inventory_hostname}}-ship.txt"
          register: file_status

        - name: set env variable
          ansible.builtin.set_fact:
            SHIPS_SETUP: 1
          when: file_status is success

        - name: finishing ships setup
          ansible.builtin.debug:
            msg: "ships init complete..."
    ```

* setting up commanders

    ```yaml
    -
        name: commanders setup 
        hosts: commanders
        vars:
            play_name: "{{ ansible_play_name }}"
            log_dir: "/target_logs"
        tasks:
        - name: create commander file
          command: "touch {{log_dir}}/{{inventory_hostname}}-commander.txt"
          register: file_status  

        - name: set env variable
          ansible.builtin.set_fact:
            COMMANDER_SETUP: 1
          when: file_status is success

        - name: finishing commanders setup
          ansible.builtin.debug:
            msg: "commanders init complete..."
    ```

* setting up logs

    ```yaml
    - 
        name: dir setup
        hosts: all
        vars:
            play_name: "{{ ansible_play_name }}"
            log_dir: "/target_logs"
        tasks:
        - name: create target dir
          command: "mkdir -p {{log_dir}}"
          register: dir_status

        - name: set env variable
          ansible.builtin.set_fact:
            DIR_SETUP: 1
          when: dir_status is success

        - name: finishing dir setup
          ansible.builtin.debug:
          msg: "dir init complete..."
    ```


* ships logs

    ```yaml
    -
        name: ship logs
        hosts: ships
        vars:
            play_name: "{{ ansible_play_name }}"
            log_dir: "/target_logs"
            log: "inventory_hostname: {{inventory_hostname}}, host-name: {{ansible_hostname}}, date: {{ansible_date_time.date}}, time: {{ansible_date_time.time}}"
        tasks:

            - name: writing {{play_name}}...
              copy: 
                content: "{{log}}"
                dest: "{{log_dir}}/{{inventory_hostname}}-ship.txt"

            - name: reading {{play_name}}...
              command: "cat {{log_dir}}/{{inventory_hostname}}-ship.txt"
              register: result

            - name: printing {{play_name}}...
              ansible.builtin.debug:
                msg: "{{ result }}"
              when: result is success
    ```

* commanders logs

    ```yaml
    -
        name: commander logs
        hosts: commanders
        vars:
            play_name: "{{ ansible_play_name }}"
            log_dir: "/target_logs"
            log: "inventory_hostname: {{inventory_hostname}}, host-name: {{ansible_hostname}}, date: {{ansible_date_time.date}}, time: {{ansible_date_time.time}}, secret: 'da wey'"
        tasks:
            - name: writing {{play_name}}...
            ansible.builtin.copy:
                content: "{{log}}"
                dest: "{{log_dir}}/{{inventory_hostname}}-commander.txt"

            - name: reading {{play_name}}...
            command: "cat {{log_dir}}/{{inventory_hostname}}-commander.txt"
            register: result

            - name: printing {{play_name}}...
            ansible.builtin.debug:
                msg: "{{ result }}"
            when: result is success
    ```

* commander runs nslookup on google or installs the package containing nslookup and retries again

    ```yaml
    -
        name: commander google nslookup
        hosts: commanders
        vars:
            play_name: "{{ ansible_play_name }}"
            log_dir: "/target_logs"
        tasks:
            - name: printing nslookup test...
              ansible.builtin.debug:
                msg: "attempting nslookup of google.com..."

            - name: nslookup test...
              command: "nslookup google.com"
              register: result
              ignore_errors: true

            - shell: "dnf provides nslookup -q"
              register: result2
              ignore_errors: True
              when: result is failed

            - name: saving provides command result
              command: "echo {{ result2.stdout_lines[0] | regex_search('(.*)-[0-9]:?', '\\1') | first  }}"
              register: command_package
              when: result2 is success and result is failed 

            - name: printing provides command result
              ansible.builtin.debug:
                msg: " 📦 found {{ command_package.stdout_lines[0] }}, attempting to install..."
              when: result2 is success and result is failed and command_package is defined

            - name: installing command package
              command: "dnf -y install {{ command_package.stdout_lines[0] }}"
              when: result2 is success and result is failed and command_package is defined

            - name: retry nslookup after fail and install
              command: "nslookup google.com"
              register: result

            - name: print nslookup result
              ansible.builtin.debug:
                msg: "{{result}}"
              when: result is success

            - debug:
                msg: " ❌  command failed..."
              when: result is failed 
            - debug:
                msg: " 🔎  status changed..."
              when: result is changed
            - debug:
                msg: " ⏭️  command was skipped..."
              when: result is skipped
            - debug:
                msg: " ✔️  command succeeded..."
              when: result is success

            - name: logging commander event
              copy: 
                content: "{{result}}"
                dest: "{{log_dir}}/{{inventory_hostname}}-commander.txt"
    ```

* setup playbook to run all the setups

    ```yaml
    - name: logs setup
      import_playbook: setup-logs.yaml
      when: DIR_SETUP is undefined or DIR_SETUP != 1

    - name: commander setup
      import_playbook: commander-setup.yaml
      when: COMMANDER_SETUP is undefined or COMMANDER_SETUP != 1

    - name: ships setup
      import_playbook: ships-setup.yaml
      when: SHIPS_SETUP is undefined or SHIPS_SETUP != 1
    ```


* log playbook to run the two log playbooks

    ```yaml
    - name: commander logs 
      import_playbook: commander-logs.yaml
      when: COMMANDER_SETUP==1

    - name: ships logs 
      import_playbook: ships-logs.yaml
      when: SHIPS_SETUP==1
    ```

* main playbook to run the setup and log playbooks

    ```yaml
    - name: setup
      import_playbook: playbooks/setup-playbook.yaml

    - name: logging
      import_playbook: playbooks/log-playbook.yaml
      when: DIR_SETUP==1

    - name: commander nslookup
      import_playbook: playbooks/commander-nslookup.yaml
      when: COMMANDER_SETUP==1
    ```




[**view output**](sample-out.md)
<br />

[↩️](README.md)
