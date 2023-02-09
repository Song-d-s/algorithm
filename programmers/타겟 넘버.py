# 타겟 넘버
# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS)

# 입력
# numbers, target = [1, 1, 1, 1, 1], 3    # 5
numbers, target = [4, 1, 2, 1], 4       # 2

def solution(numbers, target):
    end = len(numbers)
    global ans
    ans = 0

    def rec(res, pos):
        global ans
        if pos >= end:
            if res == target:
                ans += 1
            return
        rec(res + numbers[pos], pos + 1)
        rec(res - numbers[pos], pos + 1)

    rec(0,0)

    return ans

print(solution(numbers, target))