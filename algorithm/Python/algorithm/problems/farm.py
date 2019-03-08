# 가로 세로로 가장 긴 길이를 찾기
def __find_short(sides, idx, m):
    if sides[(idx - 1) % 6][1] != m:
        result = sides[(idx - 1) % 6][1]
    elif sides[(idx + 1) % 6][1] != m:
        result = sides[(idx + 1) % 6][1]
    return result


def solution(n, sides):
    max_w = max_h = 0
    for i in range(len(sides)):
        d, l = sides[i]
        if d < 3:
            if max_w < l:
                max_w, w_idx = l, i
        else:
            if max_h < l:
                max_h, h_idx = l, i
    b_h = __find_short(sides, w_idx, max_h)
    b_w = __find_short(sides, h_idx, max_w)
    return (max_w * b_h + b_w * (max_h - b_h)) * n


def main():
    n = int(input())
    sides = []
    for _ in range(6):
        sides.append(list(map(int, input().split())))
    print(solution(n, sides))


if __name__ == '__main__':
    main()
