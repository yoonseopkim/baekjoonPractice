def solution(people, limit):
#     limit > people의 아무 구성요소

    answer = 0 # 구명보트 개수
    p = sorted(people)
#     가장 가볍고 무거운 사람 구분
    l, r = 0, len(p) - 1 # -1 안해주면 범위를 벗어나버림
    while l <= r:
#         일단 사람 한명을 테운다.
#         초과하면 무거운 사람만
        if p[l] + p[r] > limit:
            answer += 1
            r -= 1
        else:
            answer += 1
            r-= 1
            l += 1
# 그렇지 않으면 두사람 모두
            
        
    return answer