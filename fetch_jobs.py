import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


PSU_SOURCES = [
    {
        "name": "ISRO",
        "url": "https://www.isro.gov.in/Careers.html"
    },
    {
        "name": "DRDO",
        "url": "https://drdo.gov.in/drdo/en/offerings/vacancies"
    }
]


def fetch_jobs():

    jobs = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }


    for source in PSU_SOURCES:

        try:

            response = requests.get(
                source["url"],
                headers=headers,
                timeout=15
            )


            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )


            for link in soup.find_all("a"):

                title = link.get_text(
                    " ",
                    strip=True
                )

                href = link.get("href")


                if not title or not href:
                    continue


                # Remove useless navigation links
                ignore = [
                    "home",
                    "english",
                    "hindi",
                    "about",
                    "contact",
                    "team",
                    "technology",
                    "products",
                    "publications",
                    "photos",
                    "videos",
                    "conference",
                    "here"
                ]


                if any(
                    word in title.lower()
                    for word in ignore
                ):
                    continue


                # Keep only recruitment related pages
                keywords = [
                    "recruit",
                    "scientist",
                    "engineer",
                    "trainee",
                    "assistant",
                    "officer",
                    "fellow",
                    "vacanc",
                    "apprentice"
                ]


                if not any(
                    word in title.lower()
                    for word in keywords
                ):
                    continue


                full_url = urljoin(
                    source["url"],
                    href
                )


                jobs.append(
                    {
                        "title": title,
                        "link": full_url,
                        "description": source["name"]
                    }
                )


        except Exception as e:

            print(
                source["name"],
                "error:",
                e
            )


    return jobs