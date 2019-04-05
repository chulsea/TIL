# 명령의 가지수는 5가지, 이를 모두 적용하여 다음 단계로 적용한다.
# 같은 자리를 한번더 진행할 수 있다. 이는 상황별로(방향별로) 모두 체크해야한다.
# 각 방향에 대해 왼쪽 / 오른쪽으로 이동할 경우에 대한 정보 테이블 만들기
def bfs(n, m):
    sy, sx, sd = start
    fy, fx, fd = arrive
    queue = [(sx-1, sy-1, sd, 0)]
    visited[sd][sy-1][sx-1] = 1
    while queue:
        x, y, d, c = queue.pop(0)
        if x == fx-1 and y == fy-1 and d == fd:
            return c
        for i in range(1, 4):
            nx = x + dx[d]*i
            ny = y + dy[d]*i
            if 0 <= nx < m and 0 <= ny < n:
                if arr[ny][nx]:
                    break
                if visited[d][ny][nx]:
                    continue
                visited[d][ny][nx] = 1
                queue.append((nx, ny, d, c+1))
        for i in range(2):
            nd = dir_table[d][i]
            if not visited[nd][y][x]:
                visited[nd][y][x] = 1
                queue.append((x, y, nd, c+1))


dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
start = list(map(int, input().split()))
arrive = list(map(int, input().split()))
visited = [[[0]*m for _ in range(n)] for _ in range(5)]
dir_table = [(), (4, 3), (3, 4), (2, 1), (1, 2)]
print(bfs(n, m))