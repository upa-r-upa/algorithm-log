def solution(n):
    i = 1
    
    while 6 * i % n != 0:
        i=i+1
        
    return i