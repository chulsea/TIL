import math


def solution(village):
    n = len(village)
    dm = 0
    for y in range(n):
        for x in range(n):
            if village[y][x] == 2:
                sy, sx = y, x
                break
    for y in range(n):
        for x in range(n):
            if village[y][x] == 1:
                d = math.ceil((abs(y - sy)**2 + abs(x - sx)**2) ** 0.5)
                dm = max(dm, d)
    return dm


def main():
    n = int(input())
    village = []
    for _ in range(n):
        village.append(list(map(int, input())))
    print(solution(village))


if __name__ == '__main__':
    main()