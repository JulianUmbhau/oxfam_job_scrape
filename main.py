import requests
from bs4 import BeautifulSoup

URL = "https://www.oxfam.org/en/take-action/jobs/affiliates" # page 1 

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

page_list = []
for a in soup.find_all("a", href=True):
    if "page" in a["href"]:
        print(a["href"])
        page_list.append("https://www.oxfam.org/en/take-action/jobs/affiliates" + a["href"])

job_list = []
for page in page_list:
    page = requests.get(page)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_= "item-list")
    results = result.find_all("h3", class_="pb-1")
    for result_i in results:
        print(result_i.text)
        job_list.append(result_i.text)

search_terms = ["data","engineer","scientist","science"]

data_jobs_list = []
for job in job_list:
    if any(xs in job for xs in search_terms):
        data_jobs_list.append(job)
        print("Data job found")
