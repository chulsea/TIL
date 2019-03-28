dp = [0]*41
dp[1] = dp[2] = 1
def fibo(n):
    if n == 1 or n == 2:
        return dp[n]
    if dp[n]:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]
n = int(input())
print(fibo(n))
