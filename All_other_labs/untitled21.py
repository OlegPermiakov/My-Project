import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
'''
alpha1 = sp.Symbol("alpha1")
alpha2 = sp.Symbol("alpha2")
alpha3 = sp.Symbol("alpha3")
alpha4 = sp.Symbol("alpha4")
gamma1 = sp.Symbol("gamma1")
gamma2 = sp.Symbol("gamma2")
N1 = sp.Symbol("N1")
N2 = sp.Symbol("N2")
N3 = sp.Symbol("N3")
'''

alpha1 = 1
alpha2 = 1
alpha3 = 1
alpha4 = 1
gamma1 = 0.7
gamma2 = 0.3
N1 = 1
N2 = 1
N3 = 1
t = sp.Symbol("t")
h = 0.01

dot = alpha1*alpha3*gamma1+alpha2*alpha4*gamma2

C1 = (N1*alpha1*alpha4*gamma2 - N2*alpha1*alpha3*gamma1)/dot
C2 = -(N1*alpha1+N2*alpha2)/2*sp.sqrt(dot) - N3/2
C3 = (N1*alpha1+N2*alpha2)/2*sp.sqrt(dot) - N3/2

y1 = C1*alpha2/alpha1 - C2*alpha3*gamma1*sp.exp(-t*sp.sqrt(dot))/sp.sqrt(dot) + C3*alpha3*gamma1*sp.exp(t*sp.sqrt(dot))/sp.sqrt(dot)
y2 = -C1 - C2*alpha4*gamma2*sp.exp(-t*sp.sqrt(dot))/sp.sqrt(dot) + C3*alpha4*gamma2*sp.exp(t*sp.sqrt(dot))/sp.sqrt(dot)
y3 = -C2*sp.exp(-t*sp.sqrt(dot)) - C3*sp.exp(t*sp.sqrt(dot))

T = np.linspace(0, 10, 101)

u11 = [0]
u21 = [0]
u31 = [0]
u12 = [0]
u22 = [0]
u32 = [0]
u13 = [0]
u23 = [0]
u33 = [0]
u14 = [0]
u24 = [0]
u34 = [0]

def f1(r, u1, u2, u3):
    return -alpha3*gamma1*u3
def f2(r, u1, u2, u3):
    return -alpha4*gamma2*u3
def f3(r, u1, u2, u3):
    return -alpha1*u1 - alpha2*u2
def f4(r, u1, u2, u3):
    y11 = y1.subs({t:r})
    return -alpha1*u1 - alpha2*u2 - y11
def f5(r, u1, u2, u3):
    y22 = y2.subs({t:r})
    return -alpha1*u1 - alpha2*u2 - y22
def f6(r, u1, u2, u3):
    y33 = y3.subs({t:r})
    return -alpha3*gamma1*u3 - gamma1*y33
def f7(r, u1, u2, u3):
    y33 = y3.subs({t:r})
    return -alpha4*gamma2*u3 - gamma2*y33


for i in range(int(len(T))-1):
    k11 = f1(T[i], u11[i], u21[i], u31[i])
    k12 = f2(T[i], u11[i], u21[i], u31[i])
    k13 = f4(T[i], u11[i], u21[i], u31[i])
    k21 = f1(T[i], u11[i] + (h*k11)/2, u21[i] + (h*k12)/2, u31[i] + (h*k13)/2)
    k22 = f2(T[i], u11[i] + (h*k11)/2, u21[i] + (h*k12)/2, u31[i] + (h*k13)/2)
    k23 = f4(T[i], u11[i] + (h*k11)/2, u21[i] + (h*k12)/2, u31[i] + (h*k13)/2)
    k31 = f1(T[i], u11[i] + (h*k21)/2, u21[i] + (h*k22)/2, u31[i] + (h*k23)/2)
    k32 = f2(T[i], u11[i] + (h*k21)/2, u21[i] + (h*k22)/2, u31[i] + (h*k23)/2)
    k33 = f4(T[i], u11[i] + (h*k21)/2, u21[i] + (h*k22)/2, u31[i] + (h*k23)/2)
    k41 = f1(T[i], u11[i] + (h*k31), u21[i] + (h*k32), u31[i] + (h*k33))
    k42 = f2(T[i], u11[i] + (h*k31), u21[i] + (h*k32), u31[i] + (h*k33))
    k43 = f4(T[i], u11[i] + (h*k31), u21[i] + (h*k32), u31[i] + (h*k33))
    u01 = u11[i] + (k11 + 2*k21 + 2*k31 + k41)*h/6
    u02 = u21[i] + (k12 + 2*k22 + 2*k32 + k42)*h/6
    u03 = u31[i] + (k13 + 2*k23 + 2*k33 + k43)*h/6
    u11.append(u01)
    u21.append(u02)
    u31.append(u03)

plt.plot(T, u11, color = "red", label = "U1")
plt.plot(T, u21, color = "green", label = "U2")
plt.plot(T, u31, color = "blue", label = "U3")
plt.title("1")
plt.show()
#############################################

