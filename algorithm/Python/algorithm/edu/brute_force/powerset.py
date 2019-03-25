def printset(n):
    for i in range(n):
        if A[i]:
            print(data[i], end=' ')
    print()


def powerset(n, k, s):
    global total
    if s == 10:
        total += 1
        printset(n)
    elif n == k or s > 10:
        return
    else:
        total += 1
        A[k] = 1  # 해당 index(k) 지점을 부분집합으로 쓰겠다는 표시
        powerset(n, k+1, s + data[k])
        A[k] = 0  # 위 지점을 0으로 돌림
        powerset(n, k+1, s)


data = [i+1 for i in range(10)]
A = [0 for _ in range(len(data))]
total = 0
powerset(len(data), 0, 0)
print(total)