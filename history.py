import json
import os


FILE = "job_history.json"



def load_history():

    if not os.path.exists(FILE):

        return []


    with open(FILE, "r") as f:

        return json.load(f)




def save_history(history):

    with open(FILE, "w") as f:

        json.dump(
            history,
            f,
            indent=4
        )




def is_new_job(link):

    history = load_history()

    return link not in history




def add_job(link):

    history = load_history()


    if link not in history:

        history.append(link)


    save_history(history)
