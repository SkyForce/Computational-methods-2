import math
import operator

y0 = [1, 0, 0]
y1 = [1,0,0]
a =[]
a.append([-1.478867, -0.093574, 0.912588])
a.append([-0.093574, 1.106642, 0.032985])
a.append([0.912588, 0.032985, -1.482249])
i = 0
l0 = 0
l1 = 0
t = 0
e = 0.0000001
while abs(l1 - l0) > e or t < 2:
    l0 = l1
    y0 = y1
    y1 = [sum(map(operator.mul, x, y0)) for x in a]
    if(y0[i] == 0):
        i += 1
        y0 = [1, 0, 0]
        t = 0
        continue
    l1 = y1[i] / y0[i]
    norm = max(abs(t) for t in y1)
    y1 = [x / norm for x in y1]
    t += 1

pogr = max(abs(q) for q in list(map(operator.sub, [sum(map(operator.mul, x, y1)) for x in a], [l1 * x for x in y1])))
print("l1, x1, N, ||Rn||")
print(l1, y1, t, pogr)
print("Scalar")
y0 = [1, 0, 0]
y1 = [1,0,0]
l0 = 0
l1 = 0
t = 0
while abs(l1 - l0) > e or t < 2:
    l0 = l1
    y0 = y1
    y1 = [sum(map(operator.mul, x, y0)) for x in a]
    l1 = sum(map(operator.mul, y1, y0)) / sum(map(operator.mul, y0, y0))
    norm = max(abs(t) for t in y1)
    y1 = [x / norm for x in y1]
    t += 1

pogr = max(abs(q) for q in list(map(operator.sub, [sum(map(operator.mul, x, y1)) for x in a], [l1 * x for x in y1])))
print("l1, x1, N, ||Rn||")
print(l1, y1, t, pogr)

b = [list(map(operator.sub, a[i], [0]*i+[l1]+(2-i)*[0])) for i in range(3)]
y0 = [1, 0, 0]
y1 = [1,0,0]
l0 = 0
l2 = 0
t = 0
e = 0.000000001
while abs(l2 - l0) > e or t < 2:
    l0 = l2
    y0 = y1
    y1 = [sum(map(operator.mul, x, y0)) for x in b]
    l2 = sum(map(operator.mul, y1, y0)) / sum(map(operator.mul, y0, y0))
    norm = max(abs(t) for t in y1)
    y1 = [x / norm for x in y1]
    t += 1
print(l1+l2)

print(sum([a[i][i] for i in range(3)]) - 2*l1 - l2)
#pogr = max(abs(q) for q in list(map(operator.sub, [sum(map(operator.mul, x, y1)) for x in a], [(l1+l2) * x for x in y1])))
#print(pogr)
