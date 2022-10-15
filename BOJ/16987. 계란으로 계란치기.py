# 16987. 계란으로 계란치기
import sys
sys.stdin = open('16987.txt')
#
def solve(egg_on_hand):
    global maxV
    if egg_on_hand >= N:
        cnt = 0             # 깨진 달걀 카운트
        for each in range(N):
            if EGGS[each][0] <= 0:
                cnt += 1
        if maxV < cnt: maxV = cnt
        return
    if EGGS[egg_on_hand][0] > 0:
        only_one = True     # 자기 자신 뿐일 때
        for target in range(N):
            if target != egg_on_hand and EGGS[target][0] > 0:
                only_one = False
                EGGS[egg_on_hand][0] -= EGGS[target][1]
                EGGS[target][0] -= EGGS[egg_on_hand][1]
                solve(egg_on_hand+1)    # 재귀
                EGGS[egg_on_hand][0] += EGGS[target][1]
                EGGS[target][0] += EGGS[egg_on_hand][1]
        if only_one: solve(N)
    else:
        solve(egg_on_hand+1)

N = int(input())
EGGS = [list(map(int, input().split())) for _ in range(N)] # (내구도, 무게)

maxV = 0
solve(0)
print(maxV)