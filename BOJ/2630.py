# 2630. 색종이 만들기
import sys
sys.stdin = open('2630.txt')
# 테스트
def printArr(arr):
    for l in arr: print(*l)
# 시작
N = int(input())
paperArr = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 0, 1, 1]
dx = [0, 1, 0, 1]

def dividePaper(sy, sx, width):
    sColor = paperArr[sy][sx]
    nwidth = width//2
    for y in range(width):
        for x in range(width):
            if paperArr[sy+y][sx+x] != sColor:
                for idx in range(4):
                    ny = sy + (nwidth * dy[idx])
                    nx = sx + (nwidth * dx[idx])
                    dividePaper(ny, nx, nwidth)
                return
    cntPaper[sColor] += 1

cntPaper = [0, 0]
dividePaper(0,0,N)
print(cntPaper[0])
print(cntPaper[1])