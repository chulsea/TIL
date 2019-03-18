

tcs = int(input())
for tc in range(tcs):
    n, l = map(int, input().split())
    gredients = []
    for _ in range(n):
        gredients.append(list(map(int, input().split())))
    gredients.sort(key=lambda x: x[1], reverse=True)
    print(f'#{tc+1} {solution(n, l)}')
