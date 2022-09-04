# 13549. 숨바꼭질 3
from collections import deque
maxVal = 10**6+1

# 위치*2를 모두 큐에 넣는 방법은 시간 초과.

def bfs(ini):
    Q.append(ini)
    visited[ini] = 0
    while Q:
        posNow = Q.popleft()
        if posNow == K:                         # 동생 발견.
            return visited[posNow]
        for idx in range(3):
            posNew, time = move(posNow, idx)
            newTime = visited[posNow] + time    # 방문 검사를 하되 최소값을 얻을 수 있도록 비교.
            if 0<=posNew<maxVal and visited[posNew] > newTime:
                visited[posNew] = newTime
                if time:
                    Q.append(posNew)
                else:                           # 최단시간을 구하기 위해서,
                    Q.appendleft(posNew)        # 0초가 걸리는 과정을 우선적으로 큐에 삽입.

def move(pos, idx):
    if idx == 0:
        return pos - 1, 1                       # +1 을 먼저 수행했을 경우 오답인 이유를 모르겠다.
    elif idx == 1:                              # 반례 : 4 6
        return pos + 1, 1
    else:
        return pos * 2, 0                       # BFS인데 값이 다르게 증가한 다는 점에 유의.

N, K = map(int, input().split())
visited = [maxVal for _ in range(maxVal)]       # 엄청 큰 수를 넣어준다.
Q = deque()

print(bfs(N))