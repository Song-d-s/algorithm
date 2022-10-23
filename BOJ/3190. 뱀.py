# 3190. 뱀
import sys
sys.stdin = open('3190.txt')
from pprint import pprint
#
from collections import deque

N = int(input()); K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]

L = int(input())
movement = []
for _ in range(L):
    X, C = input().split()
    movement.append((int(X), C))
movement.sort(key=lambda x: x[0], reverse=True)

board = [[0]*N for _ in range(N)]
for apple in apples:
    y, x = apple
    board[y-1][x-1] = 2 # 2: 사과
    

delta = deque([(0,1),(1,0),(0,-1),(-1,0)])

snake = deque([(0,0)])

board[0][0] = 1

time = 0
it_is_alive = True
while it_is_alive:
	time += 1
	# print(delta, delta[0])

	head_y, head_x = snake[0]
	tail_y, tail_x = snake[-1]

	# 방향 선정
	dy, dx = delta[0]
	ny, nx = head_y+dy, head_x+dx
	# print(time, ny, nx)

	# 이동
	if 0<=ny<N and 0<=nx<N:
		if board[ny][nx] == 1:
			it_is_alive = False
		else:
			# 사과 먹기
			if board[ny][nx] != 2:
				board[tail_y][tail_x] = 0
				snake.pop()
			snake.appendleft((ny, nx))
			board[ny][nx] = 1
	else:
		it_is_alive = False

	# 방향 전환
	if movement:
		this_time, LR = movement.pop()
		if time == this_time:
			if LR == 'D':
				delta.rotate(-1)
			else:
				delta.rotate(1)
		else:
			movement.append((this_time, LR))
	# pprint(board)

print(time)
