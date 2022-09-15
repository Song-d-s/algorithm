# 2022 KAKAO TECH INTERNSHIP
# 두 큐 합 같게 만들기
'''입력
queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
queue1 = [1, 1]
queue2 = [1, 5]'''

from collections import deque  # deque를 사용하지 않으면 시간 초과.

def solution(queue1, queue2):
    Q1, Q2 = deque(queue1), deque(queue2)
    answer = -1
    sumQ1, sumQ2 = sum(Q1), sum(Q2)
    if sumQ1 == sumQ2:
        return 0  # 애초에 똑같으면 바로 종료.

    goal = sumQ1 + sumQ2  # 목표치 설정하기.

    if goal % 2:
        return answer  # 홀수 (불가능) 이면 -1 반환 후 바로 종료.
    else:
        goal //= 2

    cnt = 0
    N = len(Q1)
    while sumQ1 != goal:
        cnt += 1
        if sumQ1 < goal and Q2:
            moved = Q2.popleft()
            Q1.append(moved)
            sumQ1 += moved
        elif Q1:
            moved = Q1.popleft()
            Q2.append(moved)
            sumQ1 -= moved
        if sumQ1 == goal:
            return cnt
        if cnt > 3 * N:
            return answer

# print(solution(queue1, queue2))
