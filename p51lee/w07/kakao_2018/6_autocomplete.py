# greatest common prefix
def gcp(w1, w2):
    u = min(len(w1), len(w2))
    for i in range(u):
        if w1[i] != w2[i]:
            return i
    return u

def solution(words):
    words.sort()
    answer = 0
    n = len(words)
    for i in range(n):
        if i == 0:
            answer += min(gcp(words[i], words[i+1]) + 1, len(words[i]))
        elif i == n-1:
            answer += min(gcp(words[i-1], words[i]) + 1, len(words[i]))
        else:
            answer += min(max(gcp(words[i-1], words[i]), gcp(words[i], words[i+1])) + 1, len(words[i]))
    return answer
