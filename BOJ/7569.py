# 7569. 토마토
import sys
#sys.stdin = open('7569.txt')
input = sys.stdin.readline
#
from collections import deque
N, M, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 0, 1, 0]
dx = [0, 0, 0, 1, 0, -1]            # 3중 배열 Z, Y, X / tomatoes[z][y][x]

Q = deque()
cnt = 0
for sz in range(H):                 # Q에 1(익은 토마토)을 다 넣고 시작한다.
    for sy in range(M):             # 모든 1을 먼저 방문처리 하지 않을 경우,
        for sx in range(N):         # '1 0 0 0 0 0 0 0 0 1'와 같은 경우 정답인 4가 아닌 8을 반환함.
            if tomatoes[sz][sy][sx] == 1: Q.append((sz, sy, sx))

def BFS():
    global cnt
    while Q:
        cz, cy, cx = Q.popleft()
        for delta in range(6):
            nz, ny, nx = cz+dz[delta], cy+dy[delta], cx+dx[delta]
            if 0<=nz<H and 0<=ny<M and 0<=nx<N and tomatoes[nz][ny][nx]==0:
                tomatoes[nz][ny][nx] = tomatoes[cz][cy][cx] + 1
                if cnt < tomatoes[nz][ny][nx] - 1: cnt = tomatoes[nz][ny][nx] - 1
                Q.append((nz, ny, nx))

BFS()

def printStatus():
    for z in range(H):
        for y in range(M):
            if 0 in tomatoes[z][y]:
                print(-1)
                return
    print(cnt)

printStatus()

# visited 배열을 사용하는 경우.
# visited = [[[0]*N for _ in range(M)] for _ in range(H)]
# def BFS():
#     global cnt
#     while Q:
#         cz, cy, cx = Q.popleft()
#         for delta in range(6):
#             nz, ny, nx = cz+dz[delta], cy+dy[delta], cx+dx[delta]
#             if 0<=nz<H and 0<=ny<M and 0<=nx<N and tomatoes[nz][ny][nx]==0:
#                 tomatoes[nz][ny][nx] = 1
#                 visited[nz][ny][nx] = visited[cz][cy][cx] + 1
#                 if cnt < visited[nz][ny][nx]: cnt = visited[nz][ny][nx]
#                 Q.append((nz, ny, nx))