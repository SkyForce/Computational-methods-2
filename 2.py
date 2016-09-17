import operator
import copy
import numpy as np

from functools import reduce
def gauss(a):
    for k in range(0, len(a)):
        tmp = a[k][k]
        a[k][k+1:] = [x / tmp for x in a[k][k+1:len(a[k])]]
        for i in range(k+1, len(a)):
            a[i][k+1:] = list(map(operator.sub, a[i][k+1:], map(lambda x: x * a[i][k], a[k][k+1:len(a[k])])))
    print("Gauss")
    printMatrix(a)
    res = [a[-1][-1]]
    for i in range(1, len(a)):
        res = [sum(map(operator.mul, [x * (-1) for x in a[-i-1][-i-1:-1]], res)) + a[-i-1][-1]] + res
    return res

def gauss_m(a, b):
    for k in range(0, len(a)):
        tmp = [abs(a[i][k]) for i in range(k, len(a))]
        ind = tmp.index(max(tmp))
        tmp = a[ind+k][k]
        a[k], a[k+ind] = a[k+ind], a[k]
        a[k][k+1:] = [x / tmp for x in a[k][k+1:len(a[k])]]
        for i in range(k+1, len(a)):
            a[i][k+1:] = list(map(operator.sub, a[i][k+1:], map(lambda x: x * a[i][k], a[k][k+1:len(a[k])])))
    if b:
        print("Gauss mod")
        printMatrix(a)
    res = [a[-1][-1]]
    for i in range(1, len(a)):
        res = [sum(map(operator.mul, [x * (-1) for x in a[-i-1][-i-1:-1]], res)) + a[-i-1][-1]] + res
    return res

def findInv(a):
    res = []
    a = [x + [0] for x in a]
    for i in range(0, len(a)):
        for x in range(0, len(a)):
            a[x][-1] = 1 if x == i else 0
        res.append(gauss_m(copy.deepcopy(a), False))
    return list(zip(*res))

def solveInv(a, b):
    return [sum(map(operator.mul, x, b)) for x in a]

def findLU(a):
    l = []
    u = []
    for i in range(0, len(a)):
        l.append([0])
        u.append([0])
        for j in range(1, len(a)):
            l[i].append(0)
            u[i].append(0)
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            l[j][i] = a[j][i] - sum([l[j][k] * u[k][i] for k in range(0, j)])
        for j in range(i, len(a)):
            u[i][j] = (a[i][j] - sum([l[i][k] * u[k][j] for k in range(0, i)])) / l[i][i]
    return (l, u)

def findDet(a):
    l = findLU(a)[0]
    return (reduce(operator.mul, [l[i][i] for i in range(0, len(a))], 1))

def findCond(a):
    return findDet(a) * findDet(findInv(a))

def printMatrix(m):
    for i in range(0, len(m)):
        print(' '.join(format(x, ".7f") for x in m[i][0:len(m[i])-1]), '|', m[i][-1])

def printMatrix2(m):
    for i in range(0, len(m)):
        print(' '.join(format(x, ".7f") for x in m[i][0:len(m[i])]))

n = 3
a = []
a.append([7.1056E-06, -6.8888E-03, 4.41168, 4.09877])
a.append([6.5056E-03, -0.68888, 1.64168, 1.83706])
a.append([0.93056, 0.91112, 1.09168, 2.20580])

printMatrix(a)

tmp = a
res = gauss(copy.deepcopy(a))
print(res)
vecD = [4.09877, 1.83706, 2.20580]
print('|| r || = ', max([format(abs(x), ".15f") for x in list(map(operator.sub, [sum(map(operator.mul, x, res)) for x in tmp], vecD))]), end = "\n\n")


tmp = a
res = gauss_m(copy.deepcopy(a), True)
print(res)
print('|| r || = ', max([format(abs(x), ".15f") for x in list(map(operator.sub, [sum(map(operator.mul, x, res)) for x in tmp], vecD))]), end = "\n\n")


print("Inv:")
t = findInv([x[0:-1] for x in a])
printMatrix2(t)
res = solveInv(t, [x[-1] for x in a])
print(res)
print('|| r || = ', max([format(abs(x), ".15f") for x in list(map(operator.sub, [sum(map(operator.mul, x, res)) for x in tmp], vecD))]), end = "\n\n")

#print(findLU([x[0:-1] for x in a]))

print("Det:")
print(findDet(a))