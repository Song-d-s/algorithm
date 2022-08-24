# 10966. 물놀이를 가자
# BFS
import sys
# sys.stdin = open('10966.txt')
# 시작
from collections import deque  # deque 사용 안하고 list로는 시간 초과.

def bfs(Q):
    sum = 0
    while Q:
        y, x = Q.popleft()
        for idx in range(4):
            ny = y + dy[idx]
            nx = x + dx[idx]
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                Q.append((ny, nx))
        sum += visited[y][x]
    return sum

T = int(input())

for tc in range(T):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    N, M = map(int, input().split())
    field = [[] for _ in range(N)]
    # -1로 visited 배열 생성.
    visited = list([-1] * M for _ in range(N))
    Q = deque()

    for y in range(N):
        inputTxt = input()
        for x, str in enumerate(inputTxt):
            field[y].append(str)
            # W 주변을 먼저 탐색해야 하므로 먼저 인큐.
            if str == 'W':
                visited[y][x] = 0
                Q.append((y, x))

    print(f'#{tc + 1} {bfs(Q)}')
