# bit = [0, 0, 0]
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)

arr = [3, 6, 7, 1]
n = len(arr)

for i in range(1 << n):
    for j in range(0, n + 1):
        if i & (1 << j):
            print(arr[j], end=', ')
    print()
print()
