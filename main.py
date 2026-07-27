from fetch_jobs import fetch_jobs
from filters import is_cse_govt_job
from pdf_finder import find_pdf_link
from pdf_reader import check_pdf_for_cse
from telegram_bot import send_message

jobs = fetch_jobs()


print("Final CSE PSU Jobs\n")


count = 0


for job in jobs:


    if is_cse_govt_job(job):


        pdf = find_pdf_link(
            job["link"]
        )


        if pdf:


            eligible = check_pdf_for_cse(pdf)


            if eligible:

                count += 1
message = "🚀 Daily CSE PSU Job Alert\n\n"

count = 0


for job in jobs:

    if is_cse_govt_job(job):

        pdf = find_pdf_link(job["link"])


        if pdf and check_pdf_for_cse(pdf):

            count += 1

            message += (
                "🏢 PSU: ISRO\n"
                f"📌 {job['title']}\n"
                f"🔗 {job['link']}\n\n"
            )


message += f"Total Jobs: {count}"


send_message(message)



print("\nTotal CSE Eligible:", count)