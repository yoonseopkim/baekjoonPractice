def aa(a1,a2):
    res = 0
    for i in range(a1,a2+1):
        res += a[i]
    return res

n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))

for _ in range(m):
    a1, a2 = map(int,input().split())
    print(aa(a1,a2))