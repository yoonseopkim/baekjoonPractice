n = int(input())

def a(n):
    if n == 1:
        return n
    return a(n-1) + n


print(a(n))