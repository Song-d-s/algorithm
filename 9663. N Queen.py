# 9663. N-Queen

N = int(input())
chessboard = [0]*N

def check(row):
    for i in range(row):    # 대각선은 거리에 비례
        if chessboard[row] == chessboard[i] or abs(chessboard[row]-chessboard[i]) == abs(row-i):
            return False
    return True

def solve(row):
    global cnt
    if row >= N:
        cnt += 1
    else:
        for column in range(N):
            chessboard[row] = column    # 행 / 열
            if check(row):              # 1차원 배열의 index를 행, value를 열로 배정.
                solve(row+1)
cnt = 0
solve(0)
print(cnt)