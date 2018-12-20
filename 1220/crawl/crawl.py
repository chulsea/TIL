import requests as req
from bs4 import BeautifulSoup
import csv

url = "https://m.stock.naver.com/marketindex/index.nhn"
res = req.get(url).text
soup = BeautifulSoup(res, "html.parser")
stocks = soup.select(".international_lst .stock_up a")
intermarket = {}
for stock in stocks:
    item = stock.select_one(".item_wrp .stock_item").text
    s = stock.select_one(".price_wrp .stock_price").text
    intermarket[item] = s
print(intermarket)

currencys = soup.select(".exchg_on .lst_wrp li a")
exg = {}
for currency in currencys:
    item = currency.select_one(".item_wrp .stock_item").text
    c = currency.select_one(".price_wrp .stock_price").text
    exg[item] = c
print(exg)


with open("currency.csv", "w", encoding="utf-8") as csvf:
    writer = csv.DictWriter(csvf, ["country", "currency"])
    writer.writeheader()
    writer.writerows(exg)
