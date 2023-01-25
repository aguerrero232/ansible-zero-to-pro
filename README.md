# Ansible Zero To Pro ✨

<img src="assets/img/header.jpg" width="100%" height="330px">

<br/>

### ⛏️ ***"A stone is broken by the last stroke of the hammer. This does not mean that the first stroke was useless. Success is the result of continuous effort."*** ⛏️

<br>

## **Description** 👀

`Ansible` is an **open-source software** provisioning, configuration management, and application-deployment tool enabling infrastructure as code. It runs on many Unix-like systems, and can configure both Unix-like systems as well as Microsoft Windows.

<br />

## **Ansible** `Definitions` <image src="assets/img/ansible.png" width="28px">

**`Idempotency`** - An operation is *idempotent* if the result of performing it once is exactly the same as the result of performing it repeatedly without any intervening actions.

<br>

## ***Table*** *of* ***`Contents`*** 📜

0. 🗃️ [***resources***](00-resources/README.md)
1. 🧠 [***core concepts***](01-core-concepts/README.md)
    * 🧳 [**inventory**](01-core-concepts/inventory/README.md)
    * ▶️ [**playbooks**](01-core-concepts/playbooks/README.md)
    * ⚙️ [**modules**](01-core-concepts/modules/README.md)
    * 🔡 [**variables**](01-core-concepts/variables/README.md)
    * 🔛 [**conditionals**](01-core-concepts/conditionals/README.md)
    * 📜 [**roles**](01-core-concepts/roles/README.md)
2. 🤯 [***advanced concepts***](02-advanced-concepts/README.md)


<br>

## **CLI** <image src="assets/img/ansible.png" width="28px">

* imperative style of execution

    ```shell
    ansible <host-pattern> -m <module> -a <command>
    ```

* `ansible` **docs**

    ```shell
    ansible-doc -l
    ```

* reboot hosts (`command`)

    ```shell
    ansible <host-pattern> -a '/sbin/reboot'
    ```

* ping hosts (`module`)

    ```shell
    ansible <host-pattern> -m ping
    ```