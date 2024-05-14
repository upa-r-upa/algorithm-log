import sys

students = list(range(1,31))

for i in range(28):
    num = int(sys.stdin.readline().rstrip())
    students.remove(num)

print(*students, sep="\n")