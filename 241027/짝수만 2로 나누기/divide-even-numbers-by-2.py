def a(arr):
    for i, val in enumerate(arr):
        if val % 2 == 0:
            arr[i] //=2



n = int(input())
arr = list(map(int,input().split()))

a(arr) 

for aa in arr:
    print(aa, end=' ')