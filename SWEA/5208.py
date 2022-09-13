# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
# Programming Advanced 파이썬 SW문제해결 응용_구현 - 05 백트래킹
import sys
#sys.stdin = open('5208.txt')
#
def moveFunc(pos, cnt):
    global minMov
    if pos >= N-1:
        if minMov > cnt: minMov = cnt
        return
    cnt += 1
    if cnt >= minMov: return
    BATTERY = STATION[pos]
    for step in range(BATTERY, 0, -1):
        moveFunc(pos+step, cnt)

T = int(input())

for tc in range(1, T+1):
    STATION = list(map(int,input().split()))
    N = STATION.pop(0)
    minMov = N
    moveFunc(0, -1)

    print(f"#{tc} {minMov}")
