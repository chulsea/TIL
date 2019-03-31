dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def __is_wall(n, x, y):
    return x < 0 or x >= n or y < 0 or y >= n


def __dfs(arr, visited, x, y, num):
    visited[y][x] = num
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not __is_wall(len(arr), nx, ny) and visited[ny][nx] == 0 and arr[ny][nx]:
            __dfs(arr, visited, nx, ny, num)


def solution(n, arr):
    visited = [[0] * n for _ in range(n)]
    num = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] and visited[i][j] == 0:
                num += 1
                __dfs(arr, visited, j, i, num)
    ans = []
    for i in range(1, num+1):
        cnt = 0
        for y in range(n):
            for x in range(n):
                if visited[y][x] == i:
                    cnt += 1
        ans.append(cnt)
    ans.sort()
    return num, ans


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input())))
    num, ans = solution(n, arr)
    print(num, *ans, sep='\n')


if __name__ == '__main__':
    main()
