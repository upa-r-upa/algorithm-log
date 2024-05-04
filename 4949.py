import sys

while True:
    stack = []
    cmd = sys.stdin.readline().rstrip()

    if cmd == ".":
        break

    for s in cmd:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")" or s == "]":
            target = "(" if s == ")" else "["
            if len(stack) > 0 and stack[len(stack) - 1] == target:
                stack.pop()
            else:
                stack.append(s)

    if len(stack) > 0:
        print("no")
    else:
        print("yes")