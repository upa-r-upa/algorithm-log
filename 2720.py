import sys

readline = sys.stdin.readline
t=int(readline().rstrip())
coins=[25,10,5,1]

for _ in range(t):
	c = int(readline().rstrip())
	
	for coin in coins:
		count = c // coin
		c -= count * coin
		
		print(count, end=" ")
		
	print("")