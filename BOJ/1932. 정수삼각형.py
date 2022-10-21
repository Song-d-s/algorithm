# 1932. 정수삼각형
import sys
sys.stdin = open('1932.txt')
#
N = int(input())
TRI = [list(map(int, input().split())) for _ in range(N)]

# 2. 반복문, DP
i = 0
for i in range(N):
    if i == 0: continue
    for elem in range(i+1):
        if elem == 0:
            TRI[i][elem] += TRI[i-1][elem]
        elif elem == i:
            TRI[i][elem] += TRI[i-1][elem-1]
        else:
            TRI[i][elem] += max(TRI[i-1][elem-1], TRI[i-1][elem])
print(max(TRI[-1]))

# # 1. 재귀 - 시간 초과
# def solve(y, x, res):
#     global max_v
#     if y >= n:
#         if res > max_v: max_v = res
#         return
#     solve(y+1, x, res+tri[y][x])
#     solve(y+1, x+1, res+tri[y][x+1])

# max_v = 0
# solve(1, 0, tri[0][0])
# print(max_v)