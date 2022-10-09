# 15686. 치킨배달
# 순열
import sys
sys.stdin = open('15686.txt')
sys.setrecursionlimit(10**6)
#
def print_arr(arr):
    for a in arr:
        print(*a)
#
def getdist(coord1, coord2):
    y1, x1 = coord1
    y2, x2 = coord2
    return abs(y1-y2) + abs(x1-x2)

N, M = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(N)]
kfc = []
house = []
for y in range(N):
    for x in range(N):
        if village[y][x] == 2:
            kfc.append((y,x))
        elif village[y][x] == 1:
            house.append((y,x))
kfc_n = len(kfc)
visited = [False]*kfc_n
chicken_v = [100]*len(house)


def combi(k, s, result):
    global chicken_v
    if k >= M:
        temp = [100]*len(house)
        for kfc_idx in result:
            for house_idx in range(len(house)):
                dist = getdist(house[house_idx], kfc[kfc_idx])
                if temp[house_idx] > dist: temp[house_idx] = dist
        if sum(chicken_v) > sum(temp):
            chicken_v = temp
        return
    for i in range(s, kfc_n):
        combi(k+1, i+1, result + [i])


combi(0, 0, [])

print(sum(chicken_v))
