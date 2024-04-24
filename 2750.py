def swap(arr, idx_a, idx_b):
    temp = arr[idx_a]

    arr[idx_a] = arr[idx_b]
    arr[idx_b] = temp

n = int(input())
result = [int(input()) for i in range(n)]

for i in range(n):
    min_i = i
    for idx in range(i+1,n):
        if result[min_i] > result[idx]:
            min_i = idx
    if min_i != i:
        swap(result, i, min_i)

print(*result, sep="\n")