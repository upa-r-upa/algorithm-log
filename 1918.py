import sys

formula=sys.stdin.readline().rstrip()
operators=[]
result=[]

for i in range(len(formula)):
    if formula[i] == "(":
        operators.append([])
    elif formula[i] == ")":
        while operators[-1]:
            result.append(operators[-1].pop())

        operators.pop()
    elif formula[i].isalpha():
        result.append(formula[i])
    else:
        if len(operators) == 0:
            operators.append([])

        if formula[i] == "+" or formula[i] == "-":
            while operators[-1]:
                result.append(operators[-1].pop())

            operators[-1].append(formula[i])
        else:
            if len(operators[-1]) >= 2 or (operators[-1] and (operators[-1][-1] == "*" or operators[-1][-1] == "/")):
                result.append(operators[-1].pop())

            operators[-1].append(formula[i])

if operators:
    result.extend(reversed(operators[-1]))

print(*result,sep="")