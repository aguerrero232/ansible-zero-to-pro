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

## ***Running in Docker-Compose*** 🐳<sup>🐳</sup>

<!-- use fedora to learn ansible, bleeding edge
  out of the box, ansible is installed and python 3.11
-->

This will get you started with ansible by running four docker containers with ansible installed through docker-compose. 

* ### ***Dockerfile***

  ```Dockerfile
  FROM fedora:latest
  RUN dnf -y install ansible; \
      ansible-doc -t connection -l 
  ```

* ### ***docker-compose.yml***

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

  * freebie its `procps-ng`

    ```shell
    dnf install procps-ng
    ```
