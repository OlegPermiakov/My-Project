import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.Symbol("t")
alpha11 = (float(input("alpha1 ")))
alpha21 = (float(input("alpha2 ")))
alpha31 = (float(input("alpha3 ")))
alpha41 = (float(input("alpha4 ")))

gamma1 = (float(input("gamma1 ")))
gamma2 = (float(input("gamma2 ")))

N1 = float(input("N1 "))
N2 = float(input("N2 "))
N3 = float(input("N3 "))
'''
gamma1 = sp.Symbol("gamma1")
gamma2 = sp.Symbol("gamma2")
N1 = sp.Symbol("N1")
N2 = sp.Symbol("N2")
N3 = sp.Symbol("N3")
'''
alpha1 = sp.Symbol("alpha1")
alpha2 = sp.Symbol("alpha2")
alpha3 = sp.Symbol("alpha3")
alpha4 = sp.Symbol("alpha4")
lamba = sp.Symbol("lamba")

eps = (float(input("Epsilon ")))
T = (float(input("T ")))

Y1 = sp.Function("y1")(t)
Y2 = sp.Function("y2")(t)
Y3 = sp.Function("y3")(t)
Y = [Y1, Y2, Y3]
C1 = sp.Symbol("C1")
C2 = sp.Symbol("C2")
C3 = sp.Symbol("C3")

y_1 = 0
y_2 = 0
y_3 = 0
y_00= sp.Matrix([[y_1], [y_2], [y_3]])

p = []

def fst_part(a1, a2, a3, a4, g1, g2, n1, n2, n3):
    
    y01 = sp.diff(Y1, t)
    y02 = sp.diff(Y2, t)
    y03 = sp.diff(Y3, t)
    
    y0 = [y01, y02, y03]
    
    eq = (sp.Eq(y01, -a3*g1*Y3), sp.Eq(y02, -a4*g2*Y3), sp.Eq(y03, -a1*Y1 - a2*Y2))
    w = []
    for i in range(int(len(eq))):
        el = []
        for j in range(int(len(eq))):
            if sp.diff(eq[i].rewrite(sp.Add) - y0[i], Y[j]) == 0:
                el.append(0)
            else:
                el.append(sp.diff(eq[i].rewrite(sp.Add) - y0[i], Y[j]).subs({alpha1:a1, alpha2:a2, alpha3:a3, alpha4:a4, gamma1:g1, gamma2:g2, N1:n1, N2:n2, N3:n3}))
        w.append(el)
    le = []
    for i in range(int(len(y0))):
        er = []
        for j in range(int(len(y0))):
            if i == j:
                er.append(lamba)
            else:
                er.append(0)
        le.append(er)
    ew = sp.Matrix(le)
    we = sp.Matrix(w) - ew
    dew = sp.det(we)
    lams = sp.solve(dew, lamba)
    print(lams)
    print()
    print()
    
    rfunctions = sp.dsolve(eq, [Y1, Y2, Y3])
    Y11 = rfunctions[0].rewrite(sp.Add) - Y1
    Y21 = rfunctions[1].rewrite(sp.Add) - Y2
    Y31 = rfunctions[2].rewrite(sp.Add) - Y3
    
    eq = (sp.Eq(Y11.subs({t:0}), N1), sp.Eq(Y21.subs({t:0}), N2), sp.Eq(Y31.subs({t:0}), N3))
    rfunctions = sp.solve(eq)
    y1 = Y11.subs({C1:rfunctions.get(C1), C2:rfunctions.get(C2), C3:rfunctions.get(C3), N1:n1, N2:n2, N3:n3})
    y2 = Y21.subs({C1:rfunctions.get(C1), C2:rfunctions.get(C2), C3:rfunctions.get(C3), N1:n1, N2:n2, N3:n3})
    y3 = Y31.subs({C1:rfunctions.get(C1), C2:rfunctions.get(C2), C3:rfunctions.get(C3), N1:n1, N2:n2, N3:n3})
    
    
    y = [[y1], [y2], [y3]]
    return y

