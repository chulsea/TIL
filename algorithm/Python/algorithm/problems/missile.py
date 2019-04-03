def __cal_live_ship():
    temp = [ships[i][:] for i in range(len(ships))]
    cnt = len(temp)
    for i in chk:
        bx, by, be = temp[i]
        if be <= 0:
            break
        for t in temp:
            if t[2] <= 0:
                continue
            if abs(bx - t[0]) + abs(by - t[1]) <= missile[2]:
                t[2] -= missile[1]
                if t[2] <= 0:
                    cnt -= 1
    return cnt


def __comb(n, r):
    global ans
    if n == 0:
        return
    if r == 0:
        lived = __cal_live_ship()
        if ans > lived:
            ans = lived
    else:
        chk[r-1] = n-1
        __comb(n-1, r)
        chk[r-1] = n-1
        __comb(n, r-1)


n = int(input())
ships = []
for _ in range(n):
    ships.append(list(map(int, input().split())))
missile = list(map(int, input().split()))
r = missile[0]
chk = [0]*r
ans = 0x7fffffff
__comb(n, r)
print(ans)