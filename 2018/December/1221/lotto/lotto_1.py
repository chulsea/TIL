import random, requests as req
from bs4 import BeautifulSoup

# 8회차 분량의 당첨번호 뽑아오기 (web crawling)
def main():
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
    numbers = sorted(random.sample(range(810,838), 8))
    for num in numbers:
        search = url + str(num)
        data = _get_data(search)
        _print(num, data)

def _get_data(url):
    res = req.get(url).text
    soup = BeautifulSoup(res, "html.parser")
    lucky = soup.select_one(".win_result")
    wins = lucky.select(".win .ball_645")
    bonus = lucky.select_one(".bonus .ball_645").text
    return wins, bonus

def _print(num, data):
    result = []
    for win in data[0]:
        result.append(win.text)
    print(f"{num}회차 당첨번호")
    for r in result:
        print(f"{r}", end=" ")
    print(f"+ {data[1]}")

if __name__ == "__main__":
    main()