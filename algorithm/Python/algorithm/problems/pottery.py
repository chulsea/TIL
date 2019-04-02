def __check(args):
    l = len(args)
    k = len(potterys)
    chk = [0]*k
    for p in range(k):
        count_p = [0] * 27
        count_a = [0] * 27
        for i in range(l):
            count_p[potterys[p][i]] += 1
            count_a[args[i]] += 1
        for i in range(26):
            if count_a[i + 1] != count_p[i + 1]:
                chk[p] = 1
                break
    if k == 0 or 0 not in chk:
        return True
    return False


def __comb(n, r, *args):
    if n < r:
        return
    if r == 0:
        if __check(args):
            potterys.append(args)
    else:
        __comb(n-1, r-1, *args, soils[n-1])
        __comb(n-1, r, *args)


tcs = int(input())
for tc in range(tcs):
    n, m = map(int, input().split())
    soils = list(map(int, input().split()))
    potterys = []
    __comb(n, m)
    print(len(potterys))
