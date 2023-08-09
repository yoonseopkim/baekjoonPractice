N = int(input())
P = list(map(int, input().split()))
P.sort()
# 각 사람이 돈을 인출하는데 걸리는 시간의 합
total_time = 0
wait_time = 0

for time in P:
    wait_time = wait_time + time
    total_time = total_time + wait_time
print(total_time)

