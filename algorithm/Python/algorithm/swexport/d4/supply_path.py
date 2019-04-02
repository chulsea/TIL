dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def prim(n):
    queue = [(0, 0)]
    cnt = [[0x7fffffff]*n for _ in range(n)]
    cnt[0][0] = 1
    while queue:
        x, y = queue.pop(0)
        chk = [-1]*4
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if cnt[ny][nx] - cnt[y][x] <= 0:
                    continue
                chk[i] = arr[ny][nx]
        for i in range(4):
            if chk[i] != -1:
                nx = x + dx[i]
                ny = y + dy[i]
                count = arr[ny][nx] + cnt[y][x]
                if count <= cnt[ny][nx]:
                    cnt[ny][nx] = count
                    queue.append((nx, ny))
    return cnt[n-1][n-1] - 1


tcs = int(input())
for tc in range(tcs):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input())))
    print('#{} {}'.format(tc+1, prim(n)))
