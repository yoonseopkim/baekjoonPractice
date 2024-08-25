def solution(s):
#     이미 리스트
    a = list(map(int, s.split()))
    miny = min(a)
    maxy = max(a)

    answer = f'{miny} {maxy}'
    return answer
