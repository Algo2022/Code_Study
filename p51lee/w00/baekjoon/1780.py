import sys


ones = 0
zeros = 0
nones = 0
def solution(mat):
    global ones
    global zeros
    global nones
    l0 = len(mat)
    if l0 == 1:
        if mat[0][0] == 1:
            ones += 1
        elif mat[0][0] == 0:
            zeros += 1
        elif mat[0][0] == -1:
            nones += 1
        return
    else:
        l = l0 // 3
        ll = l * 2
        temp = mat[0][0]
        for row in mat:
            for e in row:
                if temp != e:
                    m1 = [ r[0:l] for r in mat[0:l]]
                    m2 = [ r[l:ll] for r in mat[0:l]]
                    m3 = [ r[ll:] for r in mat[0:l]]
                    m4 = [ r[0:l] for r in mat[l:ll]]
                    m5 = [ r[l:ll] for r in mat[l:ll]]
                    m6 = [ r[ll:] for r in mat[l:ll]]
                    m7 = [ r[0:l] for r in mat[ll:]]
                    m8 = [ r[l:ll] for r in mat[ll:]]
                    m9 = [ r[ll:] for r in mat[ll:]]
                    m_list = [m1, m2, m3, m4, m5, m6, m7, m8, m9]
                    for m in m_list:
                        solution(m)
                    return
        if mat[0][0] == 1:
            ones += 1
        elif mat[0][0] == 0:
            zeros += 1
        elif mat[0][0] == -1:
            nones += 1
        return


n = int(sys.stdin.readline())


mat = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    mat.append(temp)

solution(mat)
print(nones)
print(zeros)
print(ones)

