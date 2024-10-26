def a(n):
    tmp = 0
    for i in range(1, n+1):
        tmp += i     
    return tmp // 10

n = int(input())
print(a(n))