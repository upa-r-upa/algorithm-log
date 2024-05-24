from sys import stdin

matrix=[stdin.readline().rstrip().split() for i in range(9)]
max_pos=None

for i in range(1, 10):
    for j in range(1, 10):
        n = int(matrix[i-1][j-1])

        if max_pos == None or max_pos[0] < n:
            max_pos = [n, i, j]

print(max_pos[0])
print(max_pos[1], max_pos[2])