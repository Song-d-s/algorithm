# 15652. N과 M (4)
N, M = map(int, input().split())

def solve(k, s):
    if k >= M:
        print(' '.join(result))
        return

    for i in range(s, N+1):
        result[k] = str(i)
        solve(k+1, i)
    pass

result = [0] * M
solve(0, 1)