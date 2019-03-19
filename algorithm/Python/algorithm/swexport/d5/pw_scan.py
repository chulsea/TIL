import sys

sys.stdin = open('inputs/pw_scan_input.txt')


def __make_bin(num):
    result = ''
    while num > 0:
        result = ('0' if num & 1 == 0 else '1') + result
        num >>= 1
    l = len(result)
    for _ in range(l, 4):
        result = '0' + result
    return result


def __hex_to_bin(hex_num):
    over_ten = {
        'A': 10, 'B': 11, 'C': 12,
        'D': 13, 'E': 14, 'F': 15
    }
    result = ''
    for h in hex_num:
        if h not in over_ten:
            num = int(h)
        else:
            num = over_ten[h]
        result += __make_bin(num)
    return result


def __decode(pw):
    decoder = [
        '3211', '2221', '2122', '1411', '1132',
        '1231', '1114', '1312', '1213', '3112'
    ]
    int_pw = list(map(int, pw))
    min_pw = min(int_pw)
    int_pw = list(map(lambda x: str(x // min_pw), int_pw))
    decoded = "".join(int_pw)
    for i in range(10):
        if decoded == decoder[i]:
            return i


def solution(code, n, m):
    answer = 0
    bin = []
    for i in range(n):
        bin.append(__hex_to_bin(code[i]))
    for y in range(1, n):
        pw = ''
        even = odd = cnt = 0
        first = True
        pw_cnt = 8
        for x in range(m*4-1, -1, -1):
            if bin[y-1][x] == '0' and bin[y][x] == '1':
                if first:
                    check = bin[y][x]
                    cnt = 1
                    first = False
                elif check != bin[y][x]:
                    check = bin[y][x]
                    pw = str(cnt) + pw
                    cnt = 1
                else:
                    cnt += 1
                if len(pw) == 4:
                    temp = __decode(pw)
                    if pw_cnt & 1:
                        even += temp
                    else:
                        odd += temp
                    pw_cnt -= 1
            if pw_cnt == 0:
                if (odd * 3 + even) % 10 == 0:
                    answer += odd + even
                break
    return answer

def main():
    tcs = int(input())
    for tc in range(tcs):
        n, m = map(int, input().split())
        code = []
        for _ in range(n):
            code.append(list(input()))
        print('#{} {}'.format(tc+1, solution(code, n, m)))


if __name__ == '__main__':
    main()
