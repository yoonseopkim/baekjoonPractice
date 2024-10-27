n = int(input())
li = list(map(int,input().split()))

def a(li):
    for i in range(n):
        li[i] = abs(li[i])
    return li

print(*a(li))