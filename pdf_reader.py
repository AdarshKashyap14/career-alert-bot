import requests
from pypdf import PdfReader
from io import BytesIO


CSE_KEYWORDS = [
    "computer science",
    "computer engineering",
    "information technology",
    "software engineering",
    "artificial intelligence",
    "machine learning",
]


def check_pdf_for_cse(pdf_url):

    try:

        response = requests.get(
            pdf_url,
            timeout=15
        )

        pdf = PdfReader(
            BytesIO(response.content)
        )


        text = ""

        for page in pdf.pages:
            text += page.extract_text() or ""


        text = text.lower()


        for keyword in CSE_KEYWORDS:
            if keyword in text:
                return True


        return False


    except Exception as e:

        print("PDF Error:", e)
        return False