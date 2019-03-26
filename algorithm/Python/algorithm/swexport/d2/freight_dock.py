import sys

sys.stdin = open('inputs/freight_dock_input.txt')

def solution(schedules):
    schedules.sort(key=lambda x: x[1])
    ans = 1
    last = schedules[0][1]
    for i in range(1, len(schedules)):
        if schedules[i][0] >= last:
            last = schedules[i][1]
            ans += 1
    return ans


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n = int(input())
        schedules = []
        for _ in range(n):
            schedules.append(list(map(int, input().split())))
        print('#{} {}'.format(test_case+1, solution(schedules)))


if __name__ == '__main__':
    main()