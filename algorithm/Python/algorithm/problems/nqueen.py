dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
def __dfs(board, n, x, y):
    global cnt, ans
    board[y][x] = 1
    cnt -= 1
    if cnt == 0:
        ans += 1
        return
    j = x+1
    for i in range(y, n):
        if n - i < cnt:
            return
        while j < n:
            flag = True
            for k in range(8):
                nx = j + dx[k]
                ny = i + dy[k]
                while (0 <= nx < n and 0 <= ny < n) and flag:
                    if board[ny][nx]:
                        flag = False
                    nx += dx[k]
                    ny += dy[k]
                if not flag:
                    break
            if flag:
                __dfs(board, n, j, i)
                cnt += 1
                board[i][j] = 0
            j += 1
        j = 0


def solution(board, n):
    global cnt
    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:
                cnt = n
                __dfs(board, n, x, y)
                board[y][x] = 0


def main():
    global ans
    n = int(input())
    board = [[0]*n for _ in range(n)]
    ans = 0
    solution(board, n)
    print(ans)


if __name__ == '__main__':
    main()
