#9489. 고대 유적
#User Problem > 고대 유적
import sys
sys.stdin = open("input.txt")
#
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    mapH = list()
    mapV = [[] for _ in range(M)]
    strmap = set()
    for m in range(N):
        mapH.append(list(input().split()))
        strmap.add(''.join(mapH[m]))
    for m in range(M):
        for n in range(N):
            mapV[m].append(mapH[n][m])
            strmap.add(''.join(mapV[m]))
    strmap = list(map(lambda x: x.split('0'), strmap))
    # t = [y for x in lst for y in x] 배열에서 꺼내기
    strmap = set([y for x in strmap for y in x if y!=''])
    maxV = 0
    for y in strmap:
        if maxV < len(y):
            maxV = len(y)
    print(f'#{t+1} {maxV}')