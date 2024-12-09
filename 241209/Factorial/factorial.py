import sys
sys.setrecursionlimit(10**5)

def a(n):
    if n ==0:
        return 1
    return n * a(n-1)

n = int(input())
print(a(n))