for i in range(int(len(T))-1):
    k11 = f1(T[i], u12[i], u22[i], u32[i])
    k12 = f2(T[i], u12[i], u22[i], u32[i])
    k13 = f5(T[i], u12[i], u22[i], u32[i])
    k21 = f1(T[i], u12[i] + (h*k11)/2, u22[i] + (h*k12)/2, u32[i] + (h*k13)/2)
    k22 = f2(T[i], u12[i] + (h*k11)/2, u22[i] + (h*k12)/2, u32[i] + (h*k13)/2)
    k23 = f5(T[i], u12[i] + (h*k11)/2, u22[i] + (h*k12)/2, u32[i] + (h*k13)/2)
    k31 = f1(T[i], u12[i] + (h*k21)/2, u22[i] + (h*k22)/2, u32[i] + (h*k23)/2)
    k32 = f2(T[i], u12[i] + (h*k21)/2, u22[i] + (h*k22)/2, u32[i] + (h*k23)/2)
    k33 = f5(T[i], u12[i] + (h*k21)/2, u22[i] + (h*k22)/2, u32[i] + (h*k23)/2)
    k41 = f1(T[i], u12[i] + (h*k31), u22[i] + (h*k32), u32[i] + (h*k33))
    k42 = f2(T[i], u12[i] + (h*k31), u22[i] + (h*k32), u32[i] + (h*k33))
    k43 = f5(T[i], u12[i] + (h*k31), u22[i] + (h*k32), u32[i] + (h*k33))
    u01 = u12[i] + (k11 + 2*k21 + 2*k31 + k41)*h/6
    u02 = u22[i] + (k12 + 2*k22 + 2*k32 + k42)*h/6
    u03 = u32[i] + (k13 + 2*k23 + 2*k33 + k43)*h/6
    u12.append(u01)
    u22.append(u02)
    u32.append(u03)

plt.plot(T, u12, color = "red", label = "U1")
plt.plot(T, u22, color = "green", label = "U2")
plt.plot(T, u32, color = "blue", label = "U3")
plt.title("2")
plt.show()
#############################################
for i in range(int(len(T))-1):
    k11 = f6(T[i], u13[i], u23[i], u33[i])
    k12 = f2(T[i], u13[i], u23[i], u33[i])
    k13 = f3(T[i], u13[i], u23[i], u33[i])
    k21 = f6(T[i], u13[i] + (h*k11)/2, u23[i] + (h*k12)/2, u33[i] + (h*k13)/2)
    k22 = f2(T[i], u13[i] + (h*k11)/2, u23[i] + (h*k12)/2, u33[i] + (h*k13)/2)
    k23 = f3(T[i], u13[i] + (h*k11)/2, u23[i] + (h*k12)/2, u33[i] + (h*k13)/2)
    k31 = f6(T[i], u13[i] + (h*k21)/2, u23[i] + (h*k22)/2, u33[i] + (h*k23)/2)
    k32 = f2(T[i], u13[i] + (h*k21)/2, u23[i] + (h*k22)/2, u33[i] + (h*k23)/2)
    k33 = f3(T[i], u13[i] + (h*k21)/2, u23[i] + (h*k22)/2, u33[i] + (h*k23)/2)
    k41 = f6(T[i], u13[i] + (h*k31), u23[i] + (h*k32), u33[i] + (h*k33))
    k42 = f2(T[i], u13[i] + (h*k31), u23[i] + (h*k32), u33[i] + (h*k33))
    k43 = f3(T[i], u13[i] + (h*k31), u23[i] + (h*k32), u33[i] + (h*k33))
    u01 = u13[i] + (k11 + 2*k21 + 2*k31 + k41)*h/6
    u02 = u23[i] + (k12 + 2*k22 + 2*k32 + k42)*h/6
    u03 = u33[i] + (k13 + 2*k23 + 2*k33 + k43)*h/6
    u13.append(u01)
    u23.append(u02)
    u33.append(u03)

plt.plot(T, u13, color = "red", label = "U1")
plt.plot(T, u23, color = "green", label = "U2")
plt.plot(T, u33, color = "blue", label = "U3")
plt.title("3")
plt.show()
#############################################
for i in range(int(len(T))-1):
    k11 = f1(T[i], u14[i], u24[i], u34[i])
    k12 = f7(T[i], u14[i], u24[i], u34[i])
    k13 = f3(T[i], u14[i], u24[i], u34[i])
    k21 = f1(T[i], u14[i] + (h*k11)/2, u24[i] + (h*k12)/2, u34[i] + (h*k13)/2)
    k22 = f7(T[i], u14[i] + (h*k11)/2, u24[i] + (h*k12)/2, u34[i] + (h*k13)/2)
    k23 = f3(T[i], u14[i] + (h*k11)/2, u24[i] + (h*k12)/2, u34[i] + (h*k13)/2)
    k31 = f1(T[i], u14[i] + (h*k21)/2, u24[i] + (h*k22)/2, u34[i] + (h*k23)/2)
    k32 = f7(T[i], u14[i] + (h*k21)/2, u24[i] + (h*k22)/2, u34[i] + (h*k23)/2)
    k33 = f3(T[i], u14[i] + (h*k21)/2, u24[i] + (h*k22)/2, u34[i] + (h*k23)/2)
    k41 = f1(T[i], u14[i] + (h*k31), u24[i] + (h*k32), u34[i] + (h*k33))
    k42 = f7(T[i], u14[i] + (h*k31), u24[i] + (h*k32), u34[i] + (h*k33))
    k43 = f3(T[i], u14[i] + (h*k31), u24[i] + (h*k32), u34[i] + (h*k33))
    u01 = u14[i] + (k11 + 2*k21 + 2*k31 + k41)*h/6
    u02 = u24[i] + (k12 + 2*k22 + 2*k32 + k42)*h/6
    u03 = u34[i] + (k13 + 2*k23 + 2*k33 + k43)*h/6
    u14.append(u01)
    u24.append(u02)
    u34.append(u03)

plt.plot(T, u14, color = "red", label = "U1")
plt.plot(T, u24, color = "green", label = "U2")
plt.plot(T, u34, color = "blue", label = "U3")
plt.title("4")
plt.show()
#############################################
Urt = [[u11, u21, u31], [u12, u22, u32], [u13, u23, u33], [u14, u24, u34]]
for i in range(4):
    print(f"{i+1}")
    print()
    for j in range(3):
        print(Urt[i][j])
        print()
    input()
    print()