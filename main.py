from fetch_jobs import fetch_jobs
from pdf_checker import check_pdf
from telegram_bot import send_message
from history import is_new_job, add_job


def find_pdf_link(url):

    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin


    try:

        response = requests.get(
            url,
            timeout=20,
            verify=False
        )


        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        for a in soup.find_all("a"):

            href = a.get("href")


            if href and ".pdf" in href.lower():

                return urljoin(
                    url,
                    href
                )


    except Exception as e:

        print(
            "PDF search error:",
            e
        )


    return None




def main():


    jobs = fetch_jobs()


    print("\nChecking CSE eligibility...\n")


    matched = []



    for job in jobs:


        print(
            "Checking:",
            job["title"][:70]
        )


        # Skip already sent jobs

        if not is_new_job(job["link"]):

            print(
                "Already sent - skipping"
            )

            continue



        pdf = find_pdf_link(
            job["link"]
        )


        if not pdf:

            continue



        eligible = check_pdf(
            pdf
        )



        if eligible:


            matched.append({

                "title": job["title"],

                "source": job["source"],

                "link": job["link"],

                "pdf": pdf

            })



    print("\n")

    print(
        "New CSE Eligible Jobs:",
        len(matched)
    )



    if len(matched) == 0:

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

            "-------------------\n"

        )



    send_message(
        message
    )



    # Save sent jobs

    for job in matched:

        add_job(
            job["link"]
        )





if __name__ == "__main__":

    main()