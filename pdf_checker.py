import requests
import pdfplumber
import io
import re


CSE_KEYWORDS = [
    "computer science",
    "computer engineering",
    "information technology",
    "software",
    "programming",
    "computer applications",
    "computer technology",
    "cse",
    "b.tech computer",
    "b.e computer"
]


NON_CSE_KEYWORDS = [
    "stenographer",
    "cook",
    "driver",
    "fireman",
    "security guard"
]


def check_pdf(pdf_url):

    try:

        print("PDF checking...")


        response = requests.get(
            pdf_url,
            timeout=30,
            verify=False
        )


        pdf_file = io.BytesIO(
            response.content
        )


        text = ""


        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text.lower()



        # Remove extra spaces

        text = re.sub(
            r"\s+",
            " ",
            text
        )



        # Check CSE related words

        for keyword in CSE_KEYWORDS:

            if keyword in text:

                print(
                    "CSE Match:",
                    keyword
                )

                return True



        # Special handling for mixed advertisements

        # Example:
        # Assistant + Stenographer together

        mixed_posts = [
            "assistant",
            "junior personal assistant",
            "technical assistant",
            "scientist",
            "engineer",
            "programmer"
        ]


        has_valid_post = False


        for post in mixed_posts:

            if post in text:

                has_valid_post = True



        if has_valid_post:

            print(
                "Possible CSE related mixed advertisement"
            )

            return True



        print(
            "Rejected: no CSE related post"
        )

        return False



    except Exception as e:

        print(
            "PDF error:",
            e
        )

        return False