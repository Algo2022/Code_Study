def solution(citations):
    citations.sort(reverse=True)
    answers = [0]
    for i, c in enumerate(citations):
        if c >= i+1:
           answers.append(i+1)
    return answers[-1]