dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def __cal_height(hill, y, x):
    n = len(hill)
    if x == 0 or x == n - 1 or y == 0 or y == n - 1:
        hill[y][x] = 1
        return
    min_around = float('inf')
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if hill[ny][nx] == 0:
                hill[y][x] = 1
                break
            else:
                min_around = min(min_around, hill[ny][nx])
        hill[y][x] = min_around + 1


def solution(hill):
    n = len(hill)
    max_height = 0
    for y in range(n):
        for x in range(n):
            if hill[y][x]:
                __cal_height(hill, y, x)
            max_height = max(hill[y][x], max_height)
    return max_height


def main():
    n = int(input())
    hill = []
    for _ in range(n):
        hill.append(list(map(int, input())))
    print(solution(hill))

if __name__ == '__main__':
    main()
