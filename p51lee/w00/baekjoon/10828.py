from sys import stdin

op_list = []
for _ in range(int(stdin.readline())):
    op_list.append(stdin.readline().strip())

stack = []
for op in op_list:
    if op.startswith("push"):
        stack.append(op[5:])
    elif op.startswith("pop"):
        if stack:
            print(stack.pop())
        else:
            print("-1")
    elif op.startswith("size"):
        print(len(stack))
    elif op.startswith("empty"):
        if stack:
            print("0")
        else:
            print("1")
    elif op.startswith("top"):
        if stack:
            print(stack[-1])
        else:
            print("-1")
