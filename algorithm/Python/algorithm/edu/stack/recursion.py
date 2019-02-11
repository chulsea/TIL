import time


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


dp = [0, 1]


def fibonacci(n):
    if n >= 2 and len(dp) <= n:
        dp.append(fibonacci(n - 1) + fibonacci(n - 2))
    return dp[n]


n = 5
print(factorial(5))
start = time.time()
print(fibonacci(n), time.time() - start, sep="\n")
