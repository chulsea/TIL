import sys

sys.stdin = open('inputs/simple_binary_crypto_input.txt')


def soltuon(arr, col, row):
    check = [
        '0001101', '0011001', '0010011', '0111101', '0100011',
        '0110001', '0101111', '0111011', '0110111', '0001011'
    ]
    code = ""
    for y in range(col):
        for x in range(row-1, -1, -1):
            if arr[y][x] == '1':
                code = arr[y][x-55:x+1]
                break
    parity = even = odd = 0
    for i in range(8):
        temp = code[i*7:(i+1)*7]
        for j in range(len(check)):
            if temp == check[j]:
                if i == 7:
                    parity = j
                elif i & 1:
                    even += j
                else:
                    odd += j
    pw = odd * 3 + even + parity
    return odd + even + parity if pw % 10 == 0 else 0

test_cases = int(input())
for test_case in range(test_cases):
    col, row = map(int, input().split())
    arr = []
    for _ in range(col):
        arr.append(input())
    print('#{} {}'.format(test_case+1, soltuon(arr, col, row)))

