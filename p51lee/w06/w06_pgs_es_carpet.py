def solution(brown, yellow):
    s, p = (brown + 4) / 2, yellow + brown
    return [int((s+(s**2-4*p)**0.5)/2), int((s-(s**2-4*p)**0.5)/2)]