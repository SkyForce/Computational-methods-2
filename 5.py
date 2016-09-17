import math
import operator

k = lambda x,y : math.log(3+x*y, math.e) / 3
f = lambda x : math.pow((1-x), 2)
a = 0
b = 1
N = 10

def gauss_m(a):
    for k in range(0, len(a)):
        tmp = [abs(a[i][k]) for i in range(k, len(a))]
        ind = tmp.index(max(tmp))
        tmp = a[ind+k][k]
        a[k], a[k+ind] = a[k+ind], a[k]
        a[k][k+1:] = [x / tmp for x in a[k][k+1:len(a[k])]]
        for i in range(k+1, len(a)):
            a[i][k+1:] = list(map(operator.sub, a[i][k+1:], map(lambda x: x * a[i][k], a[k][k+1:len(a[k])])))

    res = [a[-1][-1]]
    for i in range(1, len(a)):
        res = [sum(map(operator.mul, [x * (-1) for x in a[-i-1][-i-1:-1]], res)) + a[-i-1][-1]] + res
    return res

def solve(n, coeff, x):
    ca = [(b-a)/2 * v for v in coeff]
    xa = [(b-a)/2*v+(b+a)/2 for v in x]
    d = []
    for i in range(n):
        if(n==4):
            d.append([0,0,0,0])
        else :
            d.append([0,0,0,0,0,0])

    for i in range(n):
        for j in range(n):
            d[i][j] = (1 if i==j else 0) + ca[j] * k(xa[i], xa[j])
        d[i].append(f(xa[i]))

    res = gauss_m(d)
    print("u[j]:", res)

    h = (b-a) / N
    g = [-sum(ca[m] * k(a+t*h, xa[m]) * res[m] for m in range(n)) + f(a+t*h) for t in range(N+1)]
    return g

n = 4
x = [ 0.8611363116, -0.8611363116,  0.3399810436, -0.3399810436 ]
coeff = [0.3478548451, 0.3478548451, 0.6521451549, 0.6521451549 ]

g1 = solve(4, coeff, x)
print(g1)

n = 6
x = [ 0.9324695142, -0.9324695142,  0.6612093865, -0.6612093865, 0.2386191861, -0.2386191861]
coeff = [0.1713244924, 0.1713244924, 0.3607615730, 0.3607615730, 0.4679139346, 0.4679139346]

g2 = solve(6, coeff, x)
print(g2)

print("||r|| =", max(abs(q) for q in list(map(operator.sub, g2, g1))))