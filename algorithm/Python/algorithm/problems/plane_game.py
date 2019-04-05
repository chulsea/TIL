dx = [-1, 0, 1]
def bfs(sx, sy):
    queue = [(sx, sy, 5)]
    points[sy][sx] = 0
    while queue:
        x, y, b = queue.pop(0)
        for i in range(3):
            nx = x + dx[i]
            ny = y - 1
            if 0 <= nx < 5 and 0 <= ny < 13:
                if arr[ny][nx] == '*':
                    point = 10
                elif arr[ny][nx] == 'X':
                    point = -7
                elif arr[ny][nx] == '0':
                    point = 0
                if points[ny][nx] < points[y][x] + point:
                    points[ny][nx] = points[y][x] + point
                    queue.append((nx, ny, 5))


tcs = int(input())
for tc in range(tcs):
    arr = []
    for _ in range(13):
        arr.append(list(input()))
    points = [[-255]*5 for i in range(13)]
    bfs(2, 12)
    max_point = -255
    for i in range(4):
        if max_point < points[0][i]:
            max_point = points[0][i]
    print(max_point)