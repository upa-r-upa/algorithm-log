import sys
text=sys.stdin.readline().rstrip()
result=[]

for s in text:
	if s.isupper():
		result.append(chr(65+(ord(s)-65+13)%26))
	elif s.islower():
		result.append(chr(97+(ord(s)-97+13)%26))
	else:
		result.append(s)

print(*result,sep="")