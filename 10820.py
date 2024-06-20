import sys

reading=True
result=[]

while reading:
	text = sys.stdin.readline().rstrip("\n")

	if text == "":
		reading = False
		break
		
	result.append([0] * 4)
	
	for i in range(len(text)):
		if text[i].isdigit():
			result[-1][2] += 1
		elif text[i] == " ":
			result[-1][-1] += 1
		elif text[i].isupper():
			result[-1][1] += 1
		else:
			result[-1][0] += 1
			
	print(*result[-1])
	