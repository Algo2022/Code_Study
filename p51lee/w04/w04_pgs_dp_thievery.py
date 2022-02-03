def solution(money):
    money_case1 = money[2:-1]   # first house stolen
    money_case2 = money[1:]     # first house not stolen
    return max(solution_suppl(money_case1) + money[0], solution_suppl(money_case2))

def solution_suppl(money_flatten):
    for i in range(len(money_flatten)):
        if i < 2:
            continue
        elif i < 3:
            money_flatten[i] += money_flatten[i-2]
        else:
            money_flatten[i] += max(money_flatten[i-2], money_flatten[i-3])
    
    return max(money_flatten[-2:])