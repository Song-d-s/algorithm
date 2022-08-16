# 5432. 쇠막대기 자르기
import sys

sys.stdin = open('06.txt')

T = int(input())
for t in range(T):
    inputarr = list(input())
    inputlen = len(inputarr)
    opnd = list()
    pieces = 0
    for x in range(inputlen):
        if inputarr[x] == '(': # 여는 괄호 '(' 의 경우
            opnd.append(inputarr[x])
            pieces += 1 # opnd stack에 추가하고 pieces +1
        else: # 닫힌 괄호 ')' 인 경우
            opnd.pop()
            if inputarr[x - 1] == '(': # 레이저인 경우
                # pieces를 다시 -1 한 후, stack의 '(' 개수만큼 +
                pieces += len(opnd) -1 
    print(f'#{t + 1} {pieces}')