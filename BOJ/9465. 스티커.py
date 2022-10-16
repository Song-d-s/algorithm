# 9469. 스티커
import sys
sys.stdin = open('9565.txt')
#
# def print_arr(arr):
#     for each in arr:
#         print(*each)
#
# 1. 선택 시 손익을 따져서 계산하고 최대값 우선으로 선별한다.
# 오답! 중복된 값이 나올 경우에 결과가 달라진다.
from collections import deque
T = int(input())
for tc in range(1, T+1):
    print('#', tc)
    N = int(input())
    SCORES = [list(map(int, input().split())) for _ in range(2)]
    calc_score = [[0]*N for _ in range(2)]
    print_arr(SCORES)
    coord_in_order = []
    for y in range(2):
        for x in range(N):
            coord_in_order.append((y,x))
            calc_score[y][x] = SCORES[y][x]
            for d in [(-1,0),(0,1),(1,0),(0,-1)]:
                dy, dx = d
                ny, nx = y+dy, x+dx
                if 0<=ny<2 and 0<=nx<N:
                    calc_score[y][x] -= SCORES[ny][nx]
    coord_in_order.sort(key = lambda coord: calc_score[coord[0]][coord[1]])
    print_arr(calc_score)
    print(coord_in_order)
    res = 0
    while coord_in_order:
        y, x = coord_in_order.pop()
        res += SCORES[y][x]
        for d in [(-1,0),(0,1),(1,0),(0,-1)]:
            dy, dx = d
            ny, nx = y+dy, x+dx
            if (ny, nx) in coord_in_order: coord_in_order.remove((ny,nx))
    print(res)
#
# 2. 최대한 많이, 큰 값을 선택하는 경우를 생각해본다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    SCORES = [list(map(int, input().split())) for _ in range(2)]

    for x in range(N):
        for y in range(2):
            maxv = 0
            for search in [(y^1,x-1), (y^1,x-2)]:
                ny, nx = search
                if 0<=nx:
                    if maxv < SCORES[ny][nx]: maxv = SCORES[ny][nx]
            SCORES[y][x] = SCORES[y][x] + maxv
    print(max(SCORES[0][-1], SCORES[1][-1]))