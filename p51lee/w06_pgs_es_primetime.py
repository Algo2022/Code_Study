def is_prime(num: int) -> bool:
    if num < 2:
        return False
    eratosthenes_list = list(range(2, num))
    index, prime_curr = 0, 0
    while index < len(eratosthenes_list) and prime_curr < num ** 0.5:
        prime_curr = eratosthenes_list[index]
        if num % prime_curr == 0:
            return False
        index += 1
    return True


def get_num_dict(numbers_string: str) -> dict:
    num_dict = {i: 0 for i in range(10)}
    for number_string in numbers_string:
        num_dict[int(number_string)] += 1
    return num_dict


def count_prime(num_dict: dict, prev: str) -> int:
    count = 0
    choice_list = list(num_dict.keys())
    if not prev and 0 in choice_list:
        choice_list.remove(0)

    for num_choice in choice_list:
        if num_dict[num_choice] == 0:
            continue
        else:
            dict_buff = num_dict.copy()
            dict_buff[num_choice] -= 1
            curr = prev+str(num_choice)
            if is_prime(int(curr)):
                count += 1
            count += count_prime(dict_buff, curr)
    return count


def solution(numbers):
    number_dict = get_num_dict(numbers)
    return count_prime(number_dict, "")