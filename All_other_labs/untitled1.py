import numpy as np
from math import *
import matplotlib.pyplot as plt


n = int(input("Кількість змінних і їх коефіціенти: "))
m = int(input("Кількість рівнянь: "))
omega_x = []

A = np.ones((m, n))
for i in range(m):
    for j in range(n):
        A[i][j] = float(input(f"Коефіцієнт при {j+1} змінній {i+1} рівняння: "))
        b = np.ones((m, 1))
    print()
for i in range(m):
    b[i] = float(input(f"Результат {i+1} рівняння: "))
    print()

A_T = np.transpose(A)
A_pl = np.linalg.pinv(A)
epsilon = (np.dot(np.transpose(b), b) - np.dot(np.dot(np.dot(np.transpose(b), A), A_pl), b))

print()
print(A)
print()
print(b)

print()
print(f"Перевірка на однозначність: det(A_T*A) = {np.linalg.det(np.dot(A_T, A))} > 0")
print()
print(f"Точність розв'язку складає epsilon^2 = {epsilon[0][0]}")
print()

for i in range(5):
    v = np.ones((n, 1))
    for j in range(n):
        v[j] = int(input(f"Значення {j+1} компоненти вектора v: "))
    phi = np.dot(A_pl, b) + v - np.dot(np.dot(A_pl, A), v)
    q = []
    for e in phi:
        for j in e:
            q.append(j.round(8))
    omega_x.append(q)
    print()


x = []
y = []
for i in omega_x:
    x.append(i[0])
    y.append(i[1])
print()
print(f"x = {x}")
print(f"y = {y}")

x1 = np.linspace(-10, 10)
y1 = np.linspace(-10, 10) 
plt.plot(x[0], y[0], "+", x[1], y[1], "o", x[2], y[2], "*", x[3], y[3], "x", x[4], y[4], "d")
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('task')