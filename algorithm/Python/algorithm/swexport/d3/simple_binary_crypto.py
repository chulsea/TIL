import sys

sys.stdin = open('inputs/simple_binary_crypto_input.txt')

def soltuon(arr, col, row):
    answer = 0
    check = [
        '0001101', '0011001', '0010011', '0111101', '0100011',
        '0110001', '0101111', '0111011', '0110111', '0001011'
    ]
    code = ""
    for y in range(col):
        for x in range(row):
            if arr[y][x] == '1':
                code = arr[y][x:x+56]
                code_col, code_row = y, x
                break
    parity = even = odd = 0
    for i in range(0, 56, 7):
        temp = code[i:i+7]
        for j in range(len(check)):
            if temp == check[j]:
                if i == 49:
                    parity = j
                elif i % 2:
                    even += j
                else:
                    odd += j
                break
    if (odd*3 + even + parity) % 10 == 0:
        answer = odd + even + parity
    return answer



def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        col, row = map(int, input().split())
        arr = []
        for _ in range(col):
            arr.append(input())
        print('#{} {}'.format(test_case+1, soltuon(arr, col, row)))

if __name__ == '__main__':
    main()