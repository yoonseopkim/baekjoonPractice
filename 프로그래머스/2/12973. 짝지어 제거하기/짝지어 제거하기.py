def solution(s):
    tmp = []
    for a in s:
        if not tmp: #예외처리
            tmp.append(a)
            
        else:            
            if tmp[-1] == a:
                tmp.pop()
            else:
                tmp.append(a)
    if not tmp:
        return 1
    return 0


