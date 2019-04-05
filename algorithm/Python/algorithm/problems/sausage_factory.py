"""
소세지공장 (greedy)
기준을 정해서 정렬(높이 or 너비)
만약 높이를 기준으로 정렬한다면 너비 상태만 확인하면 된다.
너비를 확인 할 때 기준이 되는 소시지와 비교, 이때 너비가 크다면 기준을 바꿔준다.
"""
def solution(arr, chk, n):
    cnt = 0
    while 0 in chk:
        base = 0
        cnt += 1
        for i in range(n):
            if not chk[i] and base <= arr[i][1]:
                chk[i] = 1
                base = arr[i][1]
    return cnt


n = int(input())
temp = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append((temp[i*2], temp[i*2+1]))
arr.sort(key=lambda x: x[0])
chk = [0]*n
print(solution(arr, chk, n))