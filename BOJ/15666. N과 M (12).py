# 15666. N과 M (12)
N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
#
def solve(k, s, res):
    if k >= M:
        print(*res)
        return
    prev = 0
    for i in range(s, N):
        if prev != arr[i]:
            solve(k+1, i, res+[arr[i]])
            prev = arr[i]

visited = [False]*N
solve(0,0,[])