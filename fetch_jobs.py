import requests
import urllib3

from bs4 import BeautifulSoup
from urllib.parse import urljoin

from psu_sources import PSU_SOURCES


urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)



def fetch_jobs():

    jobs = []

    seen = set()


    headers = {
        "User-Agent":
        "Mozilla/5.0"
    }


    remove_words = [

        "home",
        "about",
        "contact",
        "policy",
        "terms",
        "sitemap",
        "quality",
        "manufacturing",
        "products",
        "software products",
        "software services",
        "research development",
        "r&d awards",
        "press",
        "twitter",
        "facebook",
        "youtube",
        "admit card",
        "shortlist",
        "result",
        "answer key",
        "interview schedule",
        "notice",
        "closure",
        "competition",
        "award",
        "regarding",
"change of",
"jurisdiction",
"region",

    ]


    job_words = [

        "career",
        "careers",
        "recruit",
        "vacancy",
        "vacancies",
        "job",
        "opening",
        "opportunity",
        "scientist",
        "engineer",
        "technical assistant",
        "project engineer",
        "research scientist",
        "jrf",
        "apprentice",
        "trainee"

    ]


    cse_words = [

        "computer",
        "computer science",
        "cse",
        "software",
        "information technology",
        "it",
        "data",
        "ai",
        "machine learning",
        "cyber",
        "network",
        "programmer",
        "developer",
        "technical officer",
        "scientist",
        "engineer"

    ]



    for source in PSU_SOURCES:


        try:

            print(
                "Checking:",
                source["name"]
            )


            response = requests.get(

                source["url"],

                headers=headers,

                timeout=20,

                verify=False

            )


            soup = BeautifulSoup(

                response.text,

                "html.parser"

            )



            for a in soup.find_all("a"):


                title = a.get_text(
                    " ",
                    strip=True
                )


                href = a.get("href")


                if not title or not href:
                    continue



                title = " ".join(
                    title.split()
                )


                lower = title.lower()



                # remove useless pages

                if any(

                    x in lower

                    for x in remove_words

                ):

                    continue



                # must look like recruitment

                if not any(

                    x in lower

                    for x in job_words

                ):

                    continue



                # CSE relevance

                if not any(

                    x in lower

                    for x in cse_words

                ):

                    continue



                url = urljoin(

                    source["url"],

                    href

                )



                if url in seen:
                    continue


                seen.add(url)



                jobs.append({

                    "title": title,

                    "link": url,

                    "source": source["name"]

                })



        except Exception as e:


            print(

                source["name"],

                "skipped:",

                str(e)[:100]

            )


    return jobs





if __name__ == "__main__":


    jobs = fetch_jobs()


    print("\n")

    print(
        "FINAL CSE PSU JOBS"
    )


    print(
        "Total:",
        len(jobs)
    )


    for job in jobs:


        print("----------------")

        print(
            job["title"]
        )

        print(
            job["source"]
        )

        print(
            job["link"]
        )