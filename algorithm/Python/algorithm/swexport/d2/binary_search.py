import sys

sys.stdin = open('inputs/binary_search_input.txt')


def solution(n):
    level = 0
    for i in range(11):
        check = 2**level
        if check > n:
            level -= 1
            break
        level += 1
    temp = 2**level
    if (temp + temp//2) <= n < check:
        root = temp
    else:
        root = temp//2 + n+1 - temp
    answer = 1 + 2*(n - 2**level)
    if n % 2 == 0:
        answer += 1
    else:
        answer -= 1
    return root, answer


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n = int(input())
        print("#{}".format(test_case+1), *solution(n))


if __name__ == '__main__':
    main()
