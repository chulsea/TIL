import requests as req
from bs4 import BeautifulSoup

url = "https://wikidocs.net/20"
res = req.get(url)
soup = BeautifulSoup(res.text, "html.parser")
data = soup.select(".list-group a span span")
for d in data:
    print(d.text.strip())