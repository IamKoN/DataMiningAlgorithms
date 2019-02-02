"""
Nathan Robinson
11/20/2018
Data Mining
Dr. Cho
"""

import numpy as np
import math


def step1(y, h, D, max_points):
    error = sum(1 for i in range(max_points) if (y[i] != h[i])) / max_points
    alpha = .5*math.log((1-error) / error)

    Z = 0
    D_exp = []
    h_alpha = []
    for i in range(max_points):
        D_exp.append(i)
        D_exp[i] = D[i] * math.exp(-alpha*y[i]*h[i])
        h_alpha.append(i)
        h_alpha[i] = alpha * h[i]
        Z += D_exp[i]

    D_next = []
    print('\nx(i) y(i) h(x(i)) D(i)\t\terror\t\talpha\t\tD*exp\t\t Z \t\t\tD(i+1)')
    for i in range(max_points):
        D_next.append(i)
        D_next[i] = D_exp[i] / Z
        print('{0:2s}\t{1:3d}\t{2:4d}\t{3:5f}\t{4:6f}\t{5:7f}\t{6:8f}\t{7:9f}\t{8:10f}'.format(points[i],y[i],h[i],D[i],error,alpha,D_exp[i],Z,D_next[i]))

    return D_next, h_alpha

max_points = 11
points = []
for i in range(max_points):
    points.append(i)
    points[i] = 'p' + str(i + 1)

D1 = []
for i in range(max_points):
    D1.append(i)
    D1[i] = 1 / max_points

y  = [ 1,-1, 1,-1,-1, 1,-1,-1, 1,-1, 1]
h1 = [ 1,-1, 1, 1,-1, 1, 1,-1, 1, 1, 1]
h2 = [-1,-1,-1,-1,-1, 1, 1, 1, 1, 1, 1]
h3 = [-1,-1, 1,-1,-1, 1, 1,-1, 1,-1, 1]
h4 = [-1,-1,-1,-1,-1,-1,-1,-1, 1, 1, 1]

D2, h1_alpha = step1(y, h1, D1, max_points)
D3, h2_alpha = step1(y, h2, D2, max_points)
D4, h3_alpha = step1(y, h3, D3, max_points)
D5, h4_alpha = step1(y, h4, D4, max_points)

H = []
pred = []
e = 0
print('\n\nx(i) y(i) sum(h(x(i))*alpha)  predictions')
for i in range(max_points):
    H.append(i)
    H[i] = h1_alpha[i] + h2_alpha[i] + h3_alpha[i] + h4_alpha[i]
    pred.append(i)
    if H[i] < 0:
        pred[i] = -1
    else:
        pred[i] = 1
    if y[i] != pred[i]:
        e += 1
    print('{0:2s}\t{1:3d}\t\t{2:4f}\t{3:5d}'.format(points[i],y[i],H[i],pred[i]))

print('\nError: ', e/max_points, '\np1, p7, and p10 are misclassified\n\nThe strong classifier can be improved by adding more unique weak classifiers.\nDifferently shaped classifiers, such as diagonal or elliptical, could be better weak classifiers.')