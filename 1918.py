import sys
text=sys.stdin.readline().rstrip()
stack=[]
result=[]
priority={"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}

for i in range(len(text)):
	if text[i].isalpha():
		result.append(text[i])
	elif text[i] == "(":
		stack.append("(")
	elif text[i] == ")":
		while stack and stack[-1] != "(":
			result.append(stack.pop())
			
		stack.pop()
	else:
		while stack and priority[stack[-1]] >= priority[text[i]]:
			result.append(stack.pop())
		
		stack.append(text[i])
		
while stack:
	result.append(stack.pop())
		
print(*result,sep="")