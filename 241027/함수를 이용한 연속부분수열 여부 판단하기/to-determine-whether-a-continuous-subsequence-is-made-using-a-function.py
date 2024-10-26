def c(n1,n2,a,b):
    tmp = []
    tmp1 = []
    pnt = 0
    life = n2
    for i in range(n1):
        if pnt < n2:
            if b[pnt] == a[i]:
                tmp.append(a[i])
                tmp1.append(b[pnt])
                pnt += 1
    # print(tmp, tmp1)
    if tmp and tmp1 and len(tmp)>1 and len(tmp1) > 1:
        if tmp == tmp1:

            return 'Yes'
    return 'No'

n1,n2 = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(c(n1,n2,a,b))