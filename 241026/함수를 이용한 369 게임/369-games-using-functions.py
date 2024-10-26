def sam(a,b):
    res = 0
    for i in range(a,b+1):
        if i %3 == 0 or issam(i):
            res += 1
    return res

def issam(i):
    while i > 0:
        tmp = i //10
        if tmp %3 ==0:

            return True

a,b = map(int,input().split())
print(sam(a,b))