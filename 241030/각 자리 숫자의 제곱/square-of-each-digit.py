n = int(input())

def a(n):
    if n < 10:
        return n** 2
    return a(n // 10) + (n%10) ** 2

print(a(n))