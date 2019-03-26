import sys

sys.stdin = open('inputs/container_input.txt')


def solution(goods, truck):
    goods.sort(reverse=True)
    truck.sort(reverse=True)
    ans = k = 0
    for i in range(len(truck)):
        t = truck[i]
        for j in range(k, len(goods)):
            if t >= goods[j]:
                ans += goods[j]
                k = j+1
                break
    return ans


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, m = map(int, input().split())
        goods = list(map(int, input().split()))
        truck = list(map(int, input().split()))
        print('#{} {}'.format(test_case+1, solution(goods, truck)))


if __name__ == '__main__':
    main()
