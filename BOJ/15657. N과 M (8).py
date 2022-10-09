# 15657. N과 M (8)
N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
#
def prod(k, s, res):
    if k >= M:
        print(res)
        return
    for i in range(s, N):
        prod(k+1,i,res+str(arr[i])+' ')
prod(0,0,'')