def scnd_part(a1, a2, a3, a4, g1, g2, n1, n2, n3):
    url = []
    urt = []
    alphas = [alpha1, alpha2, alpha3, alpha4]
    y = fst_part(a1, a2, a3, a4, g1, g2, n1, n2, n3)
    functions = [[-alpha3*gamma1*Y[2]], [-alpha4*gamma2*Y[2]], [-alpha1*Y[0]-alpha2*Y[1]]]
    
    for i in range(int(len(functions))):
        urk = []
        for j in range(int(len(Y))):
            urk.append(sp.diff(functions[i][0], Y[j]).subs({alpha1:a1, alpha2:a2, alpha3:a3, alpha4:a4, gamma1:g1, gamma2:g2, N1:n1, N2:n2, N3:n3, Y1:y[0][0], Y2:y[1][0], Y3:y[2][0]}))
        url.append(urk)
    dUdy = sp.Matrix(url)
    
    for i in range(int(len(functions))):
        urs = []
        for j in range(int(len(alphas))):
            urs.append(sp.diff(functions[i][0], alphas[j]).subs({alpha1:a1, alpha2:a2, alpha3:a3, alpha4:a4, gamma1:g1, gamma2:g2, N1:n1, N2:n2, N3:n3, Y1:y[0][0], Y2:y[1][0], Y3:y[2][0]}))
        urt.append(urs)
    dUdalpha = sp.Matrix(urt)
    
    Utt = []
    for i in range(int(len(functions))):
        dert = []
        for j in range(int(len(alphas))):
            am = "u" + str(i) + str(j)
            am = sp.Function(f"u{i+1}{j+1}")(t)
            dert.append(am)
        Utt.append(dert)
    Ut = sp.Matrix(Utt)
    
    asta = dUdy*Ut + dUdalpha
    User = []    
    for i in range(int(len(Utt))):
        Ustr = []
        for j in range(int(len(Utt[0]))):
            am = "u0" + str(i) + str(j)
            am = sp.diff(Utt[i][j], t)
            Ustr.append(am)
        User.append(Ustr)
    resp = []
    for i in range(int(len(sp.matrix2numpy(asta)[0]))):
        der = []
        for j in range(int(len(sp.matrix2numpy(asta)))):
            der.append(sp.Eq(User[j][i], sp.matrix2numpy(asta)[j][i]))
        resp.append(der)
    
    resq = [[], [], []]
    for i in range(int(len(resp))):
        west = sp.dsolve((resp[i]))
        U1 = west[0].rewrite(sp.Add) - sp.matrix2numpy(Ut)[0][i]
        U2 = west[1].rewrite(sp.Add) - sp.matrix2numpy(Ut)[1][i]
        U3 = west[2].rewrite(sp.Add) - sp.matrix2numpy(Ut)[2][i]

        resty = sp.solve([U1.subs({t:0}), U2.subs({t:0}), U3.subs({t:0})])
        resq[0].append(sp.simplify(U1.subs({C1:resty.get(C1), C2:resty.get(C2), C3:resty.get(C3)})))
        resq[1].append(sp.simplify(U2.subs({C1:resty.get(C1), C2:resty.get(C2), C3:resty.get(C3)})))
        resq[2].append(sp.simplify(U3.subs({C1:resty.get(C1), C2:resty.get(C2), C3:resty.get(C3)})))
        
    return resq


def thrd_part(a1, a2, a3, a4, g1, g2, n1, n2, n3, Time, count):
    Utt = scnd_part(a1, a2, a3, a4, g1, g2, n1, n2, n3)
    x = sp.Matrix(fst_part(a1, a2, a3, a4, g1, g2, n1, n2, n3))
    Utt_T = []
    for i in range(int(len(Utt[0]))):
        w = []
        for j in range(int(len(Utt))):
            w.append(Utt[j][i])
        Utt_T.append(w)
    Ut = sp.Matrix(Utt)
    Ut_T=sp.Matrix(Utt_T)
    
    Ut_bfr = Ut_T*Ut
    ALF = sp.matrix2numpy(Ut_bfr)
    tm = np.linspace(0, Time, count)
    result = []
    for i in range(int(len(ALF))):
        esu = []
        for j in range(int(len(ALF[0]))):
            mus = 0
            for k in range(1, int(len(tm))):
                mus += (tm[k] - tm[k-1])/6 * (ALF[i][j].subs({t:tm[k]}) + 4*ALF[i][j].subs({t:(tm[k]+tm[k-1])/2}) + ALF[i][j].subs({t:tm[k]}))
            esu.append(mus)
        result.append(esu)
    sd = sp.Matrix(result)
    one = sp.Inverse(sd)
    
    axon = y_00 - x
    alon = sp.matrix2numpy(Ut_T * axon)
    
    asum = []
    for i in range(int(len(alon))):
        salut = 0
        for k in range(1, int(len(tm))):
            salut += (tm[k] - tm[k-1])/6 * (alon[i][0].subs({t:tm[k]}) + 4*alon[i][0].subs({t:(tm[k]+tm[k-1])/2}) + alon[i][0].subs({t:tm[k-1]}))
        asum.append(salut)
    
    two = sp.Matrix(asum)
    res = one*two    
    return res    

