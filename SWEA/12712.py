# 12712. 파리퇴치3
# User Problem
import sys

sys.stdin = open("08.txt")
#
# 1. 교수님 풀이 - 델타
TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    BRD = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, 1, -1]

    maxV = 0
    for row in range(N):
        for col in range(N):
            # 사방면
            sumV = BRD[row][col]
            for direction in range(4):
                for distance in range(1, M):
                    newR = row + dr[direction] * distance
                    newC = col + dc[direction] * distance
                    if 0 <= newR < N and 0 <= newC < N:
                        sumV += BRD[newR][newC]
            if maxV < sumV:
                maxV = sumV
            # 대각선 확인
            sumV = BRD[row][col]
            for direction in range(4, 8):
                for distance in range(1, M):
                    newR = row + dr[direction] * distance
                    newC = col + dc[direction] * distance

                    if 0 <= newR < N and 0 <= newC < N:
                        sumV += BRD[newR][newC]

            if maxV < sumV:
                maxV = sumV

    print('#{} {}'.format(tc, maxV))
#
# 2. 내 풀이
def crossline(y, x, k):
    res = list()
    res.append([y, x])
    for m in range(1, M):
        res.extend([[y - m, x - m * k], [y - m * k, x + m], [y + m, x + m * k], [y + m * k, x - m]])
    return res


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    maps = list()
    maps += (list(map(int, input().split())) for _ in range(N))
    maxV = 0
    for y in range(N):
        for x in range(N):
            for k in range(2):
                cnt = 0
                for g in crossline(y, x, k):
                    if 0 <= g[0] < N and 0 <= g[1] < N:
                        cnt += maps[g[0]][g[1]]
                if maxV < cnt:
                    maxV = cnt
    print(f'#{t + 1} {maxV}')