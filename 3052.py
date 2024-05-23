diff = set()
for i in range(10):
    n = int(input())
    diff.add(n % 42)

print(len(diff))