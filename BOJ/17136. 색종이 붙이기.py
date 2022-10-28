# 17136. 색종이 붙이기
# brute force, backtracking
import sys
sys.stdin = open('17136.txt', encoding='UTF-8')
#
N = 10
board = [list(map(int, input().split())) for _ in range(N)]
cards = [0] + [5]*5

# size 만큼 색종이로 붙일 수 있는지 확인
def check_size(startpoint, cur_size):
    # 색종이를 모두 붙였다면
    if cards[cur_size] < 1:
        return False
    y, x = startpoint
    for row in range(cur_size):
        for col in range(cur_size):
            if 0<=y+row<N and 0<=x+col<N:
                if board[y+row][x+col] != 1:
                    return False
            else:
                return False
    return True

def solve(res):
    global minV
    # 이미 최소값보다 많은 색종이를 사용했을 경우
    if minV < len(res):
        return
    # 색종이를 모든 칸에 붙였는지 확인
    no_left = 1
    for y in range(N):
        if sum(board[y]) != 0:
            no_left = 0
    if no_left:
        if minV > len(res):
            minV = len(res)
        return

    for sy in range(N):
        for sx in range(N):
            if board[sy][sx] == 1:
                bool = 0
                for size in range(5, 0, -1):
                    if check_size((sy,sx), size):
                        # 색종이를 붙인다. (0으로 전환)
                        for row in range(size):
                            for col in range(size):
                                board[sy+row][sx+col] = 0
                        cards[size] -= 1
                        # 여기
                        solve(res + [size])
                        # 색종이를 뗀다. (1로 전환)
                        for row in range(size):
                            for col in range(size):
                                board[sy+row][sx+col] = 1
                        cards[size] += 1
                        bool = 1
                if bool == 0:
                    return
                # 루프 탈출을 위한 return.
                # 이 return이 없으면 같은 색종이 조합을 순서만 바꿔서 여러번 탐색하게 된다.
                # 색종이 5장의 모든 경우를 보기 때문에,
                # 좌측 최상단의 최초 1만 탐색하고 함수를 종료해줘도, 모든 색종이 조합을 볼 수 있다.
                return

minV = 10**5
solve([])

if minV == 10**5:
    print(-1)
else:
    print(minV)