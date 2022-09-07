# 1305. 광고
import sys
sys.stdin = open('1305.txt')
input = sys.stdin.readline

# 3. Pi array > KMP algorithm
# prefix, suffix를 찾아도 다른 방법으로는 절대 시간 내 해결이 안되었다.
# 참고 : https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
N = int(input())
inTxt = list(input())
lps = [0]*N

def lpsCount(inTxt, lps):
    j = 0
    i = 1
    while i < N:
        if inTxt[i] == inTxt[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j != 0:
            j = lps[j-1]
        else:
            lps[i] = 0
            i += 1
    
lpsCount(inTxt,lps)
print(N- lps[N-1])


'''
# 2. 슬라이싱 : 시간초과
N = int(input())
inTxt = input()
inTxtLen = N

def findRep(pat, patLen):
    if patLen == inTxtLen:
        print(patLen)
        return 1
    preLen = inTxtLen % patLen
    if inTxt[-preLen:] != pat[:preLen]:
        return
    patRep = inTxtLen // patLen
    if pat*patRep != inTxt[:patLen*patRep]:
        return
    print(patLen)
    return 1

if inTxt==inTxt[0]*inTxtLen:
    print(1)
else:
    for patLen in range(2, inTxtLen+1):
        pat = inTxt[:patLen]
        # print('#', pat)
        if findRep(pat, patLen):
            break
'''

'''
# 1. 단순 탐색 : 시간 초과
N = int(input())
inTxt = input()

def findShortrep():
    ptrn = ''
    for n in range(1, N + 1):
        ptrn = inTxt[:n]
        ptrnL = len(ptrn)
        # print('#', ptrn)
        for sp in range(n, N, ptrnL):
            ep = sp + ptrnL
            if ep > N:
                ep = N
            tgt = inTxt[sp:ep]
            # print(tgt)
            if tgt == ptrn[:len(tgt)]:
                if ep == N:
                    return n
            else:
                break

# findShortrep()
print(findShortrep())
'''