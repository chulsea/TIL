import sys

sys.stdin = open('inputs/word_input.txt')


def solution(n, k, arr):
    answer = 0
    for y in range(n+1):
        r_cnt = 0
        c_cnt = 0
        for x in range(n+1):
            if arr[x][y]:
                r_cnt += 1
            else:
                if r_cnt == k:
                    answer += 1
                r_cnt = 0
            if arr[y][x]:
                c_cnt += 1
            else:
                if c_cnt == k:
                    answer += 1
                c_cnt = 0
    return answer

def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, k = map(int, input().split())
        arr = []
        for _ in range(n):
            arr.append(list(map(int, input().split())) + [0])
        arr += [[0 for _ in range(n+1)]]
        print('#{} {}'.format(test_case+1, solution(n, k, arr)))


if __name__ == '__main__':
    main()
