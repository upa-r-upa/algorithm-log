n,m=map(int, input().split())
cards=sorted(list(map(int, input().split())))

max_sum = 0

for i in range(n-2):
	for j in range(i+1,n-1):
		for k in range(j+1,n):
			num = cards[i] + cards[j] + cards[k]
			if m < num:
				break
				
			if max_sum < num:
				max_sum = num
				
print(max_sum)