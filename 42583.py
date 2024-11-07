def solution(length, weight, weights):
    seconds = 0
    total = 0
    trucks = []
    
    while weights or trucks:
        seconds += 1
            
        for i in range(len(trucks)):
            trucks[i][1] -= 1
            
        if trucks and trucks[0][1] == 0:
            total -= trucks[0][0]
            trucks.pop(0)
            
        if weights and total + weights[0] <= weight and len(trucks) < length:
            total +=  weights[0] 
            trucks.append([weights.pop(0), length])
    
    return seconds