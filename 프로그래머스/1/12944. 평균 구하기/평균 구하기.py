def solution(arr): 
    answer = 0
    arr_len = len(arr)
    for i in range(arr_len):
        answer += arr[i]
    answer /= arr_len
    return answer