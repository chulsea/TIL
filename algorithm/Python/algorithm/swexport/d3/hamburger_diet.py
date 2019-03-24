def solution(gredients, n, l):
    answer = 0
    for i in range(n):
        temp, total_cal = gredients[i]
        for j in range(n):
            if i == j:
                continue
            g = gredients[j]
            if total_cal + g[1] <= l:
                total_cal += g[1]
                temp += g[0]
        if total_cal <= l:
            answer = max(answer, temp)
    return answer
"""
예외상황
1
5 500
200 400
100 150
300 350
150 500
200 200
"""

tcs = int(input())
for tc in range(tcs):
    n, l = map(int, input().split())
    gredients = []
    for _ in range(n):
        gredients.append(list(map(int, input().split())))
    gredients.sort(key=lambda g: (g[0]/g[1], g[1]), reverse=True)
    print(f'#{tc+1} {solution(gredients, n, l)}')
