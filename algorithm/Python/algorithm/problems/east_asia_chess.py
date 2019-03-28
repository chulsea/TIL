dx = [[-1, 1, 0], [-1, 1, 0], [-2, -2, -1], [2, 2, 1]]
dy = [[-2, -2, -1], [2, 2, 1], [-1, 1, 0], [-1, 1, 0]]
n, m = map(int, input().split())
board = [[0]*m for _ in range(n)]
cord = list(map(lambda x: int(x)-1, input().split()))
board[cord[2]][cord[3]] = -1
sy, sx = cord[0], cord[1]
def __is_move(x, y):
    return board[y][x] != -1
def __is_wall(n, m, x, y):
    return x < 0 or x >= m or y < 0 or y >= n
ans = 0
def bfs(n, m, x, y):
    queue = [(x, y, 1)]
    while queue:
        sx, sy, move = queue.pop(0)
        for i in range(4):
            for j in range(2):
                nx = sx + dx[i][j]
                ny = sy + dy[i][j]
                if not __is_wall(n, m, nx, ny) and \
                        __is_move(sx + dx[i][2], sy + dy[i][2]) and (board[ny][nx] == 0 or board[ny][nx] == -1):
                    if board[ny][nx] == -1:
                        return move
                    board[ny][nx] = move
                    queue.append((nx, ny, move+1))

print(bfs(n, m, sx, sy))
