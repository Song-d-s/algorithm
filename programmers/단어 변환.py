"""
단어 변환
코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS)
"""
# 입력
# begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"] # 4
begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log"] # 0

from collections import deque

def solution(begin, target, words):
    if target not in words: return 0
    
    def compare(ori, tar):
        cnt = 0
        for idx in range(len(ori)):
            if ori[idx] != tar[idx]: cnt += 1
        return True if cnt == 1 else False

    visited = [0 for x in range(len(words))]
    answer = 0
    
    Q = deque()
    for idx, each in enumerate(words):
        if compare(begin, each):
            visited[idx] = 1
            Q.append(idx)

    while Q:
        a = Q.popleft()
        A = words[a]
        if A == target:
            answer = visited[a]
            break
        for b, B in enumerate(words):
            if compare(A, B) and visited[b] < visited[a]:
                visited[b] = visited[a] + 1
                Q.append(b)

    return answer

# 결과
print("")
print(solution(begin, target, words))