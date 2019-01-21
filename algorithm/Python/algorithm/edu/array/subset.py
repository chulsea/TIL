arr = [-7, -3, -2, 5, 8]
n = len(arr)
answer = 0
for i in range(1, 1 << n):
    sum = 0
    for j in range(1 + n):
        if i & (1 << j):
            sum += arr[j]
    if sum == 0:
        answer += 1
print(answer)
