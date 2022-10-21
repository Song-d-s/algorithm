# 12865. 평범한 배낭
import sys
sys.stdin = open('12865.txt')
from pprint import pprint
# DP
# 참고: https://gsmesie692.tistory.com/113
# 입력
cargo_no, weight_limit = map(int, input().split())

weights = []; values = []
for _ in range(cargo_no):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# 최적값 저장 테이블
value_table = [[0]*(weight_limit+1) for _ in range(cargo_no+1)]

for idx in range(cargo_no+1):
    for w in range(weight_limit+1):
        if w == 0 or idx == 0: continue
        if weights[idx-1] <= w:
            value_table[idx][w] = max(values[idx-1]+value_table[idx-1][w-weights[idx-1]], value_table[idx-1][w])
        else:
            value_table[idx][w] = value_table[idx-1][w]

print(value_table[cargo_no][weight_limit])

# 1. 메모리 초과
# import sys
# sys.setrecursionlimit(10**6)
# N, K = map(int, input().split())
# W = []
# V = []
# R = []
# for _ in range(N):
#     w, v = map(int, input().split())
#     W.append(w)
#     V.append(v)
#     R.append()

# def solve(k, s, v_sum, w_sum, last):
#     global maxV
#     if K < w_sum:
#         if maxV < v_sum - V[last]:
#             maxV = v_sum - V[last]
#         return
#     for i in range(s, N):
#         solve(k+1, i+1, v_sum + V[i], w_sum + W[i], i)

# maxV = 0
# solve(0, 0, 0, 0, 0)
# print(maxV)
