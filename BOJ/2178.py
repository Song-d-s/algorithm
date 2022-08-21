# 2178. 미로탐색
import sys
# sys.stdin = open('2178.txt')
input = sys.stdin.readline
#
from collections import deque
def bfs(y, x):          # BFS
    Q = deque()
    Q.append((y, x))
    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if not (0 <= ny < N and 0 <= nx < M):
                continue
            if maze[ny][nx] == 0:
                continue
            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                Q.append((ny, nx))
    return maze[N - 1][M - 1]


N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().rstrip())))

dy = [-1, 0, 1, 0]  # 상 우 하 좌
dx = [0, 1, 0, -1]

print(bfs(0, 0))
