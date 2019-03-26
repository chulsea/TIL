import sys

sys.stdin = open('inputs/min_sum_input.txt')

dx = [1, 0]
dy = [0, 1]


def __is_wall(n, x, y):
    return x < 0 or x >= n or y < 0 or y >= n


def __dfs(arr, visited, n, x, y, sum):
    global ans
    if sum > ans:
        return
    if y == n-1 and x == n-1:
        ans = min(sum, ans)
    else:
        visited[y][x] = 1
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if not __is_wall(n, nx, ny) and not visited[ny][nx]:
                __dfs(arr, visited, n, nx, ny, sum + arr[ny][nx])
                visited[ny][nx] = 0

tcs = int(input())
for tc in range(tcs):
    n = int(input())
    ans = float('inf')
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    visited = [[0]*n for _ in range(n)]
    __dfs(arr, visited, n, 0, 0, arr[0][0])
    print('#{} {}'.format(tc+1, ans))