from math import *

def f(x):
    return x**5+x-6

a1 = 2      #a<b
b1 = 4
n = 5
x = []
for i in range(n+1):
    x.append(a1 + i*(b1-a1)/n)

#Формули Центральних прямокутників
def L11(a, b):
    L1 = f((a+b)/2)*(b-a)
    return L1

#Формули трапецій
def L21(a, b):
    L2 = (f(a) + f(b))*(b-a)/2
    return L2

#Формули Сімпсона
def L31(a, b):
    L3 = (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))
    return L3

central = 0
trapecij = 0
Simpson = 0
for i in range(1, int(len(x))):
    central += L11(x[i-1], x[i])
    trapecij += L21(x[i-1], x[i])
    Simpson += L31(x[i-1], x[i])

print(central)
print()
print(trapecij)
print()
print(Simpson)