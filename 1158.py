n,k=map(int, input().split())
idx=0
people=[i for i in range(1,n+1)]
result=[]

while people:
	next_idx=idx+k-1
	if next_idx >= len(people):
		cnt = next_idx // len(people)
		next_idx = next_idx - cnt*len(people)
		
	result.append(people.pop(next_idx))
	if next_idx >= len(people):
		idx = 0
	else:
		idx = next_idx

print("<",end="")
print(*result, sep=", ", end="")
print(">")