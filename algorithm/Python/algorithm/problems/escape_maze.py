def bfs(n, m):
    queue = [(sx, sy, 3)]
    cnt[3][sy][sx] = 0
    while queue:
        x, y, b = queue.pop(0)
        if arr[y][x] == 4:
            return cnt[b][y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if arr[ny][nx] != 1:
                if (arr[ny][nx] == 0 or arr[ny][nx] == 4) and cnt[b][y][x]+1 < cnt[b][ny][nx]:
                    cnt[b][ny][nx] = cnt[b][y][x] + 1
                    queue.append((nx, ny, b))
                elif (arr[ny][nx] == 2 or arr[ny][nx] == 4) and b > 0 and cnt[b][y][x]+1 < cnt[b-1][ny][nx]:
                    cnt[b-1][ny][nx] = cnt[b][y][x] + 1
                    queue.append((nx, ny, b-1))
    return -1

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
cnt = [[[1000]*m for _ in range(n)] for _ in range(4)]
print(bfs(n, m))