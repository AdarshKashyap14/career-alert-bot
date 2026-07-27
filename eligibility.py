import requests
from bs4 import BeautifulSoup


def check_cse_eligibility(url):

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


    text = soup.get_text(
        " ",
        strip=True
    ).lower()


    print("\nCHECKING:", url)
    print(text[:500])


    return False