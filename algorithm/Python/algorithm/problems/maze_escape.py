dx = [0, -1, 0, 1]  # 하 좌 상 우
dy = [1, 0, -1, 0]


def solution(boards, moves):
    answer = 0
    n = len(boards)
    x = y = k = 0
    m = moves[k]
    while answer <= n**2:
        boards[y][x] = 2
        nx = x + dx[m]
        ny = y + dy[m]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or boards[ny][nx] == 1:
            k += 1
            m = moves[k % len(moves)]
        elif boards[ny][nx] == 2:
            return answer
        else:
            answer += 1
            x += dx[m]
            y += dy[m]


def main():
    n = int(input())
    boards = []
    for _ in range(n):
        boards.append(list(map(int, input())))
    move_list = list(map(lambda x: int(x)-1, input().split()))
    print(solution(boards, move_list))


if __name__ == '__main__':
    main()
