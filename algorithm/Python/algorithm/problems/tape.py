def __comb(tapes, n, r):
    global ans
    if n < r:
        return
    if r == 0:
        tape1 = tape2 = 0
        for i in range(len(chk)):
            if chk[i]:
                tape1 += tapes[i]
            else:
                tape2 += tapes[i]
        result = abs(tape1 - tape2)
        if result < ans:
            ans = result
    else:
        chk[n-1] = 1
        __comb(tapes, n-1, r-1)
        chk[n-1] = 0
        __comb(tapes, n-1, r)


n = int(input())
l = n // 2
tapes = list(map(int, input().split()))
ans = 0x7fffffff
chk = [0]*n
__comb(tapes, n, l)
print(ans)