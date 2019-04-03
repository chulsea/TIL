mashrums = []
for _ in range(10):
    mashrums.append(int(input()))
for i in range(1, 10):
    mashrums[i] += mashrums[i-1]
min_diff = 0x7fffffff
idx = 0
for i in range(10):
    diff = abs(100 - mashrums[i])
    if diff <= min_diff:
        min_diff = diff
        idx = i
    else:
        break
print(mashrums[idx])