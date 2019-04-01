def floyd(n, adj):
    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if j == i or j == k:
                    continue
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])


tcs = int(input())
inf = 0x7fffffff
for tc in range(tcs):
    inputs = input().split()
    n = int(inputs[0])
    adj = [[0]*n for _ in range(n)]
    k = 1
    for i in range(n):
        for j in range(n):
            temp = int(inputs[k])
            if i == j:
                adj[i][j] = 0
            elif temp:
                adj[i][j] = temp
            else:
                adj[i][j] = inf
            k += 1
    floyd(n, adj)
    ans = inf
    for i in range(n):
        cc = 0
        for j in range(n):
            cc += adj[i][j]
        ans = min(ans, cc)
    print('#{} {}'.format(tc+1, ans))