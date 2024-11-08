from heapq import heappop, heappush, heapify

def solution(scoville, k):
    count = 0
    heapify(scoville)
    
    while len(scoville) > 1 and scoville[0] < k:
        count += 1

        first = heappop(scoville)
        second = heappop(scoville)
        mixed = first + (second * 2)
        
        heappush(scoville, mixed)
    
    return -1 if scoville[0] < k else count 