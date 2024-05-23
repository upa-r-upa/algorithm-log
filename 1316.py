from sys import stdin

n = int(stdin.readline().rstrip())
count = 0

for _ in range(n):
    word = stdin.readline().rstrip()
    used_chars = set()
    last_char = None
    is_group = True

    for char in word:
        if char in used_chars and last_char != char:
            is_group = False
            break

        used_chars.add(char)
        last_char = char

    if is_group:
        count += 1

print(count)