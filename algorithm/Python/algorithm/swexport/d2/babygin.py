import sys

sys.stdin = open('inputs/babygin_input.txt')
def __check_card(cards):
    counts = [0]*10
    for c in cards:
        counts[c] += 1
    check = 0
    for i in range(len(counts)):
        if counts[i] == 3:
            return True
        if counts[i]:
            if check:
                check += 1
            else:
                check = 1
        else:
            check = 0
        if check == 3:
            return True
    return False


def solution(cards):
    me, op = [], []
    for i in range(0, len(cards)//2):
        me.append(cards[i*2])
        op.append(cards[i*2+1])
        if __check_card(me):
            return 1
        if __check_card(op):
            return 2
    return 0


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        cards = list(map(int, input().split()))
        print('#{} {}'.format(test_case+1, solution(cards)))


if __name__ == '__main__':
    main()