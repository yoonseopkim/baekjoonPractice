N, M = map(int, input().split())

# 원래 배열
arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 Prefix Sum 배열 초기화
P = [[0] * (M+1) for _ in range(N+1)]

# Prefix Sum 배열 계산
for i in range(1, N+1):
    for j in range(1, M+1):
        P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + arr[i-1][j-1]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = P[x][y] - P[i-1][y] - P[x][j-1] + P[i-1][j-1]
    print(result)
