# def solution(citations):
#     answers = [0]
#     for i, c in enumerate(sorted(citations, reverse=True)):
#         if c >= i+1:
#            answers.append(i+1)
#     return answers[-1]

# functional?
solution = lambda c: ([0] + list(filter(lambda x:x>=0, map(lambda x:-1 if x[1]<x[0] else x[0], enumerate(sorted(c, reverse=True), start=1)))))[-1]
