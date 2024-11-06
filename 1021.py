from collections import deque

n, m = map(int, input().split())
item_list = deque(range(1, n + 1))
index_list = map(int, input().split())

count = 0

for index in index_list:
    target_index = item_list.index(index)

    if target_index <= len(item_list) // 2:
        count += target_index
        item_list.rotate(-target_index)
    else:
        count += len(item_list) - target_index
        item_list.rotate(len(item_list) - target_index)
    
    item_list.popleft()

print(count)
