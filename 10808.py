import sys
text=sys.stdin.readline().rstrip()
result=[0] * 26
standard=ord("a")

for i in range(len(text)):
	result[ord(text[i])-standard] += 1
	
print(*result)