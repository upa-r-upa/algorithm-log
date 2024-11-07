import math

def solution(progresses, speeds):
    work_days = []
    result = []
    
    for index in range(len(progresses)):
        days =  math.ceil((100 - progresses[index]) / speeds[index])
        work_days.append(days)
    
    i = 0
    while i < len(work_days):
        j = i
        
        while j+1 < len(work_days) and work_days[i] >= work_days[j+1]:
            j += 1
        
        result.append(j-i+1)
        
        i = j+1
    
    return result