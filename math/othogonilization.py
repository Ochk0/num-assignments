def findX(A):
    v = [[] for _ in range(len(A[0]))]
    for row in A:
        for j in range(len(row)):
            v[j].append(row[j])
    return v

def calculateSection(v, x):
    product = sum(a * b for a, b in zip(v, x))
    divider = sum(num**2 for num in v)
    multi = product / divider
    return [vi * multi for vi in v]

def minusMatrix(v, x):
    return [vi - xi for vi, xi in zip(v, x)]

def calculateV(x):
    orth = [x[0]]
    for i in range(1, len(x)):
        c = x[i]
        for j in range(i):
            c = minusMatrix(c, calculateSection(orth[j], x[i]))
        orth.append(c)
    return orth

def orthBasis(A):
    result = []
    for matrix in A:
        sum = 0
        for num in matrix:
            sum += num**2
        sum = sum ** 0.5
        t = []
        for i in range(len(matrix)):
            t.append( matrix[i] / sum )
        result.append(t)
    return result

# A = [[1, 3, 1], [1, 2, 0], [-1, 0, 1], [-1, 1, 0]]
# A = [[1, 0, 0], 
#      [0, 1, 0], 
#      [0, 0, 1]]
# A = [[1, 2, 3], 
#      [4, 5, 6], 
#      [7, 8, 9], 
#      [10, 11, 12]]\
# fuck you ochko

A = [
    [1, 8, 0],
    [2, 1, 0],
    [0, -6, 1]
]

def __main__():
    x = findX(A)
    orth = calculateV(x)
    print(orth)
    print(orthBasis(orth))

__main__()
