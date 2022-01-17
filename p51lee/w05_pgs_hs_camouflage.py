def solution(clothes):
    cloths_dict = {}
    for cloth in clothes:
        if cloth[1] in cloths_dict:
            cloths_dict[cloth[1]] += 1
        else:
            cloths_dict[cloth[1]] = 2

    answer = 1
    for n in cloths_dict.values():
        answer *= n
    return answer  - 1