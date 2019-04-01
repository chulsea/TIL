def prim(n, adj, dist, r):
    dist[r][0] = 0
    visited = [0]*n
    while 0 in visited:
        visited[r] = 1
        for i in range(n):
            if not visited[i] and adj[r][i] and adj[r][i] < dist[i][0]:
                dist[i][0] = adj[r][i]
                dist[i][1] = r
        min_v = 0x7fffffff
        for i in range(n):
            if not visited[i]:
                if dist[i][0] < min_v:
                    min_v = dist[i][0]
                    r = i


tcs = int(input())
for tc in range(tcs):
    v, e = map(int, input().split())
    n = v+1
    adj = [[0]*n for _ in range(n)]
    for _ in range(e):
        x, y, w = map(int, input().split())
        adj[y][x] = w
        adj[x][y] = w
    inf = 0x7fffffff
    dist = [[inf, i] for i in range(n)]
    prim(n, adj, dist, 0)
    ans = 0
    for i in range(n):
        ans += dist[i][0]
    print('#{} {}'.format(tc+1, ans))