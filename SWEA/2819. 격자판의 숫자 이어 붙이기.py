# 2819. 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open('2819.txt')
#
def print_arr(arr):
    for a in arr:
        print(a)
#
delta = [(-1,0), (0,1), (1,0), (0,-1)] # (y, x)

def bfs(pos, stck):
    y, x = pos
    if len(stck) == 7:
        res.add(stck)
        return
    for d in delta:
        dy, dx = d
        ny, nx = y + dy, x + dx
        if 0 <= ny < 4 and 0 <= nx < 4:
            bfs((ny, nx), stck + input_arr[ny][nx])


T = int(input())
for tc in range(1, T+1):
    input_arr = [input().split() for _ in range(4)]

    res = set()

    for y in range(4):
        for x in range(4):
            bfs((y,x), '')

    print(f'#{tc} {len(res)}')