def c(n1,n2,a,b):
    tmp = []
    tmp1 = []
    for i in range(n1):
        for j in range(n2):
            if b[j] == a[i]:
                tmp.append(a[i])
                tmp1.append(b[j])
    if tmp == tmp1:
        return 'Yes'
    return 'No'

n1,n2 = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(c(n1,n2,a,b))