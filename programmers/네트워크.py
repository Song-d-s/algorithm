"""
네트워크
코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS)
"""
# 입력
# n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]] #2
n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]] #1

def solution(n, computers):
    visited = [0 for x in range(n)]

    def dfs(node):
        visited[node] = 1
        for idx, status in enumerate(computers[node]):
            if status==1 and idx != node and visited[idx] == 0:
                dfs(idx)
            
    answer = 0
    for x in range(n):
        if visited[x]==0:
            answer += 1
            dfs(x)

    return answer

print(solution(n, computers))