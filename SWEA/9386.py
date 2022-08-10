#9386. 연속한 1의 개수
#User Problem > 연속한 1의 개수
import sys
sys.stdin = open("input.txt")
# 1.
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(int(x) for x in input())
    for i in range(1, N):
        arr[i] = arr[i-1] * arr[i] + arr[i]
    print(f'#{t+1} {max(arr)}')
# 2.
T = int(input())
for t in range(T):
    N = int(input())
    arr = [x for x in input().split('0') if x != '']
    maxV = 0
    for x in arr:
        if len(x) > maxV:
            maxV = len(x)
    print(f'#{t+1} {maxV}')