import sys

sys.stdin = open('inputs/hiking_input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def __is_wall(n, x, y):
    return x < 0 or x >= n or y < 0 or y >= n


def __dfs(arr, n, x, y, k, s):
    if __is_wall(n, x, y):
        return 0
    max_l = 0
    for i in range(4):
        l = 0
        ny = y + dy[i]
        nx = x + dx[i]
        if not __is_wall(n, nx, ny):
            if k != 0 and s == 0 and arr[ny][nx] < arr[y][x] - k:
                l += __dfs(arr, n, nx, ny, 0, 0) + 1
            elif arr[ny][nx] < arr[y][x]:
                l += __dfs(arr, n, nx, ny, k, s) + 1
            elif k != 0 and s != 0 and arr[ny][nx] - k < arr[y][x]:
                l += __dfs(arr, n, nx, ny, k, 0) + 1
        max_l = max(max_l, l)
    return max_l


def solution(arr, k):
    answer = max_height = 0
    n = len(arr)
    for y in range(n):
        for x in range(n):
            if max_height < arr[y][x]:
                max_height = arr[y][x]
    for y in range(n):
        for x in range(n):
            if arr[y][x] == max_height:
                answer = max(answer, __dfs(arr, n, x, y, k, 1))
    return answer


def main():
    tcs = int(input())
    for tc in range(tcs):
        s = 1
        n, k = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(n)]
        print('#{tc} {ans}'.format(tc=tc+1, ans=solution(arr, k)))


if __name__ == '__main__':
    main()
