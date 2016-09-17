import math
import operator
import scipy
from scipy import special

def l(n, x):
    if(n == 1):
        return (-5-math.sin(x)) / (7-3*math.sin(x)) * 2 - (1-x)/2*(2*x+2) + (1+x/2)*(x*x+2*x-13/2.0)
    elif n == 2:
        return (-5-math.sin(x)) / (7-3*math.sin(x)) * (6*x) - (1-x)/2*(3*x*x-3) + (1+x/2)*(x*x*x-3*x+2)
    n -= 3
    s1 = -2*(n+1)*(-2*x)*scipy.special.jacobi(n+1, 1, 1)(x)
    s2 = -2*(n+1)*(1-x*x)*(n+1+2+1) / 2 * scipy.special.jacobi(n, 2, 2)(x)
    ddy = s1 + s2
    dy = -2*(n+1)*(1-x*x)*scipy.special.jacobi(n+1, 1, 1)(x)
    return (-5-math.sin(x)) / (7-3*math.sin(x)) * ddy - (1-x)/2*dy + (1+x/2)*scipy.special.jacobi(n, 2, 2)(x)

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

def solve(x, r):
    return sum(map(operator.mul, r, [x*x+2*x-13/3]+[x*x*x-3*x+2]+[scipy.special.jacobi(i-3, 2, 2)(x) for i in range(3, n+1)]))
print("n = ")
n = int(input())
d = []
for i in range(n):
    d.append([0]*n)

for i in range(n):
    ti = math.cos((2*(i+1)-1)*math.pi/(2*n))
    for j in range(n):
        d[i][j] = l(j+1, ti)
    d[i].append(ti/3+0.5)
    print(d[i])


res = gauss_m(d)
print("cj = ", res)
print(solve(-1, res), solve(0, res), solve(1, res))

for i in range(3, 8):
    n = i
    d = []
    for i in range(n):
        d.append([0]*n)

    for i in range(n):
        ti = math.cos((2*(i+1)-1)*math.pi/(2*n))
        for j in range(n):
            d[i][j] = l(j+1, ti)
        d[i].append(ti/3+0.5)


    res = gauss_m(d)

    print("n = " + str(i+1)+":", solve(-1, res), solve(0, res), solve(1, res))









