# 5102. 노드의 거리
import sys
sys.stdin = open('01.txt')
#
from collections import deque
def bfs(S):
    Q = deque()
    visited = [-1 for _ in range(V+1)]
    Q.append(S)
    visited[S] = 0
    while Q:
        idx = Q.popleft()
        for s in edges[idx]:
            if visited[s] == -1:
                Q.append(s)
                visited[s] = visited[idx] + 1
            if s == G:
                return visited[G]
    if visited[G] == -1:
        return 0


T = int(input())

for tc in range(T):
    V, E = map(int, input().split())
    inputarr = [tuple(map(int,input().split())) for _ in range(E)]

    edges = [[] for _ in range(V+1)]

    for i in inputarr:
        a, b = i
        edges[a].append(b)
        edges[b].append(a)

    S, G = map(int, input().split())    # 시작 노드 S, 도착 G

    print(f'#{tc+1}', end=' ')
    print(bfs(S))
