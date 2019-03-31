def __comb(cows, n, r, b, s):
    global ans
    if ans < s or n < r:
        return
    if r == 0:
        if s >= b and ans > s:
            ans = s
    else:
        __comb(cows, n-1, r-1, b, s+cows[n-1])
        __comb(cows, n-1, r, b, s)


def solution(cows, n, b):
    for i in range(1, n+1):
        __comb(cows, n, i, b, 0)


def main():
    global ans
    test_cases = int(input())
    for tc in range(test_cases):
        n, b = map(int, input().split())
        cows = []
        for _ in range(n):
            cows.append(int(input()))
        ans = 0x7fffffff
        solution(cows, n, b)
        print(ans - b)


if __name__ == '__main__':
    main()
