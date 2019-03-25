a = [1, 2, 3, 4, 5, 6]
t = [0]*len(a)

def perm(n, k):
    if k == n:
        print(a)
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]


def test_perm(n, r, k):
    if r == 0:
        print(t)
    else:
        for i in range(n-1, -1, -1):
            a[n-1], a[i] = a[i], a[n-1]
            t[r-1] = a[n-1]
            test_perm(n-1, r-1, k)
            a[n - 1], a[i] = a[i], a[n - 1]

# perm(6, 0)
test_perm(6, 6, 6)
