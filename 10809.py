import sys
text=sys.stdin.readline().rstrip()
result=[-1] * 26

for i in range(len(text)):
	if result[ord(text[i])-97] == -1:
		result[ord(text[i])-97] = i
	
print(*result)