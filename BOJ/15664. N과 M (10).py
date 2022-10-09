# 15664. N과 M (10)
N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
#
def comb(k, s, res):
    if k >= M:
        print(*res)
        return
    prev = 0
    for i in range(s, N):
        if prev != arr[i]:
            comb(k+1, i+1, res+[arr[i]])
            prev = arr[i]

visited = [False]*N
comb(0,0,[])