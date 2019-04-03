# subset을 내부에서 subset을 한번더 돌리는 것보다 추를 왼쪽, 오른쪽, 두지 않는 경우로 나눠서 구분

def __sub_power_set(n, r, total):
    global ans
    if ans:
        return
    if n == r:
        other = 0
        for i in range(n):
            if chk[i] == 2:
                other += weights[i]
        if total == other:
            ans = True
    else:
        if chk[r] != 1:
            chk[r] = 2
            __sub_power_set(n, r+1, total)
            chk[r] = 0
            __sub_power_set(n, r+1, total)
        else:
            __sub_power_set(n, r+1, total)


def __power_set(n, r, marble):
    global ans
    if ans:
        return
    if n == r:
        total = 0
        for i in range(n):
            if chk[i]:
                total += weights[i]
        if marble == total:
            ans = True
        __sub_power_set(n, 0, total+marble)
    else:
        chk[r] = 1
        __power_set(n, r+1, marble)
        chk[r] = 0
        __power_set(n, r+1, marble)


n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))
for i in range(m):
    chk = [0] * n
    ans = False
    __power_set(n, 0, marbles[i])
    if ans:
        print('Y', end=' ')
    else:
        print('N', end=' ')