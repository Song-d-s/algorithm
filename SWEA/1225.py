# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
# queue
import sys
# sys.stdin = open('01.txt')
# 시작
def enqueue(item):
    global rear
    rear = rear + 1
    Q[rear] = item

def dequeue():
    global front
    front = front + 1
    return Q[front]

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    print(f'#{tc}', end=' ')
    # queue 만들기.
    N = 10 ** 6
    Q = [-1] * N
    front = rear = -1
    # queue 입력 받기.
    for idx in map(int, input().split()): enqueue(idx)
    nbrs = 8
    idx = 0
    x = 1
    while x > 0:
        idx += 1
        if idx == 6: idx = 1
        x = dequeue() - idx  # queue front에서 디큐.
        if x <= 0: x = 0
        enqueue(x)  # queue rear에 인큐.
    for idx in range(nbrs):
        print(dequeue(), end=' ')
    print()
