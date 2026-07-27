import json
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")


def send_message(message):
    with open("users.json", "r") as f:
        users = json.load(f)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    for chat_id in users:
        try:
            r = requests.post(
                url,
                data={
                    "chat_id": chat_id,
                    "text": message,
                    "disable_web_page_preview": True,
                },
                timeout=20,
            )
            print(f"{chat_id}: {r.text}")
        except Exception as e:
            print(e)