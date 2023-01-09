# <img src="../assets/img/ansible.png" width="30px"> **Ansible** - ***Section 0:*** `Resources` 🗃️

<!-- 

replacing md links with html links

regex: \[\*\*([A-z0-9- *]{1,})\*\*\]\((https://[A-z0-9-./]{1,})\)
replace: <a href="$2" target="_blank">***$1***</a> 

-->

## ***Table*** *of* ***`Contents`*** 📜

* 🏠 [**home**](../README.md)
* 🗃️ **resources**
  * 🔗 **links**
    * 📄 <a href="https://docs.ansible.com/" target="_blank">**ansible documentation**</a>

<br />

## **Description** 👀

Resources for the `Ansible` ***Zero to Pro Guide***. Has images, pdfs, and links to other resources.

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

  ```yaml
  version: '3.9'
  services:
    target: &target
      tty: true   
      scale: 4
      build:
        context: .
        dockerfile: Dockerfile    
  ```

### ***Usage Steps*** 👣

  1. Build the containers

      ```shell
      docker-compose build
      ```

  2. Run the containers

      ```shell
      docker-compose up
      ```

<br />

## ***YAML***  <img src="../assets/img/yaml.png" width="26px">

`YAML` is a ***human-readable data serialization language***. It is commonly used for *configuration files* and in applications where data is being stored or transmitted. `YAML` is stored in **key value pairs** and can be used to serialize data structures such as *maps, sequences, and scalars*.

### `YAML` **Syntax**

* `YAML` is case sensitive
* Comments are created using the # symbol

### **Examples** 🧩

* key value pairs

  ```yaml
  Fruit: Apple
  Vegetable: Carrot
  Liquid: Water
  Meat: Chicken
  ```

* arrays / lists

  ```yaml
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

  ```yaml
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

  ```yaml
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

***Notice the alignment, this is important in yaml.***

* You can *either* set a value or a list/dictionary/map but *not both*

* `Dictionaries` are an *unordered collection* while `lists` are *ordered*

<br>

## **Useful** `Commands` in ***Fedora*** &nbsp;<img src="../assets/img/fedora_logo.png" width="25px">

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
