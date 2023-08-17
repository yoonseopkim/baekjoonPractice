N, M = map(int,input().split())
arr = list(map(int,input().split()))
left=0
right = 0
count = 0

while left <= right and right <= N:
    summ = sum(arr[left:right])
    if summ < M:
        right += 1
    elif summ > M:
        left += 1
    else:
        count +=1
        right +=1

print(count)


