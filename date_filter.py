from datetime import datetime, timedelta
import re


RECENT_DAYS = 5



def extract_date(text):

    patterns = [

        # 27-07-2026
        r"\d{2}[-./]\d{2}[-./]\d{4}",

        # 27 July 2026
        r"\d{1,2}\s[A-Za-z]+\s\d{4}",

        # July 27, 2026
        r"[A-Za-z]+\s\d{1,2},\s\d{4}"

    ]


    for pattern in patterns:

        match = re.search(
            pattern,
            text
        )


        if match:

            value = match.group()


            formats = [

                "%d-%m-%Y",
                "%d/%m/%Y",
                "%d.%m.%Y",

                "%d %B %Y",

                "%B %d, %Y"

            ]


            for fmt in formats:

                try:

                    return datetime.strptime(
                        value,
                        fmt
                    )


                except:

                    pass


    return None




def is_recent(text):


    date = extract_date(text)


    if not date:

        return False



    today = datetime.now()


    return date >= (
        today - timedelta(days=RECENT_DAYS)
    )