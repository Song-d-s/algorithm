# 10993. 별 찍기 - 18
N = int(input())
#
def print_arr(arr):
    for each in arr:
        # 출력 공백 제거
        print(''.join(each).rstrip())

def solve(curN, start):
    # 1 까지 진행
    if curN < 1:
        return

    # 방향 설정
    direction = 1
    if curN%2: direction = -1

    w = width[curN]
    h = start
    # 첫 줄
    l = w//2
    for step in range(center-l,center+l+1):
            field[start][step] = '*'
    # 진행
    w -= 2
    h += direction
    for step in range(height[curN]-1):
        l = w//2
        field[h][center-l] = '*';
        field[h][center+l] = '*'
        h += direction; w -= 2

    # 다음
    if curN%2:
        solve(curN-1, start-height[curN]//2)
    else:
        solve(curN-1, start+height[curN]//2)

# N 에 따른 높이, 너비값
height = [0,1]
width = [0,1]
for n in range(2, N+1):
    height.append((height[n-1])*2+1)
    width.append((width[n-1]+2)*2-1)

field = [[' ']*width[N] for _ in range(height[N])]

# 시작점 설정
s = 0
if N%2: s = height[N]-1

center = width[N]//2

solve(N, s)
print_arr(field)

