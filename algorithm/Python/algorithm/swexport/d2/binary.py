def __make_bin(num):
    result = ''
    while num > 0:
        result = ('0' if num & 1 == 0 else '1') + result
        num >>= 1
    l = len(result)
    for _ in range(l, 4):
        result = '0' + result
    return result


def solution(hex):
    over_ten = {
        'A': 10, 'B': 11, 'C': 12,
        'D': 13, 'E': 14, 'F': 15
        
    }
    ans = ''
    for h in hex:
        if h not in over_ten:
            num = int(h)
        else:
            num = over_ten[h]
        ans += __make_bin(num)
    return ans


tcs = int(input())
for tc in range(tcs):
    n, hex = input().split()
    print('#{} {}'.format(tc+1, solution(hex)))
