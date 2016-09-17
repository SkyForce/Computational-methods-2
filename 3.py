import copy
import operator

import math


def gauss(a):
    for k in range(0, len(a)):
        tmp = a[k][k]
        a[k][k+1:] = [x / tmp for x in a[k][k+1:len(a[k])]]
        for i in range(k+1, len(a)):
            a[i][k+1:] = list(map(operator.sub, a[i][k+1:], map(lambda x: x * a[i][k], a[k][k+1:len(a[k])])))
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
        res.append(gauss(copy.deepcopy(a)))
    return list(zip(*res))

n = 3
a = []
a.append([2.19587, 0.34563, 0.17809, 2.16764])
a.append([0.34563, 3.16088, 0.55443, 6.52980])
a.append([0.17809, 0.55443, 4.89781, 6.29389])
e = 0.00000001

res = gauss(copy.deepcopy(a))
print("Gauss", res)
print("\n")

m_mn = min([a[i][i] - sum([abs(a[i][j]) for j in range(3)]) + abs(a[i][i]) for i in range(3)])
m_mx = max([a[i][i] + sum([abs(a[i][j]) for j in range(3)]) - abs(a[i][i]) for i in range(3)])
alpha = 2. / (m_mn + m_mx)
print("m, M, a: ", m_mn, m_mx, alpha)
print("\n")

b = [list(map(operator.sub, [0.] * i + [1.] + (2-i) * [0.], [x * alpha for x in a[i][0:-1]])) for i in range(3)]
c = [alpha * a[i][3] for i in range(3)]

print("Ba:")
for i in range(len(b)):
    print(b[i])
print("\n")

print("Ca: ", c)
print("\n")

nB = max(sum(abs(t) for t in x) for x in b)
print("normBa :", nB)
print("\n")

k = math.log((1-nB)*e/max([abs(x) for x in c]), nB)
k+=1
k = int(k)
print("Aprior k: ", k)
print("\n")

xk1 = [0] * 3
xk2 = [0] * 3
t = 0
print("eps, aprior, apost")
while True:
    t += 1
    xk1 = xk2
    xk2 = list(map(operator.add, [sum(map(operator.mul, b[i], xk1)) for i in range(3)], c))
    eps = max(abs(x) for x in list(map(operator.sub, res, xk2)))
    apr = (nB ** t) / (1 - nB) * max(abs(x) for x in c)
    apost = nB / (1 - nB) * max(abs(x) for x in map(operator.sub, xk2, xk1))
    print(eps, apr, apost)
    if (max(abs(q) for q in list(map(operator.sub, xk2, xk1)))) < e: break

print(xk2, t)
print(max(abs(q) for q in list(map(operator.sub, [sum(map(operator.mul, x[0:-1], xk2)) for x in a], [a[i][-1] for i in range(3)]))))

print("Zeidel")

xk1 = [0] * 3
xk2 = [0] * 3
t = 0
while True:
    t += 1
    xk1 = xk2.copy()
    for i in range(3):
        var = sum(a[i][j] * xk2[j] for j in range(i))
        var += sum(a[i][j] * xk1[j] for j in range(i+1, n))
        xk2[i] = (a[i][-1] - var) / a[i][i]
    eps = max(abs(x) for x in list(map(operator.sub, res, xk2)))
    print(eps)
    if (max(abs(q) for q in list(map(operator.sub, xk2, xk1)))) < e: break

print(xk2, t)
print(max(abs(q) for q in list(map(operator.sub, [sum(map(operator.mul, x[0:-1], xk2)) for x in a], [a[i][-1] for i in range(3)]))))