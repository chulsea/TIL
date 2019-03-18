tcs = int(input())
for tc in range(tcs):
    nums = list(map(int, input()))
    cnt = 0
    for num in nums:
        if (cnt % 2 and num == 0) or (cnt % 2 == 0 and num == 1):
            cnt += 1
    print(f'#{tc+1} {cnt}')
