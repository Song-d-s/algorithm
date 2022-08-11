#4843. 특별한 정렬
import sys
sys.stdin = open('input.txt')
#
T = int(input())

def selsort(lst): # 선택 정렬
    for phase in range(0, N - 1):
        minP = phase
        for idx in range(phase, N):
            if lst[idx] < lst[minP]:
                minP = idx
        lst[minP], lst[phase] = lst[phase], lst[minP]
    return lst

for t in range(T):
    N = int(input())
    nbrs = list(map(int, input().split()))
    nbrs = selsort(nbrs)
    res = ''
    for n in range(10):
        if n%2:
            res += ' ' + str(nbrs.pop(0))
        else:
            res += ' ' + str(nbrs.pop())
    print(f"#{t+1}{res}")