# 14719. 빗물
import sys
#sys.stdin = open('14719.txt')
input = sys.stdin.readline
#
H, W = map(int, input().split())
FIELD = list(map(int, input().split()))

# 3. 좌우비교
rain = 0
for idx in range(1, W-1):   # 맨 끝은 어차피 물이 안 쌓인다.
    L , R = FIELD[:idx] , FIELD[idx+1:]
    if idx != 0 and idx != W-1:
        curVal = min(max(L), max(R))-FIELD[idx]
        if curVal > 0: rain += curVal
print(rain)


'''
# 2. 재귀, 최대값 피봇 정하기 - 오답
# 반례를 못찾겠다.
rain = 0
max = 0
pivot = [-1,-1]
for idx, h in enumerate(FIELD):
    # print(idx, h)
    if h > max:
        max = h
        pivot = [idx, -1]
    elif h == max:
        pivot[1] = idx
if pivot[1] == -1: pivot[1]=pivot[0]
# print(pivot, max)
rain = 0
for idx in range(pivot[0]+1, pivot[1]):
    rain += max-FIELD[idx]
# print(rain)
# print(FIELD[:pivot[0]])     # 좌
# print(FIELD[pivot[1]+1:])   # 우

def rainCalc(arr, d): #d -1 좌, 1 우
    global rain
    max = 0
    pivot = [-1, -1]
    for idx, h in enumerate(arr):
        # print(idx, h)
        if h > max:
            max = h
            pivot = [idx, -1]
        elif h == max:
            pivot[1] = idx
    if pivot[1] == -1: pivot[1]=pivot[0]
    # print(pivot, max, d)
    
    if d == -1:       # 좌측
        for idx in range(pivot[0]+1, len(arr)):
            # print(arr[idx], max-arr[idx])
            rain += max-arr[idx]
        if len(arr[:pivot[0]]) >= 1:
            rainCalc(arr[:pivot[0]], -1)
    elif d == 1: # 우측
        for idx in range(0, pivot[0]):
            # print(arr[idx], max-arr[idx])
            rain += max-arr[idx]
        if len(arr[pivot[1]+1:])>=1:
            rainCalc(arr[pivot[1]+1:], 1)

rainCalc(FIELD[:pivot[0]], -1)
rainCalc(FIELD[pivot[1]+1:], 1)

print(rain)'''

'''
# 1. 오답
from collections import deque
columns = deque()    # 여기다 시작 기둥, 끝 기둥 저장할 것.

columns.append((0, FIELD[0]))
idx = 0
while idx < W-1:
    idx += 1
    col = FIELD[idx]
    # print(idx, col, ':', rain)
    # print(columns)
    
    if len(columns) < 2:
        if columns[0][1] <= col:
            columns.popleft()
        columns.append((idx, col))
    else:
        if columns[0][1] <= col:
            for i in range(columns[0][0]+1, idx):
                rain += columns[0][1] - FIELD[i]
            columns.clear()
            columns.append((idx, col))
        elif columns[1][1] <= col:
            columns.pop()
            columns.append((idx, col))
    if idx == W-1 and len(columns)==2:
        for i in range(columns[0][0]+1, columns[1][0]):
            rain += columns[1][1] - FIELD[i]
        if columns[1][0] != W-1:
            idx = columns[1][0] + 1
            columns.clear()
            columns.append((idx, FIELD[idx]))
    # print(columns)
print(rain)'''