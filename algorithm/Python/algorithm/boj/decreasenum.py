dp = [i for i in range(10)]

def make_dp(n):
    if n < 10:
        return n
    for i in range(10, 1000000000):
        t1, prev = i, -float('inf')
        while t1 > 0:
            t2 = t1 % 10
            if prev >= t2:
                break
            prev = t2
            t1 //= 10
        if t1 == 0:
            dp.append(i)
        if len(dp) == n+1:
            return


def main():
    n = int(input())
    make_dp(n)
    try:
        print(dp[n])
    except IndexError:
        print(-1)


if __name__ == '__main__':
    main()
