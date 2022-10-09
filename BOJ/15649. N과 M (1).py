# 15649. N과 M
N, M = map(int, input().split())

# 순열
def perm(k):
    if k >= M:
        print(' '.join(result))
        return
    for i in range(1, N+1):
        if visited[i]: continue
        visited[i] = True
        result[k] = str(i)
        perm(k+1)
        visited[i] = False
    pass

result = [0] * M
visited = [False] * (N+1)
perm(0)