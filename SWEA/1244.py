# 1244. 최대상금
# 순열
import sys
sys.stdin = open('1244.txt')
#
def make_perm(excT):
    tempV = int(''.join(input_arr))
    if tempV in record[excT]: return
    record[excT].add(tempV)
    if excT == excN: return
    for i in range(N-1):
        for j in range(i+1, N):
            input_arr[i], input_arr[j] = input_arr[j], input_arr[i]
            tempV = int(''.join(input_arr))
            if int(''.join(input_arr)) not in record[excT+1]: make_perm(excT+1)
            input_arr[i], input_arr[j] = input_arr[j], input_arr[i]

T = int(input())
for tc in range(1, T+1):
    input_str, excN = input().split(); excN = int(excN)
    input_arr = list(input_str)
    N = len(input_arr)
    maxV = 0; record = [set() for _ in range(excN+1)]
    make_perm(0)
    print(f'#{tc} {max(record[-1])}')