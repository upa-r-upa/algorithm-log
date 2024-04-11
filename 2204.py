import sys

result = []

while True:
    s = sys.stdin.readline().rstrip()

    if s.isdigit():
        if int(s) == 0:
            break;
        elif len(result) != 0:
            print(sorted(result, key=lambda x: x.lower())[0])
            result = []

    else:
        result.append(s)
	
print(sorted(result, key=lambda x: x.lower())[0])