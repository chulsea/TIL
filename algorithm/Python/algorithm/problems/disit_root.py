
def digit_root(num):
    if num < 10:
        return num
    else:
        result = 0
        while num:
            result += num % 10
            num //= 10
        return digit_root(result)


def solution(arr):
    answer = -float('inf'), float('inf')
    for num in arr:
        temp = digit_root(num)
        if answer[0] < temp or \
            (answer[0] == temp and answer[1] > num):
            answer = temp, num
    return answer[1]


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    print(solution(arr))


if __name__ == '__main__':
    main()
