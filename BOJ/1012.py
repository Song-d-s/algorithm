# 1012. 유기농 배추
import sys
# sys.stdin = open('1012.txt')

# 시작
def dfs(n, m):              # DFS
    if n >= N or m >= M or n <= -1 or m <= -1:
        return False        # 범위 설정
    if mapping[n][m] == 1:
        mapping[n][m] = 0   # 노드 방문처리
        for x in range(-1, 2, 2):
            dfs(n + x, m)   # 상하좌우 재귀적 방문처리
            dfs(n, m + x)
        return True


T = int(sys.stdin.readline())
for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    pos = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(K))

    mapping = list([0] * M for _ in range(N))
    for coord in pos:
        mapping[coord[1]][coord[0]] = 1
    cnt = 0
    for coord in pos:
        if dfs(coord[1], coord[0]) == True:
            cnt += 1
    print(cnt)