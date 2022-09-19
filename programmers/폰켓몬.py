# 폰켓몬
# 코딩테스트 연습 > 해시
# 입력
nums = [3,1,2,3]
nums = [3,3,3,2,2,4]
# nums = [3,3,3,2,2,2]

# 시작

# 1. 정답
def solution(nums):
    choice = len(nums)//2
    nums = set(nums)
    variety = len(nums)
    if choice >= variety:
        return variety
    else:
        return choice

# 3. 재귀 순열로 뽑기 - 시간 초과, 런타임 에러 (16번)
# def solution(nums):
#     R = len(nums)//2
#     nums = list(set(nums))
#     variety = len(nums)
#     if R >= variety: return variety
#     n = len(nums)
#     picked = []
#     start = 0
#     resLen = []
#     def recur(start):
#         if len(picked) == R:
#             # print(picked, end=' ')
#             resLen.append(len(picked))
#             return
#         for idx in range(start, n):
#             picked.append(nums[idx])
#             start += 1
#             recur(start)
#             picked.pop()
#     recur(start)
#     if resLen:
#         return max(resLen)
#     else: return 0

# 2. itertools 시간초과 80점
# from itertools import combinations
# def solution(nums):
#     choice = len(nums)//2
#     nums = set(nums)
#     variety = len(nums)
#     if choice >= variety: choice = variety
#     comb = list(combinations(nums, choice))
#     print(comb)
#     max = 0
#     for c in comb:
#         l = len(c)
#         if l == variety:
#             return l
#         if max < l:
#             max = l
#     return max

# 테스트
# print(solution(nums))