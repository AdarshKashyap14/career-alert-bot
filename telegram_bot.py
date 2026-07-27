import requests
import config


def send_message(message):

    url = (
        f"https://api.telegram.org/bot"
        f"{config.BOT_TOKEN}/sendMessage"
    )


    data = {
        "chat_id": config.CHAT_ID,
        "text": message
    }


    response = requests.post(
        url,
        data=data
    )


    return response.json()