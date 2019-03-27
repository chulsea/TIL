dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def __is_wall(x, y, i, j):
    return i < 0 or i >= x or j < 0 or j >= y

def solution(x, y, arr, start):
    queue = [start]
    arr[start[1]][start[0]] = 3
    while queue:
        i, j = queue.pop(0)
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if not __is_wall(x, y, nx, ny) and arr[ny][nx] == 1:
                arr[ny][nx] = arr[j][i] + 1
                queue.append((nx, ny))
    cnt = 0
    max_second = 0
    for i in range(y):
        for j in range(x):
            if arr[i][j] == 1:
                cnt += 1
            if max_second < arr[i][j]:
                max_second = arr[i][j]
    return max_second, cnt


def main():
    x, y = map(int, input().split())
    arr = []
    for _ in range(y):
        arr.append(list(map(int, input())))
    start = list(map(lambda k: int(k)-1, input().split()))
    print(*solution(x, y, arr, start), sep='\n')


if __name__ == '__main__':
    main()