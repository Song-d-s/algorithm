# Programming Intermediate > 파이썬 SW문제해결 기본 - Stack1
# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
import sys
sys.stdin = open("input.txt")
#
T = int(input())

def verify(S, G):  # dfs
    Q = list()
    vstchk = list(False for _ in range(V + 1))
    Q.append(S)
    while Q:
        vst = Q.pop()
        vstchk[vst] = True
        for x in range(V + 1):
            if not vstchk[x] and x in arr[vst]:
                Q.append(x)
    return vstchk[G]

for t in range(T):
    V, E = map(int, input().split())  # V, E input
    arr = list([] for _ in range(V + 1))
    for x in range(1, E + 1):  # node mapping
        m, n = map(int, input().split())
        arr[m].append(n)
    S, G = map(int, input().split())  # S, G input (Start, Goal)
    print(f'#{t + 1} {int(verify(S, G))}')