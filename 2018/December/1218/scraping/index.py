import requests as req
from bs4 import BeautifulSoup

data = req.get("https://www.naver.com/")
# data = req.get("https://finance.naver.com/sise/")
# data = req.get("https://wikidocs.net/20")
# requests로 data 가져오기
soup = BeautifulSoup(data.text, "html.parser")
# BeautifulSoup으로 data 이쁘게 가져오기
# h1 = soup.select_one("#if").text
# print(h1)
# print(soup.select_one(""))
# 데이터 가져오기 (선택자를 이용해서)
# populars = [popular.text.strip() for popular in soup.select("#PM_ID_ct .PM_CL_realtimeKeyword_rolling_base .ah_item .ah_k")]
populars = soup.select(".PM_CL_realtimeKeyword_rolling_base .ah_item")
for tag in populars:
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    s = f"{rank}위는 {name}입니다!"
    print(s)
# print(populars)
