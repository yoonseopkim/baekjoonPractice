def solution(n):
    answer = 0
#     1부터 늘어나야 . 할수
 
    for start in range(1, n+1):
        sum1 = 0
        for j in range(start, n+1):
            sum1 += j
            if sum1 == n:
                answer += 1
                break
            elif sum1 > n:
                break
            
    return answer