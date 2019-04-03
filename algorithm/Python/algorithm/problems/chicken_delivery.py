def __comb(min_dist, sum_dist, n, r):
    global ans
    if n < r:
        return
    if r == 0:
        s = sum(sum_dist)
        if ans > s:
            ans = s
    else:
        temp = sum_dist[:]
        for i in range(len(min_dist)):
            sum_dist[i] = min(min_dist[i][n-1], sum_dist[i])
        __comb(min_dist, sum_dist, n-1, r-1)
        sum_dist = temp
        __comb(min_dist, sum_dist, n-1, r)


def solution(n, m):
    shops = []
    homes = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                shops.append((j, i))
            if arr[i][j] == 1:
                homes.append((j, i))
    l = len(shops)
    min_dist = [[0]*l for _ in range(len(homes))]
    for i in range(len(homes)):
        home = homes[i]
        for j in range(l):
            min_dist[i][j] = abs(home[0] - shops[j][0]) + abs(home[1] - shops[j][1])
    sum_dist = [0x7fffffff]*len(homes)
    __comb(min_dist, sum_dist, l, m)


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
ans = 0x7fffffff
solution(n, m)
print(ans)