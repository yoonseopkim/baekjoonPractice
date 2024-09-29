def max_money(n,T,P):
    # dp 이요?
    # 퇴사일인 n + 1 에 맞춤
    dp = [0] * (n + 1)
#미래의 결과를 알고 있기 때문에 항상 최적해 르 ㄹ 보장한다.
    for i in range(n-1, -1 , -1):
        # 퇴사일을 넘어서는 안됌
        if i + T[i] <= n :
        # 최대누적합?
            dp[i] = max( P[i] + dp[i + T[i]] ,   dp[i +1])
        # 퇴사일을 넘을 경우 그냥 그 상담을 넘겨야함
        else:
            dp[i] = dp[i + 1]


    return dp[0]
        # T와 관련된 조건 필요(상담기간이




# 퇴사일
n  = int(input())
# 시간, 상담 비용
T, P = [], []


for _ in range(n):
    time, pay = map(int,input().split())
    T.append(time)
    P.append(pay)

print(max_money(n,T,P))