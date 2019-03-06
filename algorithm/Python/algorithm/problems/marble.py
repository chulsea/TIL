dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]


def __move(boards, moves, x, y):
    r, c = len(boards), len(boards[0])
    boards[y][x] = 9
    answer = 1
    m = 0
    while True:
        ny = y + dy[moves[m]]
        nx = x + dx[moves[m]]
        if ny < 0 or ny >= r or nx < 0 or nx >= c or boards[ny][nx] == 1:
            m += 1
            if m >= len(moves):
                return answer
        elif boards[ny][nx] == 0:
            answer += 1
            boards[ny][nx] = 9
            x, y = nx, ny
        else:
            x, y = nx, ny


def solution(boards, moves):
    n = len(boards)
    for y in range(n):
        for x in range(len(boards[y])):
            if boards[y][x] == 2:
                sy, sx = y, x
                break
    return __move(boards, moves, sx, sy)


def main():
    col, row = map(int, input().split())
    boards = []
    for _ in range(row):
        boards.append(list(map(int, input())))
    input()
    moves = list(map(int, input().split()))
    print(solution(boards, moves))


if __name__ == '__main__':
    main()
