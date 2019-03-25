import sys, datetime

sys.stdin = open('inputs/optimal_path_input.txt')


def __cal_distance(s, f):
    return abs(s[0] - f[0]) + abs(s[1] - f[1])


def solution(n, k, prev, finish, path, sum):
    global answer
    if sum > answer:
        return
    if k == 0:
        answer = min(answer, sum + __cal_distance(prev, finish))
    else:
        for i in range(n):
            path[n-1], path[i] = path[i], path[n-1]
            solution(n - 1, k - 1, path[n - 1], finish,
                     path, sum + __cal_distance(prev, path[n - 1]))
            path[n-1], path[i] = path[i], path[n-1]


def main():
    global answer, dp
    test_cases = int(input())
    start = datetime.datetime.now()
    for test_case in range(test_cases):
        n = int(input())
        temp = list(map(int, input().split()))
        path = []
        for i in range(len(temp)//2):
            if i == 0:
                com = temp[i*2], temp[i*2+1]
            elif i == 1:
                home = temp[i*2], temp[i*2+1]
            else:
                path.append((temp[i*2], temp[i*2+1]))
        answer = float('inf')
        solution(n, n, com, home, path, 0)
        print('#{} {}'.format(test_case+1, answer))
    print(datetime.datetime.now() - start)


if __name__ == '__main__':
    main()
