
n = int(input())
# 두개의 스택으로 커서 왼쪽 이동과 오른쪽 이동을 구현한다.

res = []
for i in range(n):
    # 커서 왼쪽 이동은 왼쪽 스택, 커서 오른쪽 이동은 오른쪽 스택으로 넣는다.
    left_word = []
    right_word = []
    word = input()
    #명령어에 해당하는 키를 제외한 문자는 왼쪽 스택에 일단 담는다.
    for w in word:
        if w == '-':
            #현재 커서에 해당하는 거를 빼야하므로
            if left_word:
                #예외처리 해야함
                left_word.pop()
        elif w == '<':
            #예외처리
            if not left_word:
                continue
            #전에 커서로 이동한다는 기준
            right_word.append(left_word.pop())
        elif w == '>':
            if not right_word:
                continue
            left_word.append(right_word.pop())
        # 아무 것도 없을경우 왼쪽 스택에 집어넣는다.
        else:
            left_word.append(w)
    res.append((''.join(left_word) +''.join(reversed(right_word))))

for i in range(len(res)):

    print(res[i])
