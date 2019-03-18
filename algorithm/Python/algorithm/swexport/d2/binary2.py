def solution(num):
    ans = ''
    base = 2
    while num > 0:
        mod = 1 / base
        if num >= mod:
            num -= mod
            ans += '1'
        else:
            ans += '0'
        base *= 2
        if len(ans) == 13:
            return 'overflow'
    return ans


tcs = int(input())
for tc in range(tcs):
    num = eval(input())

    print('#{} {}'.format(tc+1, solution(num)))
