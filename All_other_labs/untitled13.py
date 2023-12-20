import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)*x

a = -np.pi
b = np.pi
m = 15
h = (b-a)/m
n = 15
x = np.linspace(a, b, m)
y = f(x)
A = np.zeros((n+1, n+1))
z = np.zeros(n+1)


for k in range(n+1):
    for j in range(n+1):
        for i in range(m):
            A[k, j] += x[i]**(j+k)

for k in range(n+1):
    for i in range(m):
        z[k] += y[i]*x[i]**k
        
c = np.linalg.solve(A, z)

def poly(c):
    def res(x):
        s = 0
        for i in range(0, c.shape[0]):
            s+=c[i]*(x**i)
        return s
    return res


x2 = np.linspace(a, b, 100)
p = poly(c)
y2 = p(x2)

plt.plot(x, y)
plt.plot(x2, y2)