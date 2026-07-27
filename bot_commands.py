from users import add_user, remove_user


def handle_command(message):

    chat_id = message["chat"]["id"]

    text = message["text"]


    if text == "/start":

        add_user(chat_id)

        return """
🚀 Welcome to CSE Career Alert Bot

You are subscribed.

You will receive:

✅ CSE PSU Jobs
✅ Government Recruitment
✅ Official PDFs
✅ Higher Studies Updates

"""



    elif text == "/stop":

        remove_user(chat_id)

        return """
❌ You have unsubscribed.
"""


    elif text == "/help":

        return """
Commands:

/start - Subscribe alerts
/stop - Stop alerts
/jobs - Latest jobs
/exams - Upcoming exams
"""
