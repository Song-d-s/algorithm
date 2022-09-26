# 2382. [모의 SW 역량테스트] 미생물 격리
import sys
sys.stdin = open('2382.txt')
#
def print_arr(arr):
    for a in arr:
        print(a)
#
T = int(input())

dy = [0,-1, 1, 0, 0]
dx = [0,0, 0, -1, 1]
rev = [0,2, 1, 4, 3]

for tc in range(1, T+1):
    # 입력
    N, M, K = map(int, input().split())
    ARR = [list(map(int, input().split())) for _ in range(K)]

    for m in range(M):
        for k in range(K):
            d = ARR[k][3]
            ARR[k][0] = ARR[k][0] + dy[d]
            ARR[k][1] = ARR[k][1] + dx[d]

            if ARR[k][0] == 0 or ARR[k][0] == N-1 or ARR[k][1] == 0 or ARR[k][1] == N-1:
                ARR[k][2] //= 2
                ARR[k][3] = rev[ARR[k][3]]
            
        ARR.sort()
        pre = 0
        for k in range(1, K):
            if ARR[k][2] == 0:
                continue
            if ARR[k][0] == ARR[pre][0] and ARR[k][1] == ARR[pre][1]:
                ARR[k][2] += ARR[pre][2]
                ARR[pre][2] = 0
            pre = k
    
    res = 0
    for k in range(K): res += ARR[k][2]
    print(f'#{tc} {res}')

'''
# 2382. 미생물 격리
# 교수님 풀이

for tc in range(1, TC+1):
    ARR = 
    for t in range(M):
        for k in ARR[k]:
            if k의 미생물이 0이면: continue
            #1 좌표 이동
            #2
            if 벽이면:
                미생물 값을 반으로
                #방향전환
                d = rev[d]
        
        ARR.sort()
        pre = 0
        for k in range(1, k):
            if k의 미생물이 0이면: continue
            if pre의 좌표와 i번째의 좌표가 같으면:
                ARR[k]의 미생물 내용에 누적.
                pre의 미생물은 0
            pre = i

'''
'''
for t in range(M):
    for k in range(K):
        # 1 좌표 이동
        d = ARR[k][3]
        ARR[k][0] = ARR[K][0] + dr[d]
        ARR[k][1] = ARR[K][1] + dc[d]

        # 벽이면
        if ARR[k][0] == 0 or ARR[k][0] == N-1 or ARR[k][1] == 0 or ARR[k][1] == N-1:
            # 미생물 값을 반으로
            ARR[k][2] //= 2
            # 방향 전환
            ARR[k][3] = rev[ARR[k][3]]
    # 정렬
    ARR.sort()
    pre = 0

    # 동일 좌표가 있는지 확인하여 통합
    for k in range(1, K):
        if ARR[k][2] == 0: continue
        # pre의 좌표와 k번째의 좌표가 같으면
        if ARR[k][0] == ARR[pre][0] and ARR[k][1] == ARR[pre][1]:
            ARR[k][2] += ARR[pre][2]
            ARR[pre][2] = 0
        pre = k

'''