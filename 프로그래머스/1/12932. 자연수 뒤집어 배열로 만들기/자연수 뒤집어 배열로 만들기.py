def solution(n):

    answer = []
    while n > 0:
        answer.append(n % 10)
        n //= 10
    return answer



n = 12345
print(solution(n))