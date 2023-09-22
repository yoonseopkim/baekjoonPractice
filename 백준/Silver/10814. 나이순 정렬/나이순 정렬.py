n = int(input())
p = []
for _ in range(n):
    age, name = input().split()
    p.append((int(age), name))
p_sorted = sorted(p, key=lambda x: x[0])
for i in p_sorted:
    print(i[0], i[1])
