a, b = tuple(map(int,input().split()))

def c(a,b):
    if a> b:
        a *= 2
        b += 10
    else:
        b *=2
        a += 10
    return a,b

print(*c(a,b))