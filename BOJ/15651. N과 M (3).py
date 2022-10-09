# 15651. N과 M (3)
N, M = map(int, input().split())

# 중복 순열
def prod(k):
    if k >= M:
        print(' '.join(result))
        return

    for i in range(1, N+1):
        result[k] = str(i)
        prod(k+1)
    pass

result = [0] * M
prod(0)