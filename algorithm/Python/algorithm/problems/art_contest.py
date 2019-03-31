dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def __is_move(n, x, y):
    return 0 <= x < n and 0 <= y < n


def __bfs(n, arr, visited, sx, sy, k):
    global flag
    queue = [(sx, sy)]
    visited[sy][sx] = k
    check = set()
    check.add(0)
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if __is_move(n, nx, ny):
                if visited[ny][nx] not in check and ((arr[y][x] == 'G' and arr[ny][nx] == 'R') or
                        (arr[y][x] == 'R' and arr[ny][nx] == 'G')):
                    flag += 1
                    check.add(visited[ny][nx])
                if visited[ny][nx] == 0 and arr[ny][nx] == arr[y][x]:
                    visited[ny][nx] = k
                    queue.append((nx, ny))


def solution(n, arr):
    global flag
    visited = [[0] * n for _ in range(n)]
    area = blind_area = 0
    k = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                flag = 0
                __bfs(n, arr, visited, j, i, k)
                area += 1
                blind_area += 1 - flag
                k += 1
    return area, blind_area


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(input()))
    print(*solution(n, arr))


if __name__ == '__main__':
    main()
