dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(n, items, moves):
    board = [[0]*n for _ in range(n)]
    for r, c in items:
        board[r-1][c-1] = 2
    cnt, y, x = 0, 0, 0
    i = m = 0
    ty, tx, tm = 0, -1, 0
    move_stack = []
    board[0][0] = 1
    while True:
        cnt += 1 # 초계산
        ny = y + dy[m] # 다음 이동 공간
        nx = x + dx[m]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[ny][nx] == 1: # 게임이 끝나는 조건
            return cnt

        # 만약 과일을 먹는다면 몸집 그대로
        # 안먹는다면 꼬리 1 자르기
        tflag = False
        if board[ny][nx] != 2: # 꼬리 찾기
            ty += dy[tm]
            tx += dx[tm]
        else:
            tflag = True
        board[ny][nx] = 1 # 게임이 끝나지 않는다면 다음 공간에 이동
        if not tflag:
            board[ty][tx] = 0
            if move_stack and ty == move_stack[0][0] and tx == move_stack[0][1]:
                tm = move_stack[0][2]
                move_stack.pop(0)
            # if tx+dx[tm] < 0 or tx+dx[tm] >= n or ty+dy[tm] < 0 or ty+dy[tm] >= n or board[ty+dy[tm]][tx+dx[tm]] == 0:
        if i < len(moves) and cnt == moves[i][0]:
            if moves[i][1] == "D":
                m = (m+1) % 4
            else:
                m = 3 if m-1 < 0 else m-1
            i += 1
            move_stack.append((ny, nx, m))
        x, y = nx, ny


def main():
    n = int(input())
    k = int(input())
    items = []
    for _ in range(k):
        items.append(tuple(map(int, input().split())))
    l = int(input())
    moves = []
    for _ in range(l):
        x, c = input().split()
        moves.append((int(x), c))
    print(solution(n, items, moves))


if __name__ == '__main__':
    main()
