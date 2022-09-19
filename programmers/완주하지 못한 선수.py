# 완주하지 못한 선수
# 코딩테스트 연습 > 해시
# 입력
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
# 시작
def solution(P, C):
    runner = dict()
    for p in P:
        if p in runner:
            runner[p] += 1
        else: runner[p] = 1
    for c in C:
        runner[c] -= 1
        if runner[c] == 0:
            runner.pop(c)
    for s in runner.keys():
        return s
# 테스트
print(solution(participant, completion))