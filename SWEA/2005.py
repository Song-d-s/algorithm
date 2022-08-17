# 2005. 파스칼의 삼각형
import sys
sys.stdin = open('input.txt')
#
T = int(input())
for t in range(T):
    print(f'#{t+1}')
    N = int(input())
    txt = list([] for _ in range(N+1))
    for n in range(1, N+1):
        for y in range(n):
            if y == 0 or y == n-1:
                txt[n].append(1)
            else:
                txt[n].append(txt[n-1][y-1]+txt[n-1][y])
        print(*txt[n])