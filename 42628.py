
from heapq import heappop, heappush, heapify

def solution(operations):
    heap = []
    
    for operation in operations:
        cmd, data = operation.split()
        
        if cmd == "I":
            heappush(heap, int(data))
        elif cmd == "D" and data == "-1":
            if not heap:
                continue
            heappop(heap)
        else:
            if not heap:
                continue
            max_num = max(heap)
            heap.remove(max_num)
            
            heapify(heap)
            
    if not heap:
        return [0,0]
    elif len(heap) == 1:
        return [heap[0], heap[0]]
    else:
        min_num=heappop(heap)
        max_num=max(heap)
        return [max_num, min_num]
