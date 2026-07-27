import requests
import io
import pdfplumber


CSE_KEYWORDS = [

    "computer science",
    "computer engineering",
    "information technology",
    "software engineering",
    "computer applications",
    "data science",
    "artificial intelligence",
    "machine learning",
    "cyber security",
    "computer technology"

]


def check_pdf(pdf_url):

    try:

        response = requests.get(
            pdf_url,
            timeout=30
        )


        with pdfplumber.open(
            io.BytesIO(response.content)
        ) as pdf:


            text = ""


            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text



        text = text.lower()



        for keyword in CSE_KEYWORDS:

            if keyword in text:

                return True


        return False



    except Exception as e:

        print(
            "PDF Error:",
            e
        )

        return False
