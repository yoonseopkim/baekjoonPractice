from collections import Counter
def solution(k, tangerine):
    counter = Counter(tangerine)
    sorted_counter = sorted(counter.values(), reverse = True)
    answer = 0
    sum_cnt = 0
    for cnt in sorted_counter:

        sum_cnt += cnt
        answer += 1
        if sum_cnt >=k:
            break
    return answer