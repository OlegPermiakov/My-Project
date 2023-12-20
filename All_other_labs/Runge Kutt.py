import matplotlib.pyplot as plt

######################################################   h
h = 0.01
######################################################   n
n = 1000
######################################################   x0
x0 = 1
######################################################   y0
y0 = 1
######################################################   parametres
a = 1
b = 2
d = 4
ga = 1
#######################################################   f(x, y, t)
def f(x, y):
    return a*x - b*x*y
#######################################################   g(x, y, t)
def g(x, y):
    return -d*y + ga*x*y

#Метод Ейлера
eylx = []
eyly = []
eylx.append(x0)
eyly.append(y0)
t = []
for i in range(n):
    t.append(i*h)

for i in range(n-1):
    we = eylx[i] + h*f(eylx[i], eyly[i]) 
    qw = eyly[i] + h*g(eylx[i], eyly[i])
    eylx.append(we)
    eyly.append(qw)

#Метод Рунге-Кутта 2

rg2x = []
rg2y = []
rg2x.append(x0)
rg2y.append(y0)

for i in range(n-1):
    qw = rg2y[i] + h*f(rg2x[i] + h/2, rg2y[i] + h*(f(rg2x[i], rg2y[i]))/2)
    qe = rg2x[i] + h*g(rg2x[i] + h/2, rg2y[i] + h*(g(rg2x[i], rg2y[i]))/2)
    rg2y.append(qw)
    rg2x.append(qe)

#Метод Рунге-Кутта 4
rg4x = []
rg4y = []
rg4x.append(x0)
rg4y.append(y0)


for i in range(n-1):
    k1x = f(rg4x[i], rg4y[i])
    k1y = g(rg4x[i], rg4y[i])
    k2x = f(rg4x[i] + (h*k1x)/2, rg4y[i] + h*k1y/2)
    k2y = g(rg4x[i] + (h*k1x)/2, rg4y[i] + h*k1y/2)
    k3x = f(rg4x[i] + (h*k2x)/2, rg4y[i] + h*k2y/2)
    k3y = g(rg4x[i] + (h*k2x)/2, rg4y[i] + h*k2y/2)
    k4x = f(rg4x[i] + (h*k3x), rg4y[i] + h*k3y)
    k4y = g(rg4x[i] + (h*k3x), rg4y[i] + h*k3y)
    qe = rg4x[i] + (k1x + 2*k2x + 2*k3x +k4x)*h/6
    qw = rg4y[i] + (k1y + 2*k2y + 2*k3y +k4y)*h/6
    rg4x.append(qe)
    rg4y.append(qw)

plt.plot(t, rg4x, color = "red")
plt.plot(t, rg4y, color = "green")
plt.show()
plt.plot(t, eylx, color = "red")
plt.plot(t, eyly,color = "green")
plt.show()
plt.plot(t, rg2x,color = "red")
plt.plot(t, rg2y,color = "green")
