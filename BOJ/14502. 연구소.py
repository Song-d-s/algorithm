# 14502. 연구소
import sys
sys.stdin = open('14502.txt')
#
def print_arr(arr):
    for each in arr:
        print(*each)
#
from itertools import combinations
from collections import deque

N, M = map(int, (input().split()))
lab = [list(map(int, input().split())) for _ in range(N)]

corridor = []
virus = []

for y in range(N):
    for x in range(M):
        if lab[y][x] == 0:
            corridor.append((y,x))
        elif lab[y][x] == 2:
            virus.append((y,x))
candid = list(combinations(corridor, 3))
maxv = 0
safeplace = len(corridor)
for each in candid:
    # 벽 건설
    for build_here in each:
        y, x = build_here
        safeplace -= 1
        lab[y][x] = 1
    # BFS
    Q = deque(virus)
    temp = deque()
    while Q:
        vy, vx = Q.popleft()
        for d in [(-1,0),(0,1),(1,0),(0,-1)]:
            dy, dx = d
            ny, nx = vy + dy, vx + dx
            if 0<=ny<N and 0<=nx<M and lab[ny][nx]==0:
                lab[ny][nx] = 2
                safeplace -= 1
                temp.append((ny, nx)) 
                Q.append((ny, nx))  
    if maxv < safeplace: maxv = safeplace
    # 벽 철거
    for build_here in each:
        y, x = build_here
        safeplace += 1
        lab[y][x] = 0
    for restore_here in temp:
        y, x = restore_here
        safeplace += 1
        lab[y][x] = 0
print(maxv)
