n = int(input())
aa = 1
def a(n):
    if n ==0:
        return
    print(n, end = ' ')
    a(n-1)
    print(n, end = ' ')

a(n)