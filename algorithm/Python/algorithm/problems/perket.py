def __cal_taste(selected, l):
    m, s = 1, 0
    for i in range(l):
        j, k = selected[i]
        m *= j
        s += k
    return abs(m - s)


def __comb(gredients, selected, n, r, l):
    global ans
    if n < r:
        return
    if r == 0:
        taste = __cal_taste(selected, l)
        if ans > taste:
            ans = taste
    else:
        selected[r-1] = gredients[n-1]
        __comb(gredients, selected, n-1, r-1, l)
        __comb(gredients, selected, n-1, r, l)


def solution(n, gredients):
    selected = [0]*n
    for i in range(1, n+1):
        __comb(gredients, selected, n, i, i)


def main():
    global ans
    n = int(input())
    gredients = []
    for _ in range(n):
        gredients.append(list(map(int, input().split())))
    ans = 0x7fffffff
    solution(n, gredients)
    print(ans)


if __name__ == '__main__':
    main()
