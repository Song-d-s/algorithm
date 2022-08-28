# 2116. 주사위 쌓기
# import sys
# sys.stdin = open('2116.txt')
#
diceN = int(input())    # 주사위 숫자
diceArr = [list(map(int, input().split())) for _ in range(diceN)]

def returnMaxOnSide(dice, tVal):    # 탑 값에 따른 측면 최대값 리턴.
    t = dice.index(tVal)
    b = returnOpp[t]
    max = 0
    for idx in range(6):
        if idx != t and idx != b:
            if max < dice[idx]:
                max = dice[idx]
    return max

returnOpp = [5,3,4,1,2,0]           # 반대편 인덱스 리턴.

max = 0
M = 6*diceN
for idx in range(6):                # 첫 주사위 경우의 수 6가지
    top = [diceArr[0][idx]]
    sum = returnMaxOnSide(diceArr[0], top[-1])
    for d in range(1, diceN):       # 2번 주사위부터 쌓으면서 측면 최대값 계산.
        top.append(diceArr[d][returnOpp[diceArr[d].index(top[d-1])]])
        sum += returnMaxOnSide(diceArr[d], top[-1])
    if max < sum:
        max = sum
    if max == M:                    # 이미 최대값인 경우 탈출.
        break
print(max)