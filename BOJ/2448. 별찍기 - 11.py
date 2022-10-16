# 2448. 별찍기 - 11
N = int(input())    # N = 3*2**k
#
def print_arr(arr):
    for each in arr:
        print(''.join(each))
#
field = [[' ']*(N*2) for _ in range(N)]
# 재귀
def make_triangle(k, sy, sx):
    if k <= 3:
        for y in range(2):
            field[sy+y][sx-y] = '*'
            field[sy+y][sx+y] = '*'
        for x in range(3):
            field[sy+2][sx-x] = '*'
            field[sy+2][sx+x] = '*'
        return
    make_triangle(k//2, sy, sx)
    make_triangle(k//2, sy+k//2, sx-k//2)
    make_triangle(k//2, sy+k//2, sx+k//2)
make_triangle(N, 0, N-1)

print_arr(field)