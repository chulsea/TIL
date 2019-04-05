def solution(adj, n, m):
    queue = [0]
    color[0] = 1
    while queue:
        cur = queue.pop(0)
        for i in range(n):
            if adj[cur][i] and not color[i]:
                queue.append(i)


n, m = map(int, input().split())
adj = [[0]*n for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)-1):
        if temp[j]:
            adj[i][j] = 1
            adj[j][i] = 1
color = [0]*n
solution(adj, n, m)
print(*color)