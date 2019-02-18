def process_solution(a, k, sum):
    if sum == 10:
        for i in range(1, k+1):
            if a[i]:
                print(data[i], end=' ')
        print()


def make_candidates(c):
    c[0], c[1] = True, False
    return 2


def backtrack(a, k, input, sum):
    if sum > 10:
        return
    c = [0] * 2
    if k == input:
        process_solution(a, k, sum)
    else:
        k += 1
        ncands = make_candidates(c)
        for i in range(ncands):
            a[k] = c[i]
            if a[k]:
                backtrack(a, k, input, sum + data[k])
            else:
                backtrack(a, k, input, sum)


data = [i for i in range(11)]
a = [0]*11
backtrack(a, 0, 10, 0)