# 1267. [S/W 문제해결 응용] 10일차 - 작업순서
import sys
sys.stdin = open('1267.txt')
#
from collections import deque
T = 10

def checkReq(idx):
    for r in req[idx]:
        if done[r] == 0: return 0
    return 1


for tc in range(1, T+1):
    V, E = map(int, input().split())
    inputArr = list(map(int,input().split()))

    req = list([] for _ in range(V + 1))
    done = list(0 for _ in range(V + 1))
    startNode = 0
    for idx, val in enumerate(inputArr):
        if not idx % 2: startNode = val
        else: req[val].append(startNode)
    print(f'#{tc}', end=' ')
    Q = deque()
    for x in range(1, V+1): Q.append(x)
    while Q:
        cWork = Q.popleft()
        if checkReq(cWork):
            done[cWork] = 1
            print(cWork, end=' ')
        else: Q.append(cWork)
    print()