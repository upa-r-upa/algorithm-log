import sys

canvas = [[0] * 100 for _ in range(100)]
n=int(sys.stdin.readline().rstrip())

for i in range(n):
    left_x, left_y = map(int, sys.stdin.readline().rstrip().split())

    for j in range(10):
        for k in range(10):
            canvas[left_x+j][left_y+k] = 1

result = 0

for cell in canvas:
    result += sum(cell)

print(result)