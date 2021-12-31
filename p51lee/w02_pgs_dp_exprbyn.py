def solution(N, number):
    N_string = str(N)
    series_of_N = [int(N_string * i) for i in range(1, 9)]
    solution_dict = {i: {series_of_N[i - 1]} for i in range(1, 9)}

    for sol in range(1, 9):
        if number in solution_dict[sol]:
            return sol
        for op1 in solution_dict[sol]:
            for order in range(1, min(sol, 8 - sol) + 1):
                for eqn_num in solution_dict[order]:
                    solution_dict[sol + order].update(
                        [op1 + eqn_num, abs(op1 - eqn_num), op1 * eqn_num]
                    )
                    # solution_dict[sol + order].add(op1 + eqn_num)
                    # solution_dict[sol + order].add(abs(op1 - eqn_num))
                    # solution_dict[sol + order].add(op1 * eqn_num)
                    if eqn_num != 0 and op1 % eqn_num == 0:
                        solution_dict[sol + order].add(op1 / eqn_num)
                    if op1 != 0 and eqn_num % op1 == 0:
                        solution_dict[sol + order].add(eqn_num / op1)

    return -1