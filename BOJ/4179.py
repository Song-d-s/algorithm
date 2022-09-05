# 4179. 불
'''
처음 생각했던 것과 다르게 불이 여러 개였고,
불이랑 지현이를 같이 이동시켜야 해서 큐를 4개나 써서 풀었다.
다른 방법이 있을 것 같다.
'''
#
import sys
#sys.stdin = open('4179.txt')
input = sys.stdin.readline
from collections import deque
#
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]
visited = [[0 for _ in list(range(C))] for _ in range(R)]

J = []
F = []
for r in range(R):
    for c in range(C):
        if maze[r][c] == 'J':
            J=[r, c]
        elif maze[r][c] == 'F':
            F.append([r, c])                
maze[J[0]][J[1]] = '.'                      # 지현이 위치 '.' 처리

def BFS():                                  # BFS 처리.
    Q = deque()
    fQ = deque()
    Q.append(J)
    visited[J[0]][J[1]] = 1
    for f in F:                             # 모든 F 불 큐에 넣기.
        fQ.append(f)
    QNow=deque()
    while Q:
        # 지현 이동
        while Q:
            QNow.append(Q.popleft())
        while QNow:
            cJihun = QNow.popleft()
            for idx in range(4):
                cjy, cjx = cJihun
                if maze[cjy][cjx] == 'F':   # 지현이가 불에 타는 중이면 continue.
                    continue
                ny , nx = cjy + dy[idx], cjx + dx[idx]
                if ny<0 or ny>R-1 or nx<0 or nx>C-1:
                    return visited[cjy][cjx]
                if 0<=ny<R and 0<=nx<C and maze[ny][nx]=='.' and visited[ny][nx]==0:
                    Q.append([ny, nx])
                    visited[ny][nx] = visited[cjy][cjx] + 1
        # 불 이동 
        fQNow = deque()  
        if fQ:
            while fQ:
                fQNow.append(fQ.popleft())
            while fQNow:
                cFire = fQNow.popleft()
                for idx in range(4):
                    cfy, cfx = cFire
                    nfy, nfx = cfy + dy[idx], cfx + dx[idx]
                    if 0<=nfy<R and 0<=nfx<C and maze[nfy][nfx]=='.':
                        maze[nfy][nfx]='F'
                        fQ.append([nfy,nfx])
    return 'IMPOSSIBLE'

print(BFS())