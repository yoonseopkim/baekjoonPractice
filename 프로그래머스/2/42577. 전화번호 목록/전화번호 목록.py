def solution(phone_book):
    phone_book.sort()  #사전순 정렬
    first = phone_book[0]
    for i in range(len(phone_book)):
        if i>0:
            if str(phone_book[i]).startswith(first):
                return False
            else:
                first = phone_book[i]
    return True
                
            


