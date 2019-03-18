def __cal_distance(n, m, d, l):
    if d == 1:
        result = l
    elif d == 2:
        result = n*2 + m - l
    elif d == 3:
        result = (n+m)*2 - l
    elif d == 4:
        result = n + l
    return result


def solution(n, m, shops, sec):
    std = n + m
    answer = 0
    sec_dist = __cal_distance(n, m, sec[0], sec[1])
    for d, l in shops:
        shop_dist = __cal_distance(n, m, d, l)
        temp = abs(sec_dist - shop_dist)
        answer += temp if temp < std else 2*std - temp
    return answer


def main():
    n, m = map(int, input().split())
    k = int(input())
    shops = []
    for _ in range(k):
        shops.append(list(map(int, input().split())))
    sec = list(map(int, input().split()))
    print(solution(n, m, shops, sec))


if __name__ == '__main__':
    main()
