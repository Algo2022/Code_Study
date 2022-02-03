def solution(number, k):
    l = len(number)
    stack1 = list(map(int, number))
    stack1.reverse()
    stack2: list = []

    while l > 0 or k > 0:
        if not stack2:
            stack2.append(stack1.pop())
            l -= 1
        elif stack1 == [] and k > 0:
            stack2.pop()
            k -= 1
        elif stack1[-1] > stack2[-1] and k > 0:
            stack2.pop()
            k -= 1
        else:
            stack2.append(stack1.pop())
            l -= 1

    return ''.join([str(n) for n in stack2])