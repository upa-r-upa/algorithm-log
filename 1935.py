import sys
input = sys.stdin.readline

n=int(input().rstrip())
notations=input().rstrip()
nums=[int(input().rstrip()) for _ in range(n)]
stack=[]

for i in range(len(notations)):
	if notations[i].isalpha():
		stack.append(nums[ord(notations[i])-ord("A")])
	else:
		b=stack.pop()
		a=stack.pop()
		r=eval(f"{a}{notations[i]}{b}")
		stack.append(r)
		
print(f"{stack[0]:.2f}")
		