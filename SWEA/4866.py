#4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
#Programming Intermediate > 파이썬 SW문제해결 기본 - Stack1

import sys
sys.stdin = open("input.txt")
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = int(input())
opnd = ['(', '{']
clsd = [')', '}']

for t in range(T):
    input_txt = input()
    lst = []
    check = 1
    for s in input_txt:
        if s in opnd:
            lst.append(s) # 여는 괄호는 스택에 추가.
        elif s in clsd: # 닫는 괄호가 나오는 경우.
            pair = opnd[clsd.index(s)]
            if len(lst) > 0 and pair == lst[len(lst)-1]: 
                lst.pop() # 닫는 괄호가 스택의 괄호와 짝이 맞으면 꺼낸다.
            else:
                check = 0 # 그렇지 않으면 거짓(0).
                break
    if len(lst): # 스택에 괄호가 남아 있으면 거짓(0).
        check = 0
    print(f'#{t+1} {check}')




