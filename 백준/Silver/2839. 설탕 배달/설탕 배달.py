N = int(input())
cnt = 0

while N % 5 != 0 and N >= 0:
    N -= 3
    cnt += 1

if N < 0:
    print(-1)
else:
    cnt += N // 5
    print(cnt)
