max_h = int(input())
n = int(input())
dist = list(map(int, input().split()))
times = list(map(int, input().split()))
chk = [0]*n
ans = 0x7fffffff


def __comb(n, r, k, s):
    global ans, max_h
    if k < dist[r]:
        # 현재 갈 수 있는 이동거리로 다음 정비소에 못가는 경우
        return
    if ans < s:
        return
    if r == n:
        if ans > s:
            ans = s
    else:
        __comb(n, r+1, max_h, s+times[r])
        if k > dist[r]:
            # 현재 남은 이동거리가 이동한 거리 이상인 경우 정비하지 않음
            __comb(n, r+1, k-dist[r], s)


__comb(n, 0, max_h, 0)
print(ans)