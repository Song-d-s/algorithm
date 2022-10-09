# 15665. N과 M (11)
N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
#
def prod(k, res):
    if k >= M:
        print(*res)
        return
    prev = 0
    for i in range(N):
        if prev != arr[i]:
            prod(k+1, res+[arr[i]])
            prev = arr[i]

prod(0,[])