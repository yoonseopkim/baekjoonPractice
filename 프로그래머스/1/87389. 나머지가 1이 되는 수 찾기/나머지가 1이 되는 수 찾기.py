def solution(n):
    for x in range(1, n):  #1부터 해야함 0부터하면 0을 나눌수 없어서
        a = n % x  #나머지 저장
        if a == 1:
            return x