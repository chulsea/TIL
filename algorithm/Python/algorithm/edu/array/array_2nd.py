arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()

for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j], end=' ')
    print()

n = len(arr)
m = len(arr[0])

for i in range(n):
    for j in range(m):
        print(arr[i][j + (m-1-2*j) * (i % 2)], end=' ')
    print()

arr2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

for y in range(len(arr2)):
    for x in range(len(arr2)):
        if y < x:
            arr2[y][x], arr2[x][y] = arr2[x][y], arr2[y][x]
print(arr2)