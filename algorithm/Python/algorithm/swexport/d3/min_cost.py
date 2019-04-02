dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def prim(n):
    queue = [(0, 0)]
    inf = 0x7fffffff
    cnt = [[inf]*n for _ in range(n)]
    cnt[0][0] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                h = arr[ny][nx] - arr[y][x]
                if h > 0:
                    if cnt[ny][nx] > cnt[y][x] + 1 + h:
                        cnt[ny][nx] = cnt[y][x] + 1 + h
                        queue.append((nx, ny))
                else:
                    if cnt[ny][nx] > cnt[y][x] + 1:
                        cnt[ny][nx] = cnt[y][x] + 1
                        queue.append((nx, ny))
    return cnt[n-1][n-1]


tcs = int(input())
for tc in range(tcs):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print('#{} {}'.format(tc+1, prim(n)))
