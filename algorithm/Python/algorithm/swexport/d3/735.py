def __conb(nums, temp, n, r):
    global result
    if r == 0:
        num_sum = sum(temp)
        if num_sum not in result:
            result.append(num_sum)
    elif n < r:
        return
    else:
        temp[r-1] = nums[n-1]
        __conb(nums, temp, n-1, r-1)
        __conb(nums, temp, n-1, r)


def solution(nums):
    temp = [0]*3
    __conb(nums, temp, 7, 3)


def main():
    global result
    tcs = int(input())
    for tc in range(tcs):
        result = []
        nums = list(map(int, input().split()))
        solution(nums)
        result.sort()
        print(f'#{tc+1} {result[-5]}')


if __name__ == '__main__':
    main()
