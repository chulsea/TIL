import sys

sys.stdin = open('inputs/oven_input.txt')


def solution(arr, n, m):
    oven = [[arr[i], i+1] for i in range(n)]
    i = n
    while oven:
        k = 0
        while k < len(oven):
            oven[k][0] //= 2
            if oven[k][0]:
                k += 1
            else:
                pop = oven.pop(k)
                if len(oven) < n and i < m:
                    oven.insert(k, [arr[i], i+1])
                    i += 1
                    k += 1
    return pop[1]


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, m = map(int, input().split()) # n은 화덕의 크기, m은 피자 양
        arr = list(map(int, input().split()))
        print(f'#{test_case + 1} {solution(arr, n, m)}')


if __name__ == '__main__':
    main()
