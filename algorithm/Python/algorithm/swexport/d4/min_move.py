def dijkstra(n, adj, dist, s):
    visited = [0]*n
    dist[s] = 0
    while 0 in visited:
        visited[s] = 1
        for i in range(n):
            if not visited[i] and adj[s][i]:
                dist[i] = min(dist[s] + adj[s][i], dist[i])
        min_dist = 0x7fffffff
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                s = i


tcs = int(input())
for tc in range(tcs):
    v, e = map(int, input().split())
    n = v + 1
    adj = [[0]*n for _ in range(n)]
    for _ in range(e):
        x, y, w = map(int, input().split())
        adj[x][y] = w
    dist = [0x7fffffff]*n
    dijkstra(n, adj, dist, 0)
    print('#{} {}'.format(tc+1, dist[v]))