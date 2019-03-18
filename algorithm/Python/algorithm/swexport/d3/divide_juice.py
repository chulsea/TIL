test_cases = int(input())
for tc in range(test_cases):
    n = int(input())
    ans = f'1/{n} '*n
    print(f'#{tc+1} {ans}')
