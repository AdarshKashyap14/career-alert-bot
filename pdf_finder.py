import requests
from bs4 import BeautifulSoup


def find_pdf_link(url):

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )


        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        for link in soup.find_all("a"):

            href = link.get("href")


            if href and ".pdf" in href.lower():

                if href.startswith("http"):
                    return href

                return "https://www.isro.gov.in" + href


        return None


    except Exception as e:

        print("PDF finder error:", e)
        return None