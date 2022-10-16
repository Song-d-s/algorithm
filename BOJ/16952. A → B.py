# 16952. A → B
A, B = map(int, input().split())
cnt = 0
while A != B:
    if A > B:
        cnt = -1
        break
    if B % 2:
        if str(B)[-1] == '1':
            B -= 1
            B //= 10
            cnt += 1
        else:
            cnt = -1
            break
    else:
        cnt += 1
        B //= 2
if cnt != -1: cnt += 1
print(cnt)