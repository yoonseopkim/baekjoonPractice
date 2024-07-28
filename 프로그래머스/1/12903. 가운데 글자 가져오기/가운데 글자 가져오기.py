def solution(s):
    len_s = len(s)
    mid = len_s // 2
    for i in range(len_s):
        if len_s % 2 == 0 : # 짝수이면 2개수 반환
            return f'{s[mid-1]}{s[mid]}'
        else:
            return s[mid]
