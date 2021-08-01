import requests
from bs4 import BeautifulSoup

URL = "https://www.oxfam.org/en/take-action/jobs/affiliates"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

result = soup.find("div", class_= "item-list")

results = result.find_all("h3", class_="pb-1")

for result_i in results:
    print(result_i.text)
