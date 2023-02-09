"""
여행경로
코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS)
"""
# 입력
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] # ["ICN", "JFK", "HND", "IAD"]

from collections import defaultdict
def solution(tickets):
    def init():
        routes = defaultdict(list)
        for dep, des in tickets:
            routes[dep].append(des)            
        return routes
    
    def dfs():
        stack = ["ICN"]
        path = []
        while stack:
            top = stack[-1]
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]

    routes = init()
    for each in routes:
        routes[each].sort()

    answer = dfs()
    return answer

print(solution(tickets))