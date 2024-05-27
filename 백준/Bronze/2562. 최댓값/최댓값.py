stack = []
for i in range(9):
    n = int(input())
    stack.append(n)

max_n = max(stack)
index_n = stack.index(max_n) + 1
print(max_n)
print(index_n)
