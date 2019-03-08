# 기준점 잡기! 기준점을 잡고 위치와 비교하여 길이를 구한다.
# 외곽의 둘레보다 반 이상 이동하면 돌아가는 것 (반대로 계산)

def solution(n, m, shops, sec):
    answer = 0
    sd, sl = sec
    for d, l in shops:
        if sd < 3:
            if abs(sd - d) == 0:
                answer += abs(l - sl)
            elif (d == 1 or d == 2) and abs(sd - d) == 1:
                answer += min(m + l + sl, n - l + n - sl + m)
            else:
                if sd == 1 and d == 3:
                    answer += l + sl
                elif sd == 1 and d == 4:
                    answer += n - sl + l
                elif sd == 2 and d == 3:
                    answer += sl + m - l
                elif sd == 2 and d == 4:
                    answer += n - sl + m - l
        else:
            if abs(sd - d) == 0:
                answer += abs(l - sl)
            elif (d == 3 or d == 4) and abs(sd - d) == 1:
                answer += min(n + l + sl, m - l + m - sl + n)
            else:
                if sd == 3 and d == 1:
                    answer += l + sl
                elif sd == 3 and d == 2:
                    answer += m - sl + l
                elif sd == 4 and d == 1:
                    answer += sl + n - l
                elif sd == 4 and d == 2:
                    answer += n - l + m - sl
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
