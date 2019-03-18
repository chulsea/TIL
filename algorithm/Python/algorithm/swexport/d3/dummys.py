tcs = int(input())
for tc in range(tcs):
    ans = 0
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    base = sum(nums) // len(nums)
    for num in nums:
        if base < num:
           ans += num - base
    print(f'#{tc+1} {ans}')
