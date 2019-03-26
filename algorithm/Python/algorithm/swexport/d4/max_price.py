import sys, datetime
sys.stdin = open('inputs/max_price_input.txt')
def solution(boards, n, k, cnt):
    global ans
    if k == len(boards):
         k = 0
    if cnt == 0:
        result = int(''.join(list(map(str, boards))))
        if ans < result:
            ans = result
    else:
        for i in range(n):
            if i == k:
                continue
            boards[i], boards[k] = boards[k], boards[i]
            if k > i and boards[k-1] > boards[i]:
                boards[i], boards[k] = boards[k], boards[i]
                break
            solution(boards, n, k+1, cnt-1)
            boards[i], boards[k] = boards[k], boards[i]


def main():
    global ans
    tcs = int(input())
    start = datetime.datetime.now()
    for tc in range(tcs):
        boards, cnt = input().split()
        cnt = int(cnt)
        ans = 0
        for i in range(len(boards)):
            solution(list(map(int, boards)), len(boards), i, int(cnt))
        print('#{} {}'.format(tc+1, ans))
    print(datetime.datetime.now() - start)


if __name__ == '__main__':
    main()
