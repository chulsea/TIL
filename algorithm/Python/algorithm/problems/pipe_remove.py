dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def __is_move(n, x, y):
    return 0 <= x < n and 0 <= y < n

def __pipe_move(i, pipe):
    k = i - 1 if i & 1 else i+1
    return k in pipe

def __bfs(n, arr, start):
    pipe = {
        '0': (), '1': (2, 3), '2': (0, 1), '3': (1, 3), '4': (1, 2),
        '5': (0, 2), '6': (0, 3), '7': (0, 1, 3), '8': (1, 2, 3),
        '9': (0, 1, 2), 'A': (0, 2, 3), 'B': (0, 1, 2, 3)
    }
    sx, sy = start
    queue = [(sx, sy)]
    visited = [[0]*n for _ in range(n)]
    visited[sy][sx] = 1
    cnt = 1
    while queue:
        x, y = queue.pop(0)
        path = pipe[arr[y][x]]
        for i in path:
            nx = x + dx[i]
            ny = y + dy[i]
            if __is_move(n, nx, ny) and visited[ny][nx] == 0 and __pipe_move(i, pipe[arr[ny][nx]]):
                queue.append((nx, ny))
                visited[ny][nx] = 1
                cnt += 1
    return cnt


def solution(n, arr, start):
    total = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != '0':
                total += 1
    answer = __bfs(n, arr, start)
    return total - answer

def main():
    n = int(input())
    start = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(input()))
    print(solution(n, arr, start))


if __name__ == '__main__':
    main()
