import operator

import math


def solve(vecA, vecB, vecC, vecD):
    tmp = [[-vecB[0], vecC[0]] + [0]*(n-2)]
    for i in range(1, n-1):
        tmp.append([0] * (i-1) + [vecA[i], -vecB[i], vecC[i]] + [0]*(n-2-i))
    tmp.append([0]*(n-2) + [vecA[n-1], -vecB[n-1]])

    print(' '.join(format(x, ".5f") for x in tmp[0]), '|', vecD[0])
    for i in range(1, n-1):
        print(' '.join(format(x, ".5f") for x in tmp[i]), '|', vecD[i])
    print(' '.join(format(x, ".5f") for x in tmp[n-1]), '|', vecD[n-1])

    s = [vecC[0] / vecB[0]]
    t = [-vecD[0] / vecB[0]]
    print('m, k')
    print('{:.5f} {:.5f}'.format(s[0], t[0]))
    for i in range(1, n):
        tm = t[-1];
        tm1 = s[-1]
        t.append((vecA[i] * tm - vecD[i]) / (vecB[i] - vecA[i] * tm1))
        s.append( vecC[i] / (vecB[i] - vecA[i] * tm1))
        print('{:.5f} {:.5f}'.format(s[i], t[i]))

    res = [t[-1]]
    for i in range(0, n-1):
        res.append(s[n-i-2]*res[-1] + t[n-i-2])
    res.reverse()
    print('x = ',[format(x, ".8f") for x in res])
    print('Ax - d = ', [format(x, ".10f") for x in list(map(operator.sub, [sum(map(operator.mul, x, res)) for x in tmp], vecD))], end = "\n\n")

q = lambda x : 1+2*x
r = lambda x: -math.log(1+x, math.e)
f = lambda x: x - 1
alpha = 0.5
beta = 0.7

n = int(input())
h = 1 / (n-1)
vecA = [0] + [2 - q(x) * h for x in [t * h for t in range(1, n-1)]] + [-1]
vecB = [-alpha*h-1] + [4 - r(x) * 2 * h * h for x in [t * h for t in range(1, n-1)]] + [-beta*h-1]
vecC = [-1] + [2 + q(x) * h for x in [t * h for t in range(1, n-1)]] + [0]
vecD = [0] + [f(x)*2*h*h for x in [t * h for t in range(1, n-1)]] + [0]

solve(vecA, vecB, vecC, vecD)

# second
n-=1
vecA[n] = -4 + vecB[n-1]/vecA[n-1]
vecB[0] = -2*alpha*h-(3-vecA[1]/vecC[1])
vecB[n] = -2*beta*h-3+vecC[n-1]/vecA[n-1]
vecC[0] = -4 + vecB[1] / vecC[1]
vecD[0] = -vecD[1] / vecC[1]
vecD[n] = -vecD[n-1] / vecA[n-1]
n+=1
solve(vecA, vecB, vecC, vecD)





