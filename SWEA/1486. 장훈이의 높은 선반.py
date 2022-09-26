# 1486. 장훈이의 높은 선반
import sys
sys.stdin = open('1486.txt')
#
T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())    # 직원 수, 선반 높이
    heights = list(map(int, input().split()))   # 직원 키

    def par(k, sum_v):
        global min_v
        if B - sum_v == 0:  # 일치
            min_v = 0
            return
        if sum_v > B + min_v: return    # 백트래킹 - 그러나 유의미한 차이 없음.
        if k == N:
            if 0 < sum_v - B < min_v:
                min_v = sum_v - B
            return
        for i in [0,1]:
            par(k+1, sum_v + heights[k] * i)

    min_v = 99999
    par(0, 0)
    print(f'#{tc} {min_v}')