# 2105. [모의 SW 역량테스트] 디저트 카페
import sys
sys.stdin = open('2105.txt')
#
def print_arr(arr):
    for a in arr:
        print(a)
#
T = int(input())

delta = [(-1,1),(1,1),(1,-1),(-1,-1)]

def bfs(pos, d, sum_v, sp):
    global max_v
    y, x = pos
    if d == 3:
        if pos == sp:
            temp = len(set(sum_v))
            if max_v < temp:
                max_v = temp
            return
    if d > 3:
        return
    for d_idx in range(2):
        dy, dx = delta[(d + d_idx) % 4]
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and (input_arr[ny][nx] not in sum_v):
            bfs((ny,nx), d + d_idx, sum_v + [input_arr[ny][nx]], sp)


for tc in range(1, T+1):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    max_v = 0

    for y in range(N):
        for x in range(N):
            bfs((y,x), 0, list(), (y,x))
    if max_v == 0: max_v = -1
    print(f'#{tc} {max_v}')
