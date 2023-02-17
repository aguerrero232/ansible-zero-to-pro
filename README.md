# Ansible Zero To Pro ✨

<img src="assets/img/header.jpg" width="100%" height="330px">

<br/>

### ⛏️ ***"A stone is broken by the last stroke of the hammer. This does not mean that the first stroke was useless. Success is the result of continuous effort."*** ⛏️

<br>

## ***Table*** *of* ***`Contents`*** 📜

* 🗃️ [***resources***](00-resources/README.md)
* 🧠 [***core concepts***](01-core-concepts/README.md)
* 🤯 [***advanced concepts***](02-advanced/README.md)
<br />


## **Ansible** `Definitions` <image src="assets/img/ansible.png" width="28px">

**`Idempotency`** - An operation is *idempotent* if the result of performing it once is exactly the same as the result of performing it repeatedly without any intervening actions.

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