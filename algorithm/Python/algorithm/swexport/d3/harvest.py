def __sum(*args):
    result = 0
    for val in args:
        result += val
    return result


def solution(farm):
    n = len(farm)
    answer = 0
    answer += __sum(*farm[n//2])
    for i in range(1, n // 2 + 1):
        j = n // 2 - 1
        answer += __sum(*farm[n//2-i][i:n-i])
        answer += __sum(*farm[n//2+i][i:n-i])
        j -= 1
    return answer


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n = int(input())
        farm = []
        for _ in range(n):
            farm.append(list(map(int, input())))
        print('#{} {}'.format(test_case+1, solution(farm)))


if __name__ == '__main__':
    main()
