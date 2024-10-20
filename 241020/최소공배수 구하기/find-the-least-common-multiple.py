n,m = map(int,input().split())
a = 1
while True:
    if a % n==0 and a % m ==0:
        break
    else:
        a += 1

print(a)