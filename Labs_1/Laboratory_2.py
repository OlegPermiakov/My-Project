import numpy as np
from math import *

n = int(input("n = "))
a = np.ones((n, n))
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            a[i][j] = n + 100 + (i+1)/n +(j+1)/15
        else:
            a[i][j] = (i+j+2)/(15+n)
print("Матриця А")
print(a)
print()
b = np.ones((n, 1))
for i in range(0, n):
    b[i] = 23*(i+1) + n
print("Вектор b")
print(b)
print()

d = np.eye(n)
s = np.ones((n, n))
for i in range(0, n):
    for j in range(0, n):
        if j<i:
            s[i][j] = 0
        else:
            s[i][j] = 1

for i in range(0, n):
    req = 0
    ref = 0
    if j<i:
        for j in range(0, n):
            s[i][j] = 0
    elif i == 0:
        s[i][i] = sqrt(abs(a[i][i]))
        d[i][i] = abs(a[i][i])/a[i][i]
        s[i][j] = a[i][j]/(d[i][i]*s[i][i])
    else:
        for p in range(i-1):
            req += (abs(s[p][i])**2)*d[p][p]
            ref += s[p][i]*d[p][p]*s[p][j]
        d[i][i] = (abs(a[i][i])-req)/(a[i][i]-req)
        s[i][i] = sqrt(abs((a[i][i])-req))
        s[i][j] = (a[i][j] - ref)/(d[i][i]*s[i][i])
g1 = np.dot(np.transpose(s), d)
y = np.zeros((n, 1))
for i in range(n):
    summa = 0
    for j in range(n):
        if i == 0:
            y[i] = b[i]/g1[i][i]
        else:
            for k in range(i + 1):
                if y[k] != 0:
                    summa += y[k]*g1[i][k]
                else:
                    y[i] = (b[i] - summa)/g1[i][i]
x = np.zeros((n, 1))
for i in range(n-1, -1, -1):
    summa = 0
    for j in range (n-1, -1, -1):
        if i == n-1:
            x[i] = y[i]/s[i][i]
        else:
            if x[j] != 0:
                summa += x[j]*s[i][j]
            else:
                x[i] = (y[i] - summa)/s[i][i]

print("Розв'язок системи")
print(x)
print()
r = np.dot(a, x) - b
print("Незв'язка")
print(r)
print()

det_a = 1
for k in range(n):
    det_a *= d[k][k]*(s[k][k])**2
print("Визначник матриці А")
print(det_a)
print()
e = np.eye(n)
a1 = np.ones((n, n))
x1 = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if j<i:
            a1[i][j] = 0
        elif i == j:
            a1[i][j] = 1
        else:
            a1[i][j] = a[i][j]
for p in range(n-1, -1, -1):
    e1 = []
    x2 = []
    for i in range(n):
        e1.append(e[i][p])
        x2.append(x1[i][p])
    for i in range(n-1, -1, -1):
        summa = 0
        for j in range (n-1, -1, -1):
            if a1[i][j] != 0:   
                if i == n-1:
                    x2[i] = e1[i]/a1[i][i]
                else:
                    if x2[j] != 0:
                        summa += x2[j]*a1[i][j]
                    else:
                        x2[i] = (e1[i] - summa)/a1[i][i]
    for i in range(n - 1, -1, -1):
        x1[i][p] = x2[i]

ober_a = x1
print("Обернена матриця А")
print(ober_a)
print()
print("А**(-1) * A")
print(np.dot(ober_a, a))
print()

s11 = []
for i in range(n):
    s1 = 0
    for j in range(n):
        s1 += a[j][i]
        s11.append(s1)
s01 = max(s11)
s22 = []
for i in range(n):
    s2 = 0
    for j in range(n):
        s2+= ober_a[j][i]
        s22.append(s2)
s02 = max(s22)
print("Число обумовленості матриці")
print(s01 * s02)
print()

epsilon = 0.00001
q = float(input("q = "))
while q >= 1 or q < 0:
    print("q не належить проміжку [0; 1)")
    q = float(input("q = "))

k = 1
fr = []
gr = []
for i in range(n):
    gr.append(0)
fr.append(gr)
while ((q**k)/(1-q)) >= epsilon:
    tr = []
    for i in range(n):    
        tr.append(0)
    fr.append(tr)
    for i in range(n):
        sum1 = 0
        sum2 = 0
        if k == 1:  
            tr[i] = float(b[i]/a[i][i])
        else:
            if i == 0:
                sum1 += 0
            else:            
                for j in range(i):
                    sum1 += float((a[i][j]/a[i][i])*fr[k][j])
            if i == n-1:
                sum2+=0
            else:
                for j in range(i+1, n):
                    sum2 += float((a[i][j]/a[i][i])*fr[k-1][j])
            tr[i] = float(-sum1 - sum2 + b[i]/a[i][i])
    fr[k] = tr
    k+=1


print("Розв'язок системи методом Зейделя")
print(fr[0])
for i in range(1, k):
    if fr[i - 1] == fr[i]:
        st = i
        break
    else:
        print(fr[i])
        st = i
print()
xw = np.ones((n, 1))
for i in range(n):
    xw[i] = fr[st-1][i]
r1 = np.dot(a, xw) - b
print("Незв'язка")
print(r1)
print()
print("Кількість ітерацій")
print(k - 1)