def I(a1, a2, a3, a4, g1, g2, n1, n2, n3, Time, count):
    x = sp.Matrix(fst_part(a1, a2, a3, a4, g1, g2, n1, n2, n3))
    tm = np.linspace(0, Time, count)
    
    inty = x - y_00
    sm = 0
    for i in range(int(len(inty))):
        sm += inty[i]**2
    sur = (sp.sqrt(sm))**2
    sa = 0
    for j in range(1, int(len(tm))):
        sa += (tm[j] - tm[j-1])/6 * (sur.subs({t:tm[j]}) + 4*sur.subs({t:(tm[j]+tm[j-1])/2}) + sur.subs({t:tm[j-1]}))
    return sa

def final_results(a1, a2, a3, a4, g1, g2, n1, n2, n3, Time, count):
    k = 0
    b = sp.Matrix([a1, a2, a3, a4])
    Ii = []
    altron = []
    while True:
        a1, a2, a3, a4 = b[0], b[1], b[2], b[3]
        tm = np.linspace(0, Time, count)
        march = fst_part(a1, a2, a3, a4, g1, g2, n1, n2, n3)
        Ii.append(I(b[0], b[1], b[2], b[3], g1, g2, n1, n2, n3, Time, count))
        fst = []
        scnd= []
        thrd= []
        print(f"{k}")
        print("y1 = ", march[0][0])
        print()
        print("y2 = ", march[1][0])
        print()
        print("y3 = ", march[2][0])
        for i in range(int(len(tm))):
            fst.append(march[0][0].subs({t:tm[i]}))
            scnd.append(march[1][0].subs({t:tm[i]}))
            thrd.append(march[2][0].subs({t:tm[i]}))
        plt.plot(tm, fst)
        plt.title(f"{k}, y1")        
        plt.show()
        
        plt.plot(tm,scnd)
        plt.title(f"{k}, y2")
        plt.show()
        
        plt.plot(tm,thrd)
        plt.title(f"{k}, y3")
        plt.show()
        
        plt.plot(tm, fst, color = "red")
        plt.plot(tm, scnd, color = "green")
        plt.plot(tm, thrd, color = "blue")
        plt.title(f"{k}, y1, y2, y3")
        plt.show()
        atr = scnd_part(b[0], b[1], b[2], b[3], g1, g2, n1, n2, n3)
        print("Matrix ")
        for i in range(int(len(atr))):
            for j in range(int(len(atr[0]))):
                print(atr[i][j])
                print()
            print()
        

        ale = thrd_part(a1, a2, a3, a4, g1, g2, n1, n2, n3, Time, count)
        afe = []
        for i in ale:
            afe.append(i)
        a = sp.Matrix(afe)
        c = b+a
        b = c
        atr1 = scnd_part(b[0], b[1], b[2], b[3], g1, g2, n1, n2, n3)
        atr2 = I(b[0], b[1], b[2], b[3], g1, g2, n1, n2, n3, Time, count)
        print("c =", c)
        print("I = ", atr2)
        norm = sp.matrix2numpy(thrd_part(b[0], b[1], b[2], b[3], g1, g2, n1, n2, n3, Time, count))
        normal = 0
        for i in range(int(len(norm))):
            normal += norm[i][0]**2
        res =sp.sqrt(normal)
        print("Norma delta ", res)
        print()
        amsterdam = []
        amsterdam.append(march[0][0])
        amsterdam.append(march[1][0])
        amsterdam.append(march[2][0])
        amsterdam.append(atr2)
        amsterdam.append(k)
        amsterdam.append(sp.matrix2numpy(a))
        amsterdam.append(b)
        amsterdam.append(res)
        altron.append(amsterdam)
        if res < eps:
            break
        k+=1
    return [I(b[0], b[1], b[2], b[3], g1, g2, n1, n2, n3, Time, count), k, sp.matrix2numpy(a), b, atr1, Ii, altron]

