def solution(n):
    tmp = []
    answer = 0
    while n > 0:
        a = n % 10
        tmp.append(a)
        n //= 10
    tmp.sort(reverse=True)
    answer = ''.join(map(str,tmp))
    return int(answer)