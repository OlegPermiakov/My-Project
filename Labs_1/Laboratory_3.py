import matplotlib.pyplot as plt
import numpy as np
from math import *

omega_e = [] #Rivnoviddaleni vuzly
n = int(input('Кількість ітерацій n = '))
while n <= 0:
    print('n має бути натуральним')
    n = int =(input('n = '))
x = float(input("x = "))
for i in range(n):
    a = 1+i*(3/(n))
    omega_e.append(a)

def znammennic(t):
    f = 1
    for i in range(t):
        for j in range(t):
            if i == j:
                f*=1
            else:
                f*=(omega_e[i]-omega_e[j])
    return f
def znam1(x, t):
    f = 1
    for i in range(t):
        for j in range(t):
            if i == j:
                f*=1
            else:
                f*= (x - omega_e[j])
    return f


def beggining_function(r):
    res = sin(r**2)
    return res
def function_of_x_0_x_1_and_so_on(j):    
    r = 0
    for p in range(j):
        r += beggining_function(omega_e[p])/znammennic(p)
    return r
def N1(q):
    pt = function_of_x_0_x_1_and_so_on(0)
    for i in range(1, n):
        pt += function_of_x_0_x_1_and_so_on(i)*znam1(q, i - 1)
    return pt

matrica_znachen = np.ones((n, n))
for i in range(n):
    for j in range(n):
        if j>i:
            matrica_znachen[i][j] = 0
        for p in range(n):
            if j == p:
                matrica_znachen[i][j] *= omega_e[p]
def L_n_e(y):
    L = beggining_function(omega_e[0])
    for i in range(n):
        for j in range(n):
            if matrica_znachen[i][j] == 0:
                L += 0
            else:
                L += function_of_x_0_x_1_and_so_on(i)*(y - matrica_znachen[i][j])
    return L

omega_p = [] #Chebyshovi vuzly
k = 1
while len(omega_p) != n:
    a = 2.5 + (3/2)*cos(((2*k - 1)/(2*n))*pi)
    omega_p.append(a)
    k += 1
omega_p = omega_p[::-1]

matrica_znachen1 = np.ones((n, n))
for i in range(n):
    for j in range(n):
        if j>i:
            matrica_znachen1[i][j] = 0
        for p in range(n):
            if j == p:
                matrica_znachen1[i][j] *= omega_p[p]
def L_n_p(y):
    L = beggining_function(omega_p[0])
    for i in range(n):
        for j in range(n):
            if matrica_znachen1[i][j] == 0:
                L += 0
            else:
                L += function_of_x_0_x_1_and_so_on(i)*(y - matrica_znachen1[i][j])
    return L

def znam2(x, t):
    f = 1
    for i in range(t):
        for j in range(t):
            if i == j:
                f*=1
            else:
                f*= (x - omega_p[j])
    return f

def N2(q):
    pt = function_of_x_0_x_1_and_so_on(0)
    for i in range(1, n):
        pt += function_of_x_0_x_1_and_so_on(i)*znam2(q, i - 1)
    return pt

'''
#If you wanna see different graphs: on line 92 put # at the beginning
x = np.linspace((1/pi)*pi,(4/pi)*pi,1000)
y = L_n_e(x)
plt.plot(x, y)

plt.figure()
y1 = L_n_p(x)
plt.plot(x, y1)

'''
x = np.linspace((1/pi)*pi,(4/pi)*pi,1000)
x1 = np.linspace(-(1/pi)*pi,(1/pi)*pi,1000)
y1 = np.sin(x1**2)
plt.plot(x, y1)
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('task 1_1')

plt.figure()
x = omega_e
x1 = omega_p
y1 = np.sin(x1**2)
y2 = L_n_e(x1)
y3 = L_n_p(x1)
plt.plot(x, y1, '-', x, y2, '--', x, y3, '-.')
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('task 1')

plt.figure()
x = np.linspace((1/pi)*pi,(4/pi)*pi,1000)
x1 = np.linspace(-(1/pi)*pi,(1/pi)*pi,1000)
y4 = np.sin(x1**2) - L_n_e(x1)
y5 = np.sin(x1**2) - L_n_p(x1)
plt.plot(x, y4, x, y5, ':')
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('task 2') 
#'''