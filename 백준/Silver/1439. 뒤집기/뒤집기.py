s = input().strip()
current = s[0]
count = 0
for i in s[1: ]:
    if current != i:
        count +=1
        current = i
print( count // 2 + count % 2 )


