# 16509. 장기
import sys
sys.stdin = open('16509.txt')
#
from collections import deque

delta_d = [(-3,-2),(-3,2),(-2,3),(2,3),(3,2),(3,-2),(2,-3),(-2,-3)]
delta_p = [
[(-1,0),(-2,-1)],[(-1,0),(-2,1)],
[(0,1),(-1,2)],[(0,1),(1,2)],
[(1,0),(2,1)],[(1,0),(2,-1)],
[(0,-1),(1,-2)],[(0,-1),(-1,-2)],
]

def move_elep():
    global minV
    Q.append(ELEPHANT)
    while Q:
        sy, sx = Q.popleft()
        if visited[sy][sx] >= minV:
            continue
        if sy == KING[0] and sx == KING[1]:
            if visited[sy][sx] < minV:
                minV = visited[sy][sx]
            return
        for idx, d in enumerate(delta_d):
            dy, dx = d
            ny, nx = sy+dy, sx+dx
            if 0<=ny<H and 0<=nx<W and visited[ny][nx]==0:
                bool = 1
                for p in delta_p[idx]:  # 장애물 검토
                    py, px = p
                    ppy, ppx = sy+py, sx+px
                    if field[ppy][ppx] == 1:
                        bool = 0
                if bool:
                    visited[ny][nx] = visited[sy][sx] + 1
                    Q.append((ny, nx))

ELEPHANT = tuple(map(int, input().split()))
KING = tuple(map(int, input().split()))

W, H = 9, 10    # W: 0 - 8, H: 0 - 9
visited = [[0]*W for _ in range(H)]
field = [[0]*W for _ in range(H)]
Q = deque()
y, x = ELEPHANT; visited[y][x] = 1  # 상 자리
y, x = KING; field[y][x] = 1        # 왕 자리
minV = 10e6
move_elep()

print(visited[y][x]-1)