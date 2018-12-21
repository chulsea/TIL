import random, requests as req, json

def _get_data(url, round_num):
    lottery_data = json.loads(req.get(f"{url}{round_num}").text)
    round_win_num = []
    bonus = lottery_data["bnusNo"]
    for i in range(1,7):
        idx = f"drwtNo{i}"
        round_win_num.append(lottery_data[idx])
    return round_win_num, bonus

def _get_rank_and_count(win_round_num, bonus):
    prize = 0
    my_numbers = []
    win_count = 0
    while prize != 1:
        my_numbers = set(random.sample(range(1,46), 6))
        count = len(my_numbers.intersection(win_round_num))
        if count == 5 and bonus in my_numbers:
            prize = 2
            print(f"{win_count}번째에 2등 당첨입니다!!")
        elif count == 6:
            prize = 1
        elif count == 5:
            prize = 3
            print(f"{win_count}번째에 3등 당첨입니다!!")
        elif count == 4:
            prize = 4
        elif count == 3:
            prize = 5
        win_count += 1
    return win_count, prize, my_numbers

def main():
    url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
    round_num = 837
    # input("찾아볼 회차를 입력해주세요 : ")
    win_round_num, bonus = _get_data(url, round_num)
    win_count, prize, my_numbers = _get_rank_and_count(win_round_num, bonus)
    print(f"{win_count}번 만에 {prize}등으로 당첨되셨습니다!!\n{sorted(my_numbers)}")

if __name__ == "__main__":
    main()