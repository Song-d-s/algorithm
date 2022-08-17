#6588. 골드바흐의 추측
from sys import stdin

max_n = 1000000
oddprime = [True for _ in range(max_n+1)]
oddprime[0] = oddprime[1] = False
# 아리스토테네스의 체 - 소수 판별
for x in range(2, int(max_n**0.5)+1):
    if oddprime[x]:
        for y in range(x*2, max_n, x):
            oddprime[y] = False
oddprime[2] = False

def Goldbach(number):
    for x in range(3,number, 2):
        if oddprime[number - x] and oddprime[x]:
            return f'{number} = {x} + {number-x}'
    return "Goldbach's conjecture is wrong."

while True:
    input_num = int(stdin.readline())
    if input_num == 0:
        break
    print(Goldbach(input_num))