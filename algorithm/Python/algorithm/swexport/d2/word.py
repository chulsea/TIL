def solution(n, k, arr):
    answer = 0
    for y in range(n):
        for x in range(n):
            if arr[y][x]:
                c_cnt = r_cnt = 0
                for i in range(x, n):
                    if arr[y][i]:
                        c_cnt += 1
                for j in range(y, n):
                    if arr[j][x]:
                        r_cnt += 1
                if c_cnt == k:
                    answer += 1
                if r_cnt == k:
                    answer += 1
    return answer


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, k = map(int, input().split())
        arr = []
        for _ in range(n):
            arr.append(list(map(int, input().split())))
        print('#{} {}'.format(test_case+1, solution(n, k, arr)))


if __name__ == '__main__':
    main()