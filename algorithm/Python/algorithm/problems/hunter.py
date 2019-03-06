dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


def __is_hunting(arr, y, x, i):
    n = len(arr)
    if 0 <= y < n and 0 <= x < n:
        if arr[y][x] == 2:
            return __is_hunting(arr, y+dy[i], x+dx[i], i)
        elif arr[y][x] == 1:
            return True
    return False


def solution(arr):
    n = len(arr)
    answer = 0
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 2:
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if __is_hunting(arr, ny, nx, i):
                        answer += 1
                        break
    return answer


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input())))
    print(solution(arr))


if __name__ == '__main__':
    main()
