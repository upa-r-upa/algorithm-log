def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    
    for i in range(len(sorted_phone_book)-1):
        if sorted_phone_book[i+1].startswith(sorted_phone_book[i]):
            return False
    
    return True
    
# 정렬을 하게 되면, 인접한 것들끼리 앞뒤로 묶이게 됨.
# 그래서 현재 요소를 기준으로 +1 것이 startswith로 검사했을때 맞다면 false, 아니라면 true