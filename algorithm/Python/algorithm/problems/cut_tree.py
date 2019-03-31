def cut(l, r, h):
    result = 0
    for i in range(l, r):
        result += trees[i] - h
    return result

def tree_bs(l, r, k):
    while l <= r:
        mid = (l + r) // 2
        if trees[mid] == k:
            return mid
        if trees[mid] > k:
            r = mid - 1
        else:
            l = mid + 1
    return l

def bs(l, r, k):
    t = r
    while l <= t:
        mid = (t + l) // 2
        idx = tree_bs(0, len(trees), mid)
        get_trees = cut(idx, len(trees), mid)
        if get_trees == k:
            return mid
        if get_trees < k:
            t = mid - 1
        else:
            l = mid + 1
    return t

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
print(bs(trees[0], trees[-1], m))
