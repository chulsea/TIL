import sys

sys.stdin = open('backtrack.txt')


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
flag = 0


def backtrack(M, x, y):
    global flag
    M[y][x] = 9
    if flag == 1:
        return
    if x == 7 and y == 7:
        flag = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < len(M)) and (0 <= ny < len(M)):
            if M[ny][nx] == 0:
                backtrack(M, nx, ny)


def main():
    M = []
    for _ in range(8):
        M.append(list(map(int, input().split())))
    backtrack(M, 0, 0)
    print(flag)


if __name__ == '__main__':
    main()
