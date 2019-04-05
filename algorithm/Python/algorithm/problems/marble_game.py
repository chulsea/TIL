dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(srx, sry, sbx, sby, fx, fy):
    queue = [(srx, sry, sbx, sby, 0)]
    visited[sry][srx][sby][sbx] = 1
    while queue:
        rx, ry, bx, by, c = queue.pop(0)
        for i in range(4):
            nrx = rx + dx[i]
            nry = ry + dy[i]
            nbx = bx + dx[i]
            nby = by + dy[i]
            if arr[nby][nbx] == '#':
                nbx = bx
                nby = by
            if arr[nry][nrx] == '#':
                nrx = rx
                nry = ry
            if nrx == fx and nry == fy:
                return c + 1
            if nbx == fx and nby == fy:
                continue
            if (nrx != nbx or nry != nby) and not visited[nry][nrx][nby][nbx] and c < 10:
                visited[nry][nrx][nby][nbx] = 1
                queue.append((nrx, nry, nbx, nby, c+1))
    return -1


tcs = int(input())
for tc in range(tcs):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(input()))
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                rx, ry = j, i
            elif arr[i][j] == 'B':
                bx, by = j, i
            elif arr[i][j] == 'H':
                fx, fy = j, i
    visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    print(bfs(rx, ry, bx, by, fx, fy))