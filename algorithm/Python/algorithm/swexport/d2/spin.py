import sys

sys.stdin = open('inputs/spin_input.txt')


def solution(arr, m):
    n = len(arr)
    return arr[m % n]


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        print(f'#{test_case + 1} {solution(arr, m)}')


if __name__ == '__main__':
    main()
