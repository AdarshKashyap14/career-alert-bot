def is_cse_govt_job(job):

    text = (
        job["title"]
        + " "
        + job["description"]
    ).lower()


    # Remove non-relevant updates
    ignore_keywords = [
        "interview schedule",
        "shortlisted",
        "result",
        "answer key",
        "merit list",
        "selected candidates"
    ]


    if any(word in text for word in ignore_keywords):
        return False



    # Remove non-CSE technical branches
    exclude_keywords = [
        "mechanical",
        "civil",
        "electrical",
        "electronics",
        "cook",
        "stenographer",
        "personal assistant",
        "library assistant",
        "draughtsman",
        "clerk"
    ]


    if any(word in text for word in exclude_keywords):
        return False



    # PSU technical positions
    technical_keywords = [
        "scientist",
        "engineer",
        "technical",
        "research",
        "jrf",
        "project associate",
        "apprentice",
        "trainee"
    ]


    if not any(
        word in text
        for word in technical_keywords
    ):
        return False


    # PSU organizations
    govt_keywords = [
        "isro",
        "drdo",
        "bel",
        "ecil",
        "barc",
        "hal",
        "ntpc",
        "iocl",
        "ongc"
    ]


    if not any(
        word in text
        for word in govt_keywords
    ):
        return False


    return True