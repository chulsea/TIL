def find_max(board):
    max_val = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            max_val = max(board[i][j], max_val);
    return max_val

def cnt(board, max_val):
    cnt = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == max_val:
                cnt += 1
    return cnt


tcs = int(input())
for tc in range(tcs):
    n, m = map(int, input().split())
    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().split())))
    board = [[0]*n for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for y, x, d, j in arr:
        nx, ny = x, y
        while 0 <= nx < n and 0 <= ny < n:
            board[ny][nx] += 1
            nx += dx[d]*j
            ny += dy[d]*j
    max_val = find_max(board)
    total = cnt(board, max_val)
    print('#{} {} {}'.format(tc+1, max_val, total))


