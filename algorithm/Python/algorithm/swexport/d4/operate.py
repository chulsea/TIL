delta = [1, -1, -10]
def bfs(dp, m, n):
    rear = 0
    queue = [n]
    dp[n] = 1
    while rear < len(queue):
        cur = queue[rear]
        rear += 1
        if cur == m:
            return dp[cur] - 1
        for i in range(4):
            if i == 3:
                next = cur*2
            else:
                next = cur + delta[i]
            if 0 <= next < 1000001 and not dp[next]:
                if dp[next]:
                    continue
                dp[next] += dp[cur] + 1
                queue.append(next)


tcs = int(input())
for tc in range(tcs):
    n, m = map(int , input().split())
    dp = [0]*1000001
    print('#{} {}'.format(tc+1, bfs(dp, m, n)))