assume = final_results(alpha11, alpha21, alpha31, alpha41, gamma1, gamma2, N1, N2, N3, T, 100)
print("RESULTS: ")
print("I(p_k)")
print(assume[0])
print()
print("k")
print(assume[1])
print()
print("Delta p_k")
print(assume[2])
print()
print("p = [alpha1, alpha2, alpha3, alpha4]")
print(sp.matrix2numpy(assume[3]))
print()
print("Matrix czutlywosti")
for i in range(int(len(assume[4]))):
    for j in range(int(len(assume[4][0]))):
        print(assume[4][i][j])
        print()
    print()
plt.title("I(p_k)")
for i in range(int(len(assume[5]))):
    plt.plot(i, assume[5][i], "*", color = "red")
plt.show()
print(assume[5][0])

print()
print()
print()
print("1 -- y_1, 2 -- y_2, 3 -- y_3, 4 -- I(p_k), 5 -- k, 6 -- Delta p_k, 7 -- p, 8 -- ||Delta p_k||")
for i in range(int(len(assume[6]))):
    print(i)
    for j in range(int(len(assume[6][0]))):
        print(assume[6][i][j])
        print()
    print()
'''
alpha1 .37
alpha2 .61
alpha3 .87
alpha4 .61
gamma1 .29
gamma2 .71
N1 1
N2 1
N3 1
Epsilon .1
T 1


RESULTS: 
I(p_k)
2.03581440017613

k
4

Delta p_k
[[0.163235537193065]
 [-0.695938598819597]
 [6.55474616250192]
 [0.466057243980761]]

p = [alpha1, alpha2, alpha3, alpha4]
[[-0.0439300835356441]
 [0.731080642395694]
 [2.15294146156789]
 [0.0458063700431652]]

Matrix czutlywosti
5.12863947917471e+18*sin(0.0604259355195946*t) - 5.12863947917471e+18*sin(0.0604259355195946*t) + 5.83217695183851e+19*cos(0.0604259355195946*t) - 5.83217695183851e+19*cos(0.0604259355195946*t) - 45972.317335492

2.67150614581751e+17*sin(0.0604259355195946*t) - 2.67150614581751e+17*sin(0.0604259355195946*t) + 3.0379785191762e+18*cos(0.0604259355195946*t) - 3.03797851917618e+18*cos(0.0604259355195946*t) - 16679.2920646966

-1.04648252061749e+17*sin(0.0604259355195946*t) + 1.04648252061749e+17*sin(0.0604259355195946*t) - 1.19003709697865e+18*cos(0.0604259355195946*t) + 1.19003709697861e+18*cos(0.0604259355195946*t) + 38658.9765351851

4.26378782559683e+18*sin(0.0604259355195946*t) - 4.26378782559683e+18*sin(0.0604259355195946*t) + 4.84868651519583e+19*cos(0.0604259355195946*t) - 4.84868651519585e+19*cos(0.0604259355195946*t) + 157329.056284704


2.67150614581751e+17*sin(0.0604259355195946*t) - 2.67150614581752e+17*sin(0.0604259355195946*t) + 3.03797851917621e+18*cos(0.0604259355195946*t) - 3.03797851917621e+18*cos(0.0604259355195946*t) - 2600.35392737996

1.39158642679427e+16*sin(0.0604259355195946*t) - 1.39158642679427e+16*sin(0.0604259355195946*t) + 1.58248173181142e+17*cos(0.0604259355195946*t) - 1.58248173181141e+17*cos(0.0604259355195946*t) - 992.50632138896

-5.4511230447614e+15*sin(0.0604259355195946*t) + 5.4511230447614e+15*sin(0.0604259355195946*t) - 6.19889822873824e+16*cos(0.0604259355195946*t) + 6.19889822873801e+16*cos(0.0604259355195946*t) + 2322.98869660673

2.22100528352537e+17*sin(0.0604259355195946*t) - 2.22100528352537e+17*sin(0.0604259355195946*t) + 2.52567876472623e+18*cos(0.0604259355195946*t) - 2.52567876472624e+18*cos(0.0604259355195946*t) + 9453.78414414412


5.64447892403707e+18*sin(0.0604259355195946*t) - 5.64447892403707e+18*sin(0.0604259355195946*t) - 4.96358352777011e+17*cos(0.0604259355195946*t) + 4.96358352777011e+17*cos(0.0604259355195946*t)

2.94020669550533e+17*sin(0.0604259355195946*t) - 2.94020669550531e+17*sin(0.0604259355195946*t) - 2.58552857021064e+16*cos(0.0604259355195946*t) + 2.58552857021064e+16*cos(0.0604259355195946*t)

-1.15173791333625e+17*sin(0.0604259355195946*t) + 1.15173791333621e+17*sin(0.0604259355195946*t) + 1.01280338041468e+16*cos(0.0604259355195946*t) - 1.01280338041468e+16*cos(0.0604259355195946*t)

4.69264034172663e+18*sin(0.0604259355195946*t) - 4.69264034172664e+18*sin(0.0604259355195946*t) - 4.12656555466144e+17*cos(0.0604259355195946*t) + 4.12656555466144e+17*cos(0.0604259355195946*t)


1.92838711187019



1 -- y_1, 2 -- y_2, 3 -- y_3, 4 -- I(p_k), 5 -- k, 6 -- Delta p_k, 7 -- p, 8 -- ||Delta p_k+1||
0
0.134797701618188/exp(-0.597948158287991*t)**1.0 + 0.308461663245157 + 0.556740635136655*exp(-0.597948158287991*t)

0.23139470697914/exp(-0.597948158287991*t)**1.0 - 0.18709969737821 + 0.95570499039907*exp(-0.597948158287991*t)

-0.319469034578079/exp(-0.597948158287991*t)**1.0 + 1.31946903457808*exp(-0.597948158287991*t)

1.61809121691772

0

[[-0.0986258226572401]
 [0.121310477541215]
 [2.34768197386978]
 [-0.102301679238594]]

Matrix([[0.271374177342760], [0.731310477541215], [3.21768197386978], [0.507698320761406]])

8.23790692786466


1
0.256165812690505/exp(-0.718915296535568*t)**1.0 - 0.810297848827569 + 1.55413203613707*exp(-0.718915296535568*t)

0.0989564551779589/exp(-0.718915296535568*t)**1.0 + 0.300684755491961 + 0.60035878933008*exp(-0.718915296535568*t)

-0.197359382750572/exp(-0.718915296535568*t)**1.0 + 1.19735938275057*exp(-0.718915296535568*t)

3.19154910974086

1

[[-0.470406197655979]
 [1.01146696920561]
 [-8.11283627114685]
 [-0.894790908054768]]

Matrix([[-0.199032020313219], [1.74277744674683], [-4.89515429727707], [-0.387092587293362]])

0.289304112504268


2
3.20300395772069*sin(0.443207303190646*t) + 11.156455850307*cos(0.443207303190646*t) - 10.156455850307

0.620106516746784*sin(0.443207303190646*t) + 2.15990709593011*cos(0.443207303190646*t) - 1.15990709593012

-3.48312271778962*sin(0.443207303190646*t) + 1.0*cos(0.443207303190646*t)

3.14477435944387

2

[[-0.00256204800624939]
 [-0.00541563169112456]
 [0.288893698583309]
 [-0.0141918030615456]]

Matrix([[-0.201594068319469], [1.73736181505570], [-4.60626059869376], [-0.401284390354908]])

0.372163266540864


3
2.81175989061332*sin(0.475081666141064*t) + 9.08940601022549*cos(0.475081666141064*t) - 8.08940601022549

0.599711454803618*sin(0.475081666141064*t) + 1.93865092104435*cos(0.475081666141064*t) - 0.938650921044353

-3.2326394727264*sin(0.475081666141064*t) + 1.0*cos(0.475081666141064*t)

3.36104575925264

3

[[-0.00557155240923998]
 [-0.310342573840411]
 [0.204455897759723]
 [-0.0189664835826879]]

Matrix([[-0.207165620728709], [1.42701924121529], [-4.40180470093403], [-0.420250873937595]])

6.61005922692303


4
3.17803245513697*sin(0.401670965067553*t) + 9.65151761908084*cos(0.401670965067553*t) - 8.65151761908084

0.742842143059835*sin(0.401670965067553*t) + 2.25597256577695*cos(0.401670965067553*t) - 1.25597256577695

-3.03694746838728*sin(0.401670965067553*t) + 1.0*cos(0.401670965067553*t)

2.03581440017613

4

[[0.163235537193065]
 [-0.695938598819597]
 [6.55474616250192]
 [0.466057243980761]]

Matrix([[-0.0439300835356441], [0.731080642395694], [2.15294146156789], [0.0458063700431652]])

0.000118016337308668
'''