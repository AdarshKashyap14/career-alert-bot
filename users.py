import json
import os


FILE = "users.json"


def load_users():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)



def add_user(chat_id):

    users = load_users()

    if chat_id not in users:

        users.append(chat_id)

        with open(FILE, "w") as f:
            json.dump(users, f, indent=4)



def remove_user(chat_id):

    users = load_users()

    if chat_id in users:

        users.remove(chat_id)

        with open(FILE, "w") as f:
            json.dump(users, f, indent=4)