a, b = map(int, input().split())
m = int(input())
a_digits = list(map(int, input().split()))

def num_to_decimal(uni, nums):
    decimal = 0
    rev_nums = nums[::-1]

    for i in range(len(rev_nums)):
        decimal = decimal + (uni ** i) * rev_nums[i]

    return decimal


def decimal_to_unit_num(decimal, uni):
    stack = []
    while decimal > 0:
        stack.append(str(decimal % uni))
        decimal = decimal // uni
    
    return " ".join(stack[::-1])

result = num_to_decimal(a, a_digits)
result = decimal_to_unit_num(result, b)

print(result)