def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        idx = i+1
        
        while idx < len(prices) and prices[idx] >= prices[i]:
            if idx + 1 >= len(prices):
                break
            idx += 1
            
        answer.append(idx-i)
        
    answer.append(0)
        
    return answer