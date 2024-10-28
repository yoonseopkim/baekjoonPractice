n = int(input())
def a(n):
    if n ==0:
        return
    a(n-1)
    print("HelloWorld")

a(n)