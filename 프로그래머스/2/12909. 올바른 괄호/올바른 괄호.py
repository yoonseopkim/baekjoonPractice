def solution(s):
    # ( 이게 나오면 스택에 넣고 )이게 나오면 스택에서 꺼내서  비교하면 될듯
#     처음에  ) 이거 나오면 바로 펄스
    stack = []


    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack
        


                    

