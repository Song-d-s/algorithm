# 4366. 정식이의 은행업무
import sys
sys.stdin = open('4366.txt')
#
T = int(input())
for tc in range(1, T+1):
    bin_arr, tri_arr = list(input()), list(input())

    print(f'#{tc}', end = ' ')
    bin_res = set()
    for idx in range(1, len(bin_arr)):
        bin_arr[idx] = str(int(bin_arr[idx]) ^ 1)
        bin_res.add(int(''.join(bin_arr), 2))
        bin_arr[idx] = str(int(bin_arr[idx]) ^ 1)
    
    tri_res = set()
    for idx in range(len(tri_arr)):
        ori_v = tri_arr[idx]
        for v in range(3):
            if v != ori_v: tri_arr[idx] = str(v)
            if tri_arr[0] != '0':
                tri_res.add(int(''.join(tri_arr), 3))
        tri_arr[idx] = ori_v

    print(*(bin_res & tri_res))
            
'''
# 교수님 풀이
def check():
    이진수의 i 번째가 틀린 경우
    for i in range(N):
        삼진수의 j번째가 틀린 경우
        for j in range(M):
            b = 이진수의 i번째 데이터를 변경하고 0 <-> 1
                b[i] = (b[i]+1)%2
            t = 삼진수의 i번째 데이터를 변경해서 0: 1,2 / 1: 2,3 / 3: 0,1
                for k in [1,2]:
                    t[j] = (t[j]+k) % 3
                    if b의 십진수 == t의 십진수:
                        return b의 십진수
    return -1
'''