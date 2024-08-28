def solution(n):
    answer = 0
    if n<= 2:
        return n
    dp = [0] * (n+ 1)
    dp[1], dp[2] = 1, 2
#     3부터 해야 됌
    for i in range(3, n +1):
#         모듈려 연산 누락
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]