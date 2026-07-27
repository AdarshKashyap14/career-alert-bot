from fetch_jobs import fetch_jobs
from pdf_checker import check_pdf
from telegram_bot import send_message
from history import is_new_job, add_job
from date_filter import is_recent

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import urllib3


urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)



def find_pdf_link(url):

    try:

        response = requests.get(
            url,
            timeout=20,
            verify=False,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )


        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        # Normal PDF links

        for a in soup.find_all(
            "a",
            href=True
        ):

            href = a["href"]


            if ".pdf" in href.lower():

                return urljoin(
                    url,
                    href
                )



        # PDF hidden in source

        pdfs = re.findall(
            r'["\']([^"\']+\.pdf)["\']',
            response.text,
            re.IGNORECASE
        )


        if pdfs:

            return urljoin(
                url,
                pdfs[0]
            )



    except Exception as e:

        print(
            "PDF search error:",
            e
        )


    return None





def clean_title(title):


    ignore = [

        "closure",
        "result",
        "selected",
        "shortlisted",
        "interview schedule",
        "admit card",
        "dv/pi",
        "answer key",
        "corrigendum",
        "application count",
        "provisional list"

    ]


    title = title.lower()


    for word in ignore:

        if word in title:

            return False


    return True






def main():


    jobs = fetch_jobs()


    print(
        "\nChecking CSE eligibility...\n"
    )


    matched = []



    for job in jobs:


        title = job["title"]



        print(
            "Checking:",
            title[:80]
        )



        # Remove useless notices

        if not clean_title(title):

            print(
                "Ignored old notice"
            )

            continue




        # FIRST check date
        # No PDF download for old jobs

        if not is_recent(title):

            print(
                "Old advertisement skipped"
            )

            continue




        # Duplicate check

        if not is_new_job(
            job["link"]
        ):

            print(
                "Already sent - skipping"
            )

            continue





        # Search PDF only after date validation

        pdf = find_pdf_link(
            job["link"]
        )



        if not pdf:

            print(
                "Recent job but PDF not found"
            )

            continue




        print(
            "PDF Found:",
            pdf
        )



        try:

            eligible = check_pdf(
                pdf
            )


        except Exception as e:

            print(
                "PDF Error:",
                e
            )

            continue





        if eligible:


            matched.append({

                "title": title,

                "source": job["source"],

                "link": job["link"],

                "pdf": pdf

            })







    print("\n")

    print(
        "New CSE Eligible Jobs:",
        len(matched)
    )



    if not matched:

        print(
            "No new jobs found"
        )

        return





    message = (
        "🚀 CSE PSU JOB ALERT\n\n"
    )



    for job in matched:


        message += (

            "🏢 "
            + job["source"]
            + "\n\n"


            "📌 "
            + job["title"]
            + "\n\n"


            "🔗 Apply:\n"
            + job["link"]
            + "\n\n"


            "📄 Notification PDF:\n"
            + job["pdf"]
            + "\n\n"


            "-------------------\n\n"

        )





    send_message(
        message
    )




    for job in matched:

        add_job(
            job["link"]
        )







if __name__ == "__main__":

    main()