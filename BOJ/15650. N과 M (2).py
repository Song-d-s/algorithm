# 15650. N과 M(2)
N, M = map(int, input().split())

# 조합
def comb(k,s):
    if k >= M:
        print(' '.join(result))
        return
    for i in range(s, N+1):
        result[k] = str(i)
        comb(k+1, i+1)

result = [0]*M
comb(0,1)