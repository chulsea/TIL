def perm(chk, n, r, start, s):
    global ans
    if ans < s:
        return
    if n-1 == r:
        if cost[start][0] == 0:
            return
        s += cost[start][0]
        if s < ans:
            ans = s
    else:
        for i in range(1, n):
            if cost[start][i] and not chk[i]:
                chk[i] = 1
                perm(chk, n, r+1, i, s+cost[start][i])
                chk[i] = 0


n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
chk = [0]*n
ans = 0x7fffffff
for i in range(1, n):
    if cost[0][i]:
        chk[i] = 1
        perm(chk, n, 1, i, cost[0][i])
        chk[i] = 0
print(ans)