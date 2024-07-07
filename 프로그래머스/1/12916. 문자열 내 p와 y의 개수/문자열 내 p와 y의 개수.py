from collections import Counter
def solution(s):
    a = s.lower()
    cnt1 =0
    cnt2 = 0
    for i in a:
        if i == 'p':
            cnt1 += 1
        elif i == 'y':
            cnt2 += 1
        else:
            continue
    if cnt1 == cnt2:
        return True
    else:
        return False
