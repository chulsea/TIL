import sys

sys.stdin = open('inputs/sum_input.txt')

def find_max(*args):
    max_num = args[0]
    for i in range(1, len(args)):
        target = args[i]
        if max_num < target:
            max_num = target
    return max_num

def solution(input_list):
    max_sum = -float('inf')
    n = len(input_list)
    for i in range(n):
        a = b = v = h = 0
        a += input_list[i][i]
        b += input_list[n - i - 1][i]
        for j in range(n):
            v += input_list[j][i]
            h += input_list[i][j]
        max_sum = find_max(max_sum, v, h)
    return find_max(max_sum, a, b)


def main():
    for test_case in range(10):
        input_list = []
        n = int(input())
        for i in range(100):
            input_list.append(list(map(int, input().split())))
        print(f"#{test_case + 1} {solution(input_list)}")


if __name__ == '__main__':
    main()
