# 1074. Z
# 재귀함수
N, r, c = map(int, input().split())

field = [[0]*2 for _ in range(2)]
cnt = 0
						# 4등분의 첫좌표값 구해서 재귀처리.
def func(sy, sx, N): 	# 시작 좌표 x/y , N 제곱.
	global cnt
	
	if N == 1:
		for y in range(2):
			for x in range(2):
				if sy+y == r and sx+x == c:
					print(cnt)
					return
				cnt += 1
	else:
		N -= 1
		width = 2**N
		for y in range(2):
			for x in range(2):
				if r <= sy+((y+1)*width)-1 and c <= sx+((x+1)*width)-1:
					func(sy+(y*width), sx+(x*width), N)
					return
				else:
					cnt += width**2

func(0, 0, N)