#1206. View
import sys
sys.stdin = open("input.txt")
T = 10
#
for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, list(input().split())))

    room_cnt = 0
    for x in range(len(buildings)):
        if buildings[x] > 0:
            for v in range(buildings[x], 0, -1):
                if buildings[x-2] < v and buildings[x-1] < v and buildings[x+1] < v and buildings[x+2] < v:
                    room_cnt += 1
                else:
                    break
    print(f'#{test_case} {room_cnt}')