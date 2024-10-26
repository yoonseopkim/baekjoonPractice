def miny(*a):
    miny1 = min(*a)
    return miny1
n = tuple(map(int,input().split()))
print(miny(n))