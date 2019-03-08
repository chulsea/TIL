def solution(nums):
    n = len(nums)
    if n == 1:
        return 1
    is_bigger = True
    answer = cnt = 1
    same_cnt = 1
    temp = nums[0]
    for i in range(1, n):
        if is_bigger:
            if temp <= nums[i]:
                if temp == nums[i]:
                    same_cnt += 1
                else:
                    same_cnt = 1
                cnt += 1
            else:
                answer = max(cnt, answer)
                cnt = 1 + same_cnt
                same_cnt = 1
                is_bigger = False
        else:
            if temp >= nums[i]:
                if temp == nums[i]:
                    same_cnt += 1
                else:
                    same_cnt = 1
                cnt += 1
            else:
                answer = max(cnt, answer)
                cnt = 1 + same_cnt
                same_cnt = 1
                is_bigger = True
        temp = nums[i]
        answer = max(cnt, answer)
    return answer


def main():
    input()
    nums = list(map(int, input().split()))
    print(solution(nums))


if __name__ == '__main__':
    main()
