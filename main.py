from fetch_jobs import fetch_jobs
from filters import is_cse_govt_job


jobs = fetch_jobs()


print("Filtered CSE PSU Jobs\n")


count = 0


for job in jobs:

    if is_cse_govt_job(job):

        count += 1

        print("----------------")
        print(job["title"])
        print(job["link"])


print("\nTotal matched:", count)