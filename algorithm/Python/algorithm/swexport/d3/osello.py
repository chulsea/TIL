import sys

sys.stdin = open('inputs/osello_input.txt')

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
def __board_init(n):
    base = [(n//2, n//2), (n//2-1, n//2-1),
            (n//2-1, n//2), (n//2, n//2-1)]
    board = [[0] * n for _ in range(n)]
    for idx, (y, x) in enumerate(base):
        if idx < 2:
            board[y][x] = 2
        else:
            board[y][x] = 1
    return board


def __cal_stone(board):
    w = b = 0
    n = len(board)
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                w += 1
            elif board[y][x] == 2:
                b += 1
    return w, b


def __is_out(n, x, y):
    return 0 <= y < n and 0 <= x < n


def solution(n, plays):
    board = __board_init(n)
    for x, y, s in plays:
        board[y-1][x-1] = s
        k = 2 if s == 1 else 1
        for i in range(8):
            ny = y + dy[i] - 1
            nx = x + dx[i] - 1
            stack = []
            while __is_out(n, nx, ny) and board[ny][nx] == k:
                stack.append((ny, nx))
                ny += dy[i]
                nx += dx[i]
            if __is_out(n, nx, ny) and board[ny][nx] == s:
                while stack:
                    ty, tx = stack.pop()
                    board[ty][tx] = s
    return __cal_stone(board)


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, m = map(int, input().split())
        plays = []
        for _ in range(m):
            plays.append(list(map(int, input().split())))
        print('#{}'.format(test_case+1), *solution(n, plays), sep=" ")


if __name__ == '__main__':
    main()
