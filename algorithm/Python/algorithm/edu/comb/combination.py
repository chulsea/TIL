T = [0, 0, 0]
A = [i+1 for i in range(4)]


def __myprint(q):
    while q:
        q -= 1
        print(T[2-q], end=' ')
    print()


def combination(n, r, q):
    if r == 0:
        __myprint(q)
    elif n == 0:
        return
    else:
        T[r-1] = A[n-1]
        combination(n, r-1, q)
        combination(n-1, r, q)
        """
        중복조합
        """

def main():
    combination(len(A), 3, 3)


if __name__ == '__main__':
    main()
