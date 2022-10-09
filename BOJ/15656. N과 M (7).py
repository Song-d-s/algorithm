# 15656. N과 M (7)
N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
#
def prod(k, res):
    if k >= M:
        print(res)
        return
    for i in range(N):
        prod(k+1,res+str(arr[i])+' ')
prod(0,'')