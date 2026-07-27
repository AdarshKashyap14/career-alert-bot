from fetch_jobs import fetch_jobs
from pdf_checker import check_pdf
from telegram_bot import send_message



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


    print("\n")

    print(
        "Checking CSE eligibility..."
    )


    matched = []



    for job in jobs:


        print(
            "Checking:",
            job["title"][:60]
        )


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
        "Final CSE Eligible:",
        len(matched)
    )



    if matched:


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



if __name__ == "__main__":

    main()