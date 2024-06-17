stack = []
raser=input()
result=0

for i in range(len(raser)):
	if raser[i] == "(":
		stack.append(raser[i])
	else:
		if raser[i - 1] == "(":
			stack.pop()
			result += len(stack)
		else:
			stack.pop()
			result += 1

print(result)
		