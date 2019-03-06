dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(lake_map):
    answer = 0
    n = len(lake_map)
    for i in range(1, n//2 + 1):
        for y in range(i, n-i):
            for x in range(i, n-i):
                depth = 0
                flag = True
                if lake_map[y][x] >= 1:
                    depth = 1
                    for k in range(i):
                        for l in range(4):
                            ny = y + dy[l]*(k+1)
                            nx = x + dx[l]*(k+1)
                            if not lake_map[ny][nx]:
                                flag = False
                                break
                        if flag:
                            depth += 1
                        else:
                            break
                lake_map[y][x] = depth

    for i in range(n):
        for j in range(n):
            answer += lake_map[i][j]
    return answer



def main():
    n = int(input())
    lake_map = []
    for _ in range(n):
        lake_map.append(list(map(int, input().split())))
    print(solution(lake_map))


if __name__ == '__main__':
    main()