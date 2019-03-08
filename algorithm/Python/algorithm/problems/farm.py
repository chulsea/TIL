def solution(n, sides):
    max_w = max_h = 0
    for i in range(len(sides)):
        d, l = sides[i]
        if d < 3:
            if max_w < l:
                max_w = l
                w_idx = i
        else:
            if max_h < l:
                max_h = l
                h_idx = i
    if sides[(w_idx - 1) % 6][1] != max_h:
        b_h = sides[(w_idx - 1) % 6][1]
    elif sides[(w_idx + 1) % 6][1] != max_h:
        b_h = sides[(w_idx + 1) % 6][1]
    if sides[(h_idx - 1) % 6][1] != max_w:
        b_w = sides[(h_idx - 1) % 6][1]
    elif sides[(h_idx + 1) % 6][1] != max_w:
        b_w = sides[(h_idx + 1) % 6][1]
    return (max_w * b_h + b_w * (max_h - b_h)) * n


def main():
    n = int(input())
    sides = []
    for _ in range(6):
        sides.append(list(map(int, input().split())))
    print(solution(n, sides))


if __name__ == '__main__':
    main()
