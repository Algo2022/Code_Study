def solution(N, number):
    N_string = str(N)
    series_of_N = [int(N_string * i) for i in range(1, 9)]
    solution_dict = {i: {series_of_N[i - 1]} for i in range(1, 9)}

    for ord1 in range(1, 9):
        if number in solution_dict[ord1]:
            return ord1
        for op1 in solution_dict[ord1]:
            for ord2 in range(1, min(ord1, 8 - ord1) + 1):
                for op2 in solution_dict[ord2]:
                    solution_dict[ord1 + ord2].update(
                        [op1 + op2, abs(op1 - op2), op1 * op2]
                    )
                    if op2 != 0 and op1 % op2 == 0:
                        solution_dict[ord1 + ord2].add(op1 / op2)
                    if op1 != 0 and op2 % op1 == 0:
                        solution_dict[ord1 + ord2].add(op2 / op1)

    return -1