# 15654. N과 M (5)
N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

# 순열
def perm(k):
    if k >= M:
        print(' '.join(result))
        return
    for i in range(N):
        if visited[i]: continue
        visited[i] = True
        result[k] = str(arr[i])
        perm(k+1)
        visited[i] = False

result = [0] * M
visited = [False] * N
perm(0)