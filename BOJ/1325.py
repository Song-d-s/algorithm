#1325. 효율적인 해킹
from sys import stdin
from collections import deque #queue 자료형

N, M = map(int, stdin.readline().rstrip().split())

trustlist = [[] for _ in range(N+1)]
for _ in range(M):
    a , b = map(int, stdin.readline().rstrip().split())
    trustlist[b].append(a)

def bfs(com_number): #bfs
    queue = deque([com_number])
    counts = 1
    checked = [False for _ in range(N+1)]
    checked[com_number] = True
    while queue:
        x = queue.popleft()
        for i in trustlist[x]:
            if not checked[i]:
                checked[i] = True
                queue.append(i)
                counts += 1
    return counts

results = list()
for i in range(1, N+1):
        results.append(bfs(i))

M = max(results)
for i in range(len(results)):
    if M == results[i]:
        print(i+1, end=' ')