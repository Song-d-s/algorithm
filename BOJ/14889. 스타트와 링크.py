# 14889. 스타트와 링크
import sys
sys.stdin = open('14889.txt')
#
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

def comb(k, s):
    global minV
    if k >= N//2:
        strt = result
        lnk = list(set(range(1,N+1)) - set(strt))
        strt_res = 0
        lnk_res = 0
        for m in range(N//2):
            for n in range(m+1, N//2):
                strt_res += arr[strt[m]-1][strt[n]-1] + arr[strt[n]-1][strt[m]-1]
                lnk_res += arr[lnk[m]-1][lnk[n]-1] + arr[lnk[n]-1][lnk[m]-1]
        gap = abs(strt_res-lnk_res)
        if gap < minV:
            minV = gap
        return
    for i in range(s, N+1):
        result[k] = i
        comb(k+1, i+1)
minV = 10e6
result = [0]*(N//2)
comb(0, 1)
print(minV)