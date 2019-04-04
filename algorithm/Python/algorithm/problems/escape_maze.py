
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if arr[i][j] == 3:
            sx, sy = j, i
            break
visited = [[0]*m for _ in range(n)]
print(dfs(sx, sy, 3, 1))