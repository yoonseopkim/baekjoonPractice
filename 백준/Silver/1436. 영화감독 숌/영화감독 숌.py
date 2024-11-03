def sol(num):
    return '666' in str(num)

n = int(input())

cnt = 0
num = 666

while True:
    if sol(num):
        cnt += 1

    if cnt == n:
        print(num)
        break

    num += 1

