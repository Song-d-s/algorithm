# 15663. N과 M (9)
N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
#
def perm(k, res):
    if k >= M:
        if not res in result:
            result.append(res)
            print(res)
        return
    for i in range(N):
        if visited[i]: continue
        visited[i] = True
        perm(k+1, res+str(arr[i])+' ')
        visited[i] = False
    pass

result = []
visited = [False]*N
perm(0,'')

# dfs로 다시 풀어보자