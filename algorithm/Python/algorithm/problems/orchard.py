def __fruit_cnt(orchard, sx, fx, sy, fy):
    cnt = 0
    for i in range(sy, fy):
        for j in range(sx, fx):
            if orchard[i][j]:
                cnt += 1
    return cnt


def __is_equal(orchard, x, y):
    answer = -1
    n = len(orchard)
    loc = [(0, x, 0, y), (x, n, 0, y), (0, x, y, n), (x, n, y, n)]
    for sx, fx, sy, fy in loc:
        cnt = __fruit_cnt(orchard, sx, fx, sy, fy)
        if answer == -1:
            answer = cnt
        else:
            if answer != cnt:
                return False
    return True


def solution(orchard):
    answer = 0
    n = len(orchard)
    for y in range(1, n):
        for x in range(1, n):
            if __is_equal(orchard, x, y):
                answer += 1
    return -1 if answer == 0 else answer


def main():
    n = int(input())
    orchard = []
    for _ in range(n):
        orchard.append(list(map(int, input())))
    print(solution(orchard))


if __name__ == '__main__':
    main()