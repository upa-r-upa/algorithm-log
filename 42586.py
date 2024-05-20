def check(progresses, speeds, day):
    return progresses[0] + day * speeds[0] >= 100

def solution(progresses, speeds):
    day = 1
    deploys = [0]
    
    while len(progresses) > 0:
        if check(progresses, speeds, day):
            progresses.pop(0)
            speeds.pop(0)
            deploys[-1] += 1
            
            if len(progresses) != 0 and check(progresses, speeds, day) is False:
                deploys.append(0)
                day = 1
        else:
            day = -(((100 - progresses[0]) / speeds[0]) // -1)
    
    
    return deploys
            