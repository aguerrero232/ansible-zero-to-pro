# <img src="../assets/img/ansible.png" width="30px"> **Ansible** - ***Section 0:*** `Resources` 🗃️

⚠️ *This guide assumes that you have **python**, **docker**, **docker-compose**, and **ansible** installed on your local machine.* ⚠️

## **Description** 👀

Resources for the `Ansible` ***Zero to Pro Guide***.

<br />

## 🔗 **links**
  * <img src="../assets/img/ansible.png" width="18px"> <a href="https://docs.ansible.com/" target="_blank">**ansible documentation**</a>
    <!-- * dev guide link https://docs.ansible.com/ansible/latest/dev_guide/  -->
    * <a href="https://docs.ansible.com/ansible/latest/dev_guide/index.html" target="_blank">**ansible development guide**</a>
    * <a href="https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_async.html" target="_blank">**ansible asynchronous actions**</a>
  * 🌌 <a href="https://galaxy.ansible.com/docs/" target="_blank">**ansible-galaxy documentation**</a>
  * 🐍 <a href="https://docs.python.org/3/" target="_blank">**python documentation**</a>
  * 🐳 <a href="https://docs.docker.com/" target="_blank">**docker documentation**</a>
  * 🐳<sup>🐳</sup> <a href="https://docs.docker.com/compose/" target="_blank">**docker-compose documentation**</a>

<br />


## **Helpful** `Content` 📌

This is a collection of helpful content for the `Ansible` ***Zero to Pro Guide***. It is not a part of `Ansible`, but it is helpful for learning `Ansible`.

### ***Running in Docker-Compose*** 🐳<sup>🐳</sup>

This will get you up and running with ansible. The below configuration will be starting up **four** `docker containers` using `fedora` as the base image with ansible installed.

* ***Dockerfile***

  ```Dockerfile
  FROM fedora:latest
  RUN dnf -y install ansible; \
      ansible-doc -t connection -l 
  ```

* ***docker-compose.yml***

  ```yml
  version: '3.9'
  services:
    target: &target
      tty: true   
      scale: 4
      build:
        context: .
        dockerfile: Dockerfile    
  ```

* ***.env***

  ```yml
  COMPOSE_PROJECT_NAME=ansible
  ```

***Usage Steps*** 👣

  1. Build the containers

      ```shell
      docker-compose build
      ```

  2. Run the containers

      ```shell
      docker-compose up -d
      ```

<br />

### ***yml***  <img src="../assets/img/yml.png" width="26px">

`yml` is a ***human-readable data serialization language***. It is commonly used for *configuration files* and in applications where data is being stored or transmitted. `yml` is stored in **key value pairs** and can be used to serialize data structures such as *maps, sequences, and scalars*.

`yml` **Syntax**

* `yml` is case sensitive
* Comments are created using the # symbol

**Examples** 🧩

* key value pairs

  ```yml
  Fruit: Apple
  Vegetable: Carrot
  Liquid: Water
  Meat: Chicken
  ```

* arrays / lists

  ```yml
  Fruits:
    - Orange
    - Apple
    - Banana

  Vegetables:
    - Carrot 
    - Cauliflower
    - Tomato
  ```

* dictionary / map

  ```yml
  Banana:
      Calories: 105
      Fat: 0.4g
      Carbs: 27g

  Grapes:
      Calories: 62
      Fat: 0.3g
      Carbs: 16g
  ```

* key value / dictionary / lists

  ```yml
  Fruits:
    - Banana:
        Calories: 105
        Fat: 0.4g
        Carbs: 27g

    - Grapes:
        Calories: 62
        Fat: 0.3g
        Carbs: 16g
  ```

***Notice the alignment, this is important in yml.***

* You can *either* set a value or a list/dictionary/map but *not both*

* `Dictionaries` are an *unordered collection* while `lists` are *ordered*

<br>

### **Useful** `Commands` in ***Fedora*** &nbsp;<img src="../assets/img/fedora_logo.png" width="25px">

* installs core utils

  ```shell
  dnf install coreutils
  ```

* installs proc utils

  ```shell
  dnf install procutils
  ```

* check what provides the `ps` command

  ```shell
  dnf whatprovides ps
  ```

  * **freebie**, it's `procps-ng`

    ```shell
    dnf install procps-ng
    ```

<br />

[↩️🏠](../README.md)

