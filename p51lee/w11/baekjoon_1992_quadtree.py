from sys import stdin

mat = []
for _ in range(int(stdin.readline())):
    mat.append(list(map(int, list(stdin.readline().strip()))))

def quadtree(mat):
    l = len(mat)
    zero = False
    one = False
    for z in [y for x in mat for y in x]:
        if z: one = True
        else: zero = True

    if one and not zero:
        return "1"
    elif zero and not one:
        return "0"
    else:
        mat1 = [row[:l//2] for row in mat[:l//2]]
        mat2 = [row[l//2:] for row in mat[:l//2]]
        mat3 = [row[:l//2] for row in mat[l//2:]]
        mat4 = [row[l//2:] for row in mat[l//2:]]
        return "({}{}{}{})".format(
                quadtree(mat1),
                quadtree(mat2),
                quadtree(mat3),
                quadtree(mat4)
                )

print(quadtree(mat))

