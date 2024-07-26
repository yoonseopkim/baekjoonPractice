from itertools import combinations
from collections import Counter

def solution(orders, course):
    #문제분석
    #코스요리 == 2가지 이상 단품메뉴
    #최소 2명 이상의 손님에게 주문된 단품요리
    #코스요리 개수가 나오면 메뉴구성이 문자열로 리스트에 담김
    #2*10*10*10=2000 시간복잡도는 고려 x
    #오름차순정렬
    #알고리즘

    #엣지케이스
    #단품요리가 주문된 횟수가 같을경우->모두 배열에 담기
    answer = []

    for course_length in course:
        tmp = []

        #횟수를 하나씩 세는 카운터가 있으면 좋을듯
        for order in orders:
            sorted_order = sorted(order)

            if len(sorted_order) >= course_length:

                combs = list(combinations(sorted_order,course_length))

                for comb in combs:
                    tmp.append(''.join(comb))
                    
        comb_counts = Counter(tmp)

        if comb_counts:
            max_count = max(comb_counts.values())

            if max_count > 1:
                for combo, count in comb_counts.items():
                    if count == max_count:
                        answer.append(combo)



    return sorted(answer)