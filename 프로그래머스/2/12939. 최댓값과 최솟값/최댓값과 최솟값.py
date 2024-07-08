def solution(s):
    ee = s.split()
    li = []
    for eee in ee:
        li.append(int(eee))

    maxy = max(li)
    miny = min(li)
    # return miny, maxy
    # print(f'"{miny} {maxy}"')
    return f'{miny} {maxy}'


    
