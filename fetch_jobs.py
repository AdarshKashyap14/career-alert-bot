import requests

from bs4 import BeautifulSoup

from urllib.parse import urljoin

from psu_sources import PSU_SOURCES

from date_filter import is_recent



def fetch_jobs():

    jobs = []


    headers = {

        "User-Agent":
        "Mozilla/5.0"

    }



    ignore_words = [

        "home",
        "about",
        "contact",
        "login",
        "privacy",
        "sitemap",
        "facebook",
        "twitter",
        "youtube",
        "quality",
        "products",
        "technology",
        "research",
        "policy",
        "terms",
        "result",
        "interview",
        "shortlist",
        "schedule",
        "closure",
        "appointment"

    ]



    keywords = [

        "recruit",
        "advert",
        "vacancy",
        "notification",
        "engineer",
        "scientist",
        "trainee",
        "fellow",
        "apprentice",
        "assistant",
        "officer",
        "junior",
        "associate",
        "project"

    ]



    for source in PSU_SOURCES:


        print(
            "Checking:",
            source["name"]
        )


        try:


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



            found = 0



            for link in soup.find_all("a"):


                title = link.get_text(

                    " ",

                    strip=True

                )


                href = link.get("href")



                if not title or not href:

                    continue



                title_lower = title.lower()



                # remove useless links

                if any(

                    word in title_lower

                    for word in ignore_words

                ):

                    continue




                # only recruitment pages

                if not any(

                    word in title_lower

                    for word in keywords

                ):

                    continue




                # check only last 5 days

                if not is_recent(title):

                    print(

                        "Skipping old/no date:",

                        title[:80]

                    )

                    continue




                full_url = urljoin(

                    source["url"],

                    href

                )



                job = {

                    "title": title,

                    "link": full_url,

                    "source": source["name"]

                }



                jobs.append(job)


                found += 1


                print(

                    "Added:",

                    title[:80]

                )




            print(

                source["name"],

                "recent jobs:",

                found

            )




        except Exception as e:


            print(

                source["name"],

                "skipped:",

                e

            )



    return jobs