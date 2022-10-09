# 15655. N과 M (6)
N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

# 조합
def comb(k, s, res):
    if k >= M:
        print(res)
        return
    for i in range(s, N):
        comb(k+1,i+1,res+str(arr[i])+' ')
comb(0,0,'')