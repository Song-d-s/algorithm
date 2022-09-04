# 1926. 그림
import sys
#sys.stdin = open('1926.txt')
input = sys.stdin.readline
#
# 입력
H, W = map(int, input().split())
field = list(list(map(int,input().split())) for _ in range(H))
#visited = [list(0 for _ in range(W)) for _ in range(H)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 3. BFS 풀이
# - BFS 탐색
# - visited 배열을 사용하지 않고 그래프를 0으로 지우면서 이동.

from collections import deque

Q = deque()
max = 0
cntDrw = 0
for sy in range(H):
    for sx in range(W):
        if field[sy][sx] == 1:
            cntDrw += 1
            Q.append((sy,sx))
            field[sy][sx] = 0
            cnt = 1
            while Q:
                cy, cx = Q.popleft()
                for idx in range(4):
                    ny = cy + dy[idx]
                    nx = cx + dx[idx]
                    if 0<=ny<H and 0<=nx<W and field[ny][nx]==1:
                        cnt += 1
                        field[ny][nx] = 0
                        Q.append((ny,nx))
            if max < cnt:
                max = cnt
print(cntDrw)
print(max)

# 1. Recursion Error
# from sys import setrecursionlimit
# sys.setrecursionlimit = 10**6

# def func(y, x):
#     global s
#     if y<0 or y>=H or x<0 or x>=W:
#         return 0
#     if field[y][x]==1 and visited[y][x]==0:
#         s += 1
#         visited[y][x] = s
#         for idx in range(4):
#             ny = y + dy[idx]
#             nx = x + dx[idx]
#             if 0<=ny<H and 0<=nx<W:
#                 if field[ny][nx] == 1:
#                     func(ny, nx)
#         return 1
#     return 0

# cnt = 0
# maxV = 0
# for h in range(H):
#     for w in range(W):
#         s = 0
#         if func(h,w):
#             cnt += 1
#             if maxV < s:
#                 maxV = s
# print(cnt)
# print(maxV)

# 2. 시간초과
# from collections import deque

# Q = deque()
# max = 0
# Tcnt = 0
# for sy in range(H):
#     for sx in range(W):
#         if field[sy][sx] == 1 and visited[sy][sx] == 0:
#             Tcnt += 1
#             Q.append((sy,sx))
#             visited[sy][sx] = 1
#             cnt = 1
#             while Q:
#                 cy, cx = Q.popleft()
#                     for idx in range(4):
#                         ny = cy + dy[idx]
#                         nx = cx + dx[idx]
#                         if 0<=ny<H and 0<=nx<W:
#                             if field[ny][nx]==1 and visited[ny][nx]==0:
#                                 cnt += 1
#                                 visited[ny][nx] = cnt
#                                 if max < visited[ny][nx]:
#                                     max = visited[ny][nx]
#                                 Q.append((ny,nx))
# print(Tcnt)
# print(max)
        
## hint: BFS
