import json
import os

contacts = 'contacts.json'


def save_to_json(data: dict) -> None:
    with open(contacts, 'a', encoding='utf-8') as f:
        if os.stat(contacts).st_size == 0:
            json.dump([data], f, ensure_ascii=False, indent=4)
        else:
            with open(contacts, encoding='utf-8') as json_file:
                data_list = json.load(json_file)
            data_list.append(data)
            with open(contacts, "w", encoding='utf-8') as json_file:
                json.dump(data_list, json_file, ensure_ascii=False, indent=4)