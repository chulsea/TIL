# 명령의 가지수는 5가지, 이를 모두 적용하여 다음 단계로 적용한다.
# 같은 자리를 한번더 진행할 수 있다. 이는 상황별로(방향별로) 모두 체크해야한다.
# 각 방향에 대해 왼쪽 / 오른쪽으로 이동할 경우에 대한 정보 테이블 만들기
def count_dir_command(d, i):
    if d & 1:
        if i - d == 1:
            return 2
    else:
        if d - i == 1:
            return 2
    return 1

def bfs(n, sx, sy, sd, fx, fy, fd):
    queue = (sx, sy, sd)
    cnt[sy][sx] = 0
    while queue:
        x, y, d = queue.pop(0)
        for i in range(5):
            dir_com = count_dir_command(d, i)
            for j in range(1, 4):
                nx = x + dx[i]*j
                ny = y + dy[i]*j
                if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] == 0:
                    dir_com + 1

                    queue.append((nx, ny, i))





dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
start = list(map(int, input().split()))
arrive = list(map(int, input().split()))
cnt = [[1000]*m for _ in range(n)]