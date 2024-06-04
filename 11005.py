n,b=map(int, input().split())

decimal = n
remains = []

while decimal != 0:
    remains.append(decimal%b)
    decimal = decimal // b


for i in range(len(remains)):
    num = remains[len(remains) - 1 - i]
    
    if num > 9:
        print(chr(65-10+num), end="")
    else:
        print(num, end="")