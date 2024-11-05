def pop_first_y_item(matrix, y):
    for x in range(len(matrix)):
        if matrix[x][y] != 0:
            item = matrix[x][y]
            matrix[x][y] = 0
            
            return item
        
    return 0

def solution(board, moves):
    count = 0
    stack = []
    
    for move in moves:
        toy = pop_first_y_item(board, move - 1)
                    
        if toy == 0:
            continue
        
        if stack and stack[-1] == toy:
            stack.pop()
            count += 2
        else:
            stack.append(toy)
    
    return count
    