import sys
input = sys.stdin.read
# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
stack = []
data = input().split()
n = int(data[0])

index = 1
res = []

for i in range(n):
    # command = input().split()
    command_type = int(data[index])
    if command_type ==1:
        a = int(data[index + 1])
        stack.append(a)
        index += 2
    if command_type ==2:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
        index += 1
    if command_type ==3:
        print(len(stack))
        index += 1
    if command_type == 4:
        if not stack:
            print(1)
        else:
            print(0)
        index += 1
    if command_type == 5:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
        index += 1

