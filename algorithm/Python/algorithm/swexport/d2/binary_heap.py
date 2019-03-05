def __add_heap(heap, idx, val):
    heap[idx] = val
    __heapify(heap, idx)


def __heapify(heap, idx):
    c = idx
    p = idx // 2
    while c > 1 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p //= 2


def __anc_sum(heap, idx):
    next = idx
    answer = 0
    while next > 0:
        next //= 2
        answer += heap[next]
    return answer


def solution(nodes):
    n = len(nodes)
    heap = [0]*(n+1)
    for i in range(n):
        __add_heap(heap, i+1, nodes[i])
    return __anc_sum(heap, n)


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        input()
        nodes = list(map(int, input().split()))
        print("#{} {}".format(test_case+1, solution(nodes)))


if __name__ == '__main__':
    main()
