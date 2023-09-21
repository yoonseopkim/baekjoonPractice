n = int(input())
person = []
for _ in range(n):
    age, name = input().split()
    person.append((int(age), name))
sorted_person = sorted(person, key=lambda x: x[0])
for i in sorted_person:
    print(i[0], i[1])
