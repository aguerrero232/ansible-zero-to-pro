# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Playbooks***: `Sample Playbook` ▶️

The below playbook example has two plays. The first play is executed on all hosts in the inventory. The second play is executed on the host `inventory_target_3`. 

* `Play 1`: prints the date, inventory and ansible host name, and finished

* `Play 2`: attempts a nslookup on google.com and if the command fails, attempts to install the package associated with the and re-run nslookup. 


```yaml
- 
  name: Play 1
  hosts: all
  vars: 
    date: "{{ ansible_date_time.date }}"
    play_name: "{{ ansible_play_name }}"
  tasks:
    - name: printing date
      ansible.builtin.debug:
        msg: "📅 date:  {{ date }}"
    - name: printing getting host name
      ansible.builtin.debug:
        msg: "🖥️  {{ inventory_hostname }}: {{ ansible_hostname }}"
    - name: finishing play 1
      ansible.builtin.debug:
        msg: "✔️  {{play_name}} finished..."

- 
  name: Play 2
  hosts: inventory_target_3
  vars:
    play_name: "{{ ansible_play_name }}"
  tasks:
    
    - name: printing tast
      ansible.builtin.debug:
        msg: "attempting nslookup of google.com..."

    - shell: nslookup google.com
      register: result
      ignore_errors: True

    - debug:
        msg: "❌  command failed..."
      when: result is failed 

    - debug:
        msg: "🔎  status changed..."
      when: result is changed

    - debug:
        msg: "⏭️  command was skipped..."
      when: result is skipped

    - debug:
        msg: "✔️  command succeeded..."
      when: result is success

    - shell: dnf provides nslookup -q
      register: result2
      ignore_errors: True
      when: result is failed
    
    - name: saving provides command result
      command: "echo {{ result2.stdout_lines[0] | regex_search('(.*)-[0-9]:?', '\\1') | first  }}"
      register: command_package
      when: result2 is success and result is failed 
    
    - name: printing provides command result
      ansible.builtin.debug:
        msg: "📦 found {{ command_package.stdout_lines[0] }}, attempting to install..."
      when: result2 is success and result is failed and command_package is defined

    - name: installing command package
      command: "dnf -y install {{ command_package.stdout_lines[0] }}"
      when: result2 is success and result is failed and command_package is defined
    
    - debug:
        msg: "✔️  package install complete..."
      when: result2 is success 

    - debug:
        msg: "❌  package install failed..."
      when: result2 is failed

    - name: retry nslookup after fail and install
      command: "nslookup google.com"
      register: result 
      ignore_errors: true
      when: result2 is success

    - debug:  
        msg: "{{ result }}"
      when: result is success

    - name: finishing play 2
      ansible.builtin.debug:
        msg: "✔️ {{play_name}} finished..."

```
[**view output**](sample-out.md)
<br />

[↩️](README.md)
