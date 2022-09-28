# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산
import sys
sys.stdin = open('5247.txt')
#
# 그냥 재귀 함수로 풀면 시간 초과 또는 recursive error
from collections import deque
T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N, M = map(int, input().split())
    MAX = 1000001
    visited = [-1]*MAX

    Q = deque()
    Q.append(N)
    visited[N] = 0
    while Q:
        i = Q.popleft()
        if i == M:
            print(visited[i])
            break
        for idx in range(4):
            if idx == 0 and 0 < i+1 < MAX and visited[i+1] < 0 :
                Q.append(i+1)
                visited[i+1] = visited[i]+1
            elif idx == 1 and 0 < i-1 < MAX and visited[i-1] < 0 :
                Q.append(i-1)
                visited[i-1] = visited[i]+1
            elif idx == 2 and 0 < i*2 < MAX and visited[i*2] < 0 :
                Q.append(i*2)
                visited[i*2] = visited[i]+1
            elif 0 < i-10 < MAX and visited[i-10] < 0 :
                Q.append(i-10)
                visited[i-10] = visited[i]+1
