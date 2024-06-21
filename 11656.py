import sys

s=sys.stdin.readline().rstrip()
result=[]

for i in range(len(s)):
	result.append(s[i:])
	
print(*sorted(result),sep="\n")