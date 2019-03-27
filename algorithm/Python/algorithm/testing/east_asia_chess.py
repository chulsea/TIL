dx = [-2, -3, -3, -2, 2, 3, 3, 2]
dy = [-3, -2, 2, 3, 3, 2, -2, -3]
def __is_wall(x, y, nx, ny):
    return nx < 0 or nx >= x or ny < 0 or ny >= y


def dfs(board, x, y, king, depth):
    global min_dis
    board[y][x] = 1
    if king[0] == y and king[1] == x:
        min_dis = min(depth, min_dis)
        return
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if not __is_wall(8, 9, nx, ny) and board[ny][nx] == 0:
            dfs(board, nx, ny, king, depth+1)
            board[y][x] = 0


def solution(sang, king):
    board = [[0] * 8 for _ in range(9)]
    dfs(board, sang[1], sang[0], king, 0)


def main():
    global min_dis
    min_dis = 0x7fffffff
    sang = tuple(map(int, input().split()))
    king = tuple(map(int, input().split()))
    solution(sang, king)
    print(min_dis)


if __name__ == '__main__':
    main()
