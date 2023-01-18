# <img src="../../assets/img/ansible.png" width="30px"> **Ansible** - ***Playbooks***: `Sample Output` ▶️

* **run** the `playbook`

```shell
🚀  ansible-zero-to-pro ➜ ansible-playbook main.yml -i inventory.txt 
```

* **`output`**

    ```shell
    PLAY [dir setup] ********************************************************************************************
    TASK [Gathering Facts] **************************************************************************************ok: [ansible_target_3]
    ok: [ansible_target_1]
    ok: [ansible_controller_1]
    ok: [ansible_target_4]
    ok: [ansible_target_2]

    TASK [create target dir] ************************************************************************************ok: [ansible_controller_1]
    ok: [ansible_target_3]
    ok: [ansible_target_4]
    ok: [ansible_target_2]
    ok: [ansible_target_1]

    PLAY [commanders setup] *************************************************************************************
    TASK [Gathering Facts] **************************************************************************************ok: [ansible_controller_1]

    TASK [create commander file] ********************************************************************************changed: [ansible_controller_1]

    PLAY [ships setup] ******************************************************************************************
    TASK [Gathering Facts] **************************************************************************************ok: [ansible_target_1]
    ok: [ansible_target_4]
    ok: [ansible_target_3]
    ok: [ansible_target_2]

    TASK [create ship file] *************************************************************************************changed: [ansible_target_1]
    changed: [ansible_target_3]
    changed: [ansible_target_4]
    changed: [ansible_target_2]

    PLAY [commander command tester] *****************************************************************************
    TASK [Gathering Facts] **************************************************************************************ok: [ansible_controller_1]

    TASK [ls test...] *******************************************************************************************changed: [ansible_controller_1]

    TASK [debug] ************************************************************************************************skipping: [ansible_controller_1]

    TASK [debug] ************************************************************************************************ok: [ansible_controller_1] => {
        "msg": " 🔎  ls status changed..."
    }

    TASK [debug] ************************************************************************************************skipping: [ansible_controller_1]

    TASK [debug] ************************************************************************************************ok: [ansible_controller_1] => {
        "msg": " ✔️  ls succeeded..."
    }

    TASK [searching for package] ********************************************************************************skipping: [ansible_controller_1]

    TASK [command] **********************************************************************************************skipping: [ansible_controller_1]

    TASK [ansible.builtin.debug] ********************************************************************************skipping: [ansible_controller_1]

    TASK [command] **********************************************************************************************skipping: [ansible_controller_1]

    TASK [command] **********************************************************************************************changed: [ansible_controller_1]

    TASK [include_tasks] ****************************************************************************************included: /home/guerrero/code/ansible-zero-to-pro/01-core-concepts/playbooks/yaml-examples/write-commander-logs.yaml for ansible_controller_1

    TASK [writing commander logs...] ****************************************************************************changed: [ansible_controller_1]

    PLAY [random pokemon] ***************************************************************************************
    TASK [Gathering Facts] **************************************************************************************ok: [ansible_target_1]
    ok: [ansible_target_4]
    ok: [ansible_target_2]
    ok: [ansible_target_3]

    TASK [set_fact] *********************************************************************************************ok: [ansible_target_1]
    ok: [ansible_target_2]
    ok: [ansible_target_3]
    ok: [ansible_target_4]

    TASK [getting a random pokemon...] **************************************************************************changed: [ansible_target_1]
    changed: [ansible_target_2]
    changed: [ansible_target_3]
    changed: [ansible_target_4]

    TASK [debug] ************************************************************************************************skipping: [ansible_target_2]
    skipping: [ansible_target_1]
    skipping: [ansible_target_3]
    skipping: [ansible_target_4]

    TASK [debug] ************************************************************************************************ok: [ansible_target_1] => {
        "msg": " 🔎  curl status changed..."
    }
    ok: [ansible_target_3] => {
        "msg": " 🔎  curl status changed..."
    }
    ok: [ansible_target_2] => {
        "msg": " 🔎  curl status changed..."
    }
    ok: [ansible_target_4] => {
        "msg": " 🔎  curl status changed..."
    }

    TASK [debug] ************************************************************************************************skipping: [ansible_target_1]
    skipping: [ansible_target_2]
    skipping: [ansible_target_3]
    skipping: [ansible_target_4]

    TASK [debug] ************************************************************************************************ok: [ansible_target_1] => {
        "msg": " ✔️  curl succeeded..."
    }
    ok: [ansible_target_2] => {
        "msg": " ✔️  curl succeeded..."
    }
    ok: [ansible_target_3] => {
        "msg": " ✔️  curl succeeded..."
    }
    ok: [ansible_target_4] => {
        "msg": " ✔️  curl succeeded..."
    }

    TASK [include_tasks] ****************************************************************************************included: /home/guerrero/code/ansible-zero-to-pro/01-core-concepts/playbooks/yaml-examples/write-ships-logs.yaml for ansible_target_1, ansible_target_2, ansible_target_3, ansible_target_4

    TASK [writing ship logs...] *********************************************************************************changed: [ansible_target_4]
    changed: [ansible_target_2]
    changed: [ansible_target_1]
    changed: [ansible_target_3]

    PLAY [commander read logs] **********************************************************************************
    TASK [Gathering Facts] **************************************************************************************ok: [ansible_controller_1]

    TASK [reading commander read logs...] ***********************************************************************changed: [ansible_controller_1]

    TASK [ansible.builtin.debug] ********************************************************************************ok: [ansible_controller_1] => {
        "msg": [
            "{'inventory_hostname': 'ansible_controller_1', 'host-name': 'a76310fcd14b', 'date': '2023-01-18', 'time': '00:12:39', 'event': 'ls -la', event_result: 'total 72'}"
        ]
    }

    PLAY [read ship logs] ***************************************************************************************
    TASK [Gathering Facts] **************************************************************************************ok: [ansible_target_1]
    ok: [ansible_target_2]
    ok: [ansible_target_3]
    ok: [ansible_target_4]

    TASK [reading read ship logs...] ****************************************************************************changed: [ansible_target_1]
    changed: [ansible_target_2]
    changed: [ansible_target_3]
    changed: [ansible_target_4]

    TASK [ansible.builtin.debug] ********************************************************************************ok: [ansible_target_1] => {
        "msg": [
            "{'inventory_hostname': 'ansible_target_1', 'host-name': '5a8b1da65a15', 'date': '2023-01-18', 'time': '00:12:46', 'event': 'curl https://retro-pokemon-game-api-k6cgale4bq-uc.a.run.app/pokemon/186', event_result: {'_id': '6241bb164c13370f9824fa9f', 'generation': 2, 'pokedex_number': 186, 'name': 'Politoed', 'description': 'At nightfall, these Pokémon appear on the shores of lakes. They announce their territorial claims by letting out cries that sound like shouting.', 'species': 'Frog Pokémon', 'type_1': 'Water', 'height_m': 1.1, 'weight_kg': 33.9, 'ability_1': 'Water Absorb', 'ability_2': 'Damp', 'ability_hidden': 'Drizzle', 'stat_total': 500, 'hp': 90, 'attack': 75, 'defense': 75, 'sp_attack': 90, 'sp_defense': 100, 'speed': 70, 'sound_link': 'https://play.pokemonshowdown.com/audio/cries/politoed.mp3', 'image_link': 'https://projectpokemon.org/images/normal-sprite/politoed.gif', '__v': 0}}"
        ]
    }
    ok: [ansible_target_2] => {
        "msg": [
            "{'inventory_hostname': 'ansible_target_2', 'host-name': 'e22e00112a1b', 'date': '2023-01-18', 'time': '00:12:46', 'event': 'curl https://retro-pokemon-game-api-k6cgale4bq-uc.a.run.app/pokemon/481', event_result: {'_id': '6241bb164c13370f9824ff12', 'generation': 4, 'pokedex_number': 481, 'name': 'Mesprit', 'description': 'Known as “The Being of Emotion.” It taught humans the nobility of sorrow, pain, and joy.', 'species': 'Emotion Pokémon', 'type_1': 'Psychic', 'height_m': 0.3, 'weight_kg': 0.3, 'ability_1': 'Levitate', 'stat_total': 580, 'hp': 80, 'attack': 105, 'defense': 105, 'sp_attack': 105, 'sp_defense': 105, 'speed': 80, 'sound_link': 'https://play.pokemonshowdown.com/audio/cries/mesprit.mp3', 'image_link': 'https://projectpokemon.org/images/normal-sprite/mesprit.gif', '__v': 0}}"
        ]
    }
    ok: [ansible_target_3] => {
        "msg": [
            "{'inventory_hostname': 'ansible_target_3', 'host-name': 'be5ee28686d6', 'date': '2023-01-18', 'time': '00:12:46', 'event': 'curl https://retro-pokemon-game-api-k6cgale4bq-uc.a.run.app/pokemon/547', event_result: {'_id': '6241bb164c13370f9824fdad', 'generation': 5, 'pokedex_number': 547, 'name': 'Whimsicott', 'description': 'It scatters cotton all over the place as a prank. If it gets wet, it’ll become too heavy to move and have no choice but to answer for its mischief.', 'species': 'Windveiled Pokémon', 'type_1': 'Grass', 'type_2': 'Fairy', 'height_m': 0.7, 'weight_kg': 6.6, 'ability_1': 'Prankster', 'ability_2': 'Infiltrator', 'ability_hidden': 'Chlorophyll', 'stat_total': 480, 'hp': 60, 'attack': 67, 'defense': 85, 'sp_attack': 77, 'sp_defense': 75, 'speed': 116, 'sound_link': 'https://play.pokemonshowdown.com/audio/cries/whimsicott.mp3', 'image_link': 'https://projectpokemon.org/images/normal-sprite/whimsicott.gif', '__v': 0}}"
        ]
    }
    ok: [ansible_target_4] => {
        "msg": [
            "{'inventory_hostname': 'ansible_target_4', 'host-name': '384ab47c40f0', 'date': '2023-01-18', 'time': '00:12:46', 'event': 'curl https://retro-pokemon-game-api-k6cgale4bq-uc.a.run.app/pokemon/708', event_result: {'_id': '6241bb164c13370f9824fe4e', 'generation': 6, 'pokedex_number': 708, 'name': 'Phantump', 'description': 'After a lost child perished in the forest, their spirit possessed a tree stump, causing the spirit’s rebirth as this Pokémon.', 'species': 'Stump Pokémon', 'type_1': 'Ghost', 'type_2': 'Grass', 'height_m': 0.4, 'weight_kg': 7, 'ability_1': 'Natural Cure', 'ability_2': 'Frisk', 'ability_hidden': 'Harvest', 'stat_total': 309, 'hp': 43, 'attack': 70, 'defense': 48, 'sp_attack': 50, 'sp_defense': 60, 'speed': 38, 'sound_link': 'https://play.pokemonshowdown.com/audio/cries/phantump.mp3', 'image_link': 'https://projectpokemon.org/images/normal-sprite/phantump.gif', '__v': 0}}"
        ]
    }

    PLAY RECAP **************************************************************************************************ansible_controller_1       : ok=14   changed=5    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0   
    ansible_target_1           : ok=14   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
    ansible_target_2           : ok=14   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
    ansible_target_3           : ok=14   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
    ansible_target_4           : ok=14   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
    ```

[**view playbook**](sample-playbook.md)
<br />

[↩️](README.md)
