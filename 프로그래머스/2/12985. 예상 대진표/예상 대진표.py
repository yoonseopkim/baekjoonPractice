def solution(n,a,b):
    answer = 0

    
    while a != b:
        answer += 1
#     한 라운드가 끝날떄마다 수가 반으로 줄어든다 토너먼트라
        a = (a+1) //2
        b = (b+1 ) // 2
    return answer