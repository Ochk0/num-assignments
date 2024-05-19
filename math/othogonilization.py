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

A = [[1, 3, 1], [1, 2, 0], [-1, 0, 1], [-1, 1, 0]]

def __main__():
    x = findX(A)
    orth = calculateV(x)
    print(orth)

__main__()
