# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Playbooks***: `Sample Playbook` ▶️

## ***Ships & Commanders*** `Example` 🚢🎖️

* setting up ships

    ```yml
    # ships-setup.yml
    -
      name: ships setup
      hosts: ships
      tags: ['ship', 'setup']
      vars:
        log_dir: "/target_logs"
        file_name: "{{inventory_hostname}}-ship.txt"
      tasks:
        - name: create ship file
          command: touch {{file_name}}  chdir={{log_dir}} creates={{file_name}}
    ```

* setting up commanders

    ```yml
    # commander-setup.yml
    -
      name: commanders setup 
      hosts: commanders
      tags: ['commander', 'setup']
      vars:
        log_dir: "/target_logs"
        file_name: "{{inventory_hostname}}-commander.txt"
      tasks:
        - name: create commander file
          command: touch {{file_name}} chdir={{log_dir}} creates={{file_name}}
    ```

* setting up logs

    ```yml
    # logs-setup.yml
    - 
      name: dir setup
      hosts: all
      tags: ['setup', 'dir']
      vars:
        play_name: "{{ ansible_play_name }}"
        log_dir: "/target_logs"
      tasks:
        - name: create target dir
          command: mkdir {{log_dir}} chdir=/ creates={{log_dir}}
    ```


* ships logs


  * read
    ```yml
    # read-ships-logs.yml
    -
      name: read ship logs
      hosts: ships
      tags: ['ship', 'log', 'read']
      vars:
        play_name: "{{ ansible_play_name }}"
        log_dir: "/target_logs"
        file_name: "{{inventory_hostname}}-ship.txt"
      tasks:
        - name: reading {{play_name}}...
          command: "cat {{log_dir}}/{{file_name}}"
          register: result

        - ansible.builtin.debug:
            msg: "{{ result.stdout_lines }}"
    ```

  * write
    ```yml
    # write-ships-logs.yml
    -
    name: 'writing ship logs...'
    vars:
      log_dir: "/target_logs"
      file_name: "{{inventory_hostname}}-ship.txt"
      event: "**DEFAULT**"
      event_result: "**DEFAULT**"
      log: "{'inventory_hostname': '{{inventory_hostname}}', 'host-name': '{{ansible_hostname}}', 'date': '{{ansible_date_time.date}}', 'time': '{{ansible_date_time.time}}', 'event': '{{event}}', event_result: {{event_result}}}"
    lineinfile:
      line: "{{log}}"
      path: "{{log_dir}}/{{file_name}}"
    tags: [ship, log, write]
    ```



* commanders logs

  * read

    ```yml
    # read-commander-logs.yml
    -
      name: commander read logs
      hosts: commanders
      tags: [commander, log, read]
      vars:
        play_name: "{{ ansible_play_name }}"
        log_dir: "/target_logs"
        file_name: "{{inventory_hostname}}-commander.txt"
      tasks:
        - name: reading {{play_name}}...
          command: "cat {{log_dir}}/{{file_name}}"
          register: result
        
        - ansible.builtin.debug:
            msg: "{{ result.stdout_lines }}"
    ```

  * write

    ```yml
    # write-commander-logs.yml
    - 
      name: 'writing commander logs...'
      vars: 
        log_dir: "/target_logs"
        file_name: "{{inventory_hostname}}-commander.txt"
        event: "**DEFAULT**"
        event_result: "**DEFAULT**"
        log: "{'inventory_hostname': '{{inventory_hostname}}', 'host-name': '{{ansible_hostname}}', 'date': '{{ansible_date_time.date}}', 'time': '{{ansible_date_time.time}}', 'event': '{{event}}', event_result: {{event_result}}}"
      lineinfile:
        line: "{{log}}"
        path: "{{log_dir}}/{{file_name}}"
      tags: [commander, log, write]
  ```

* random tasks

  * **commander**: command tester 
    
    ```yml
    # commander-command.yml
    -
      name: commander command tester
      hosts: commanders
      tags: ['commander', 'command']
      vars:
        play_name: '{{ ansible_play_name }}'
        tool: 'nslookup'
        parameter: 'google.com'

      tasks:
        - name: '{{tool}} test...'
          command: '{{tool}} {{parameter}}'
          register: result
          ignore_errors: true

        - debug:
            msg: ' ❌  {{tool}} failed...'
          when: result is failed 

        - debug:
            msg: ' 🔎  {{tool}} status changed...'
          when: result is changed

        - debug:
            msg: ' ⏭️  {{tool}} was skipped...'
          when: result is skipped

        - debug:
            msg: ' ✔️  {{tool}} succeeded...'
          when: result is success

        - name: 'searching for package'
          shell: 'dnf provides {{tool}} -q'
          register: result2
          ignore_errors: True
          when: result is failed
        
        - command: "echo {{ result2.stdout_lines[0] | regex_search('(.*)-[0-9]:?', '\\1') | first  }}"
          register: command_package
          when: result2 is success and result is failed 
        
        - ansible.builtin.debug:
            msg: ' 📦 found {{ command_package.stdout_lines[0] }}, attempting to install...'
          when: result2 is success and result is failed

        - command: 'dnf -y install {{ command_package.stdout_lines[0] }}'
          when: result2 is success and result is failed

        - command: '{{tool}} {{parameter}}'
          register: result

        - include_tasks: write-commander-logs.yml
          vars:
            event: '{{tool}} {{parameter}}'
            event_result: "'{{result.stdout_lines[0]}}'"
      ```

  * **ships**: get random pokemon

    ```yml
    # ships-pokemon-command.yml
    -
      name: random pokemon
      hosts: ships
      tags: ['ship', 'command']
      vars:
        play_name: "{{ ansible_play_name }}"
        tool: "curl"
        url: "https://retro-pokemon-game-api-k6cgale4bq-uc.a.run.app/pokemon"        
      tasks:
        - set_fact:
            num: "{{range(1, 800) | random }}"
          when: num is not defined

        - name: 'getting a random pokemon...'
          command: "{{tool}} {{url}}/{{num}}"
          register: result
          ignore_errors: true
      
        - debug:
            msg: " ❌  {{tool}} failed..."
          when: result is failed 

        - debug:
            msg: " 🔎  {{tool}} status changed..."
          when: result is changed

        - debug:
            msg: " ⏭️  {{tool}} was skipped..."
          when: result is skipped

        - debug:
            msg: " ✔️  {{tool}} succeeded..."
          when: result is success

        - include_tasks: write-ships-logs.yml
          vars:
            event: "{{tool}} {{url}}/{{num}}"
            event_result: "{{result.stdout}}"
    ```


* use all the playbooks 

  ```shell
  ansible-playbook main.yml -i inventory.txt
  ```


  ```yml
  # main.yml
  - name: dir setup
  run_once: true
  import_playbook: logs-setup.yml

  - name: commander setup
    run_once: true
    import_playbook: commander-setup.yml

  - name: ships setup
    run_once: true
    import_playbook: ships-setup.yml

  - name: commander command
    import_playbook: commander-command.yml
    vars:
      tool: "ls"
      parameter: "-la"

  - name: ships get random pokemon
    import_playbook: ships-pokemon-command.yml

  - name: read commander logs 
    import_playbook: read-commander-logs.yml

  - name: read ships logs 
    import_playbook: read-ships-logs.yml
  ```


[**view output**](sample-out.md)
<br />

[↩️](README.md)
