dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def __is_wall(m, n, x, y):
    return x < 0 or x >= m or y < 0 or y >= n


def solution(arr, m, n):
    ans = 0
    queue = []
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                queue.append((x, y))
    k = len(queue)
    while queue:
        x, y = queue.pop(0)
        k -= 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not __is_wall(m, n, nx, ny) and arr[ny][nx] == 0:
                arr[ny][nx] = 1
                queue.append((nx, ny))
        if k == 0:
            k = len(queue)
            ans += 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return -1
    return ans - 1


def main():
    m, n = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(solution(arr, m, n))


if __name__ == '__main__':
    main()

"""testcase
6 4
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
=> 4
"""