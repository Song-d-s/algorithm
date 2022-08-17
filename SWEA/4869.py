#4869. 종이 붙이기
#Programming Intermediate > 파이썬 SW문제해결 기본 - Stack1 
import sys
sys.stdin = open("input.txt")

from math import factorial

def nCr(n, r): # n개중 같은 r개를 선택하는 경우의 수 nCr
    return factorial(n)//factorial(r)//factorial(n-r)

T=int(input()) # 여러(T)개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(T):
    width = int(input())//10 # 가로 길이 / 10
    
    cnt = 0
    for x in range(width//2+1): # 20짜리 종이 개수
        if x == 0:
            cnt += 1
        else:
            num_cnt = width - x # 20짜리 개수에 따른 총 종이 개수
            cnt += 2**x*nCr(num_cnt , x) # nCr

    print(f'#{t+1} {cnt}')