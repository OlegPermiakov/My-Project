from math import *

for i in range(1, 2):
    if i == 0:
        x1 = []
        x2 = []
        x3 = []
        n2 = []
        epsilon = 0.00001
        t = float(input("x_0 = "))
        while (i+1)/2 > t  or t > (i+1)*3/5:
            print(f"x_0 не в промежутке [{(i+1)/2};{(i+1)*3/5}]")
            t = float(input("x_0 = "))
        else:
            x1.append(t)
            x2.append(t)
            x3.append(t)
        t1 = float(input("Для методу хорд необхідно x_1 = "))
        while (i+1)/2 > t1  or t1 > (i+1)*3/5:
            print(f"x_1 не в промежутке [{(i+1)/2};{(i+1)*3/5}]")
            t1 = float(input("x_1 = "))
        else:
            x3.append(t1)
        delta = float(input("delta = "))
        while 0 > delta  or delta > 1:
            print("delta не в промежутке [0;1]")
            delta = float(input("delta = "))
        n2.append(x2[0]-i)
        n2.append(i+1-x2[0])
        
        def phi(r):
            res = r + r*(r**4 - 2*r**3 + r**2 - 2*r + 1)
            return res
        def pohidna_phi(r):
            res = 1 + (5*r**4 - 8*r**3 + 3*r**2 - 4*r + 1)
            return res
        def f(r):
            res = r**4 - 2*r**3 + r**2 - 2*r + 1
            return res
        def pohidna_f(r):
            res = 4*r**3 - 6*r**2 + 2*r - 2
            return res
        def pohidna2_f(r):
            res = 12*r**2 - 12*r + 2
            return res
        
        m1 = []
        for i in range(26):
            m1.append(abs(pohidna_f(0.5 + i/100)))
        m11 = min(m1)
        
        M2 = []
        for i in range(26):
            M2.append(abs(pohidna2_f(0.5 + i/100)))
        M22 = max(M2)
        
        r = []
        for i in range(0, 101):
            resq = abs(pohidna_phi(i/100))
            if resq > 0 and resq < 1:
                r.append(resq)
        q1 = max(r)
        if q1 > 1 or q1 < 0:
            break
        
        y = abs(phi(x1[0])-x1[0])
        z = delta*(1- q1)
        n = ceil(log(y/((1- q1)*epsilon))/log(1/ q1))+1
        q = (M22*max(n2))/(2*m11)
        if q > 1 or q < 0:
            break
        n1 = ceil(log2(log(max(n2)/epsilon)/log(1/ q)))+1
        
        print("k           x_k           x_k-(x_k-1)           f(x_k)")
        for j in range(1, n):
            cv = phi(x1[j-1])
            x1.append(cv)
            print(j, f"      {cv:1.10f}     {cv-x1[j-1]:1.10f}     {f(cv):1.10f}")
        print()
        print("k           x_k           x_k-(x_k-1)           f(x_k)")
        for j in range(1, n1):
            cv = x2[j-1] - f(x2[j-1])/pohidna_f(x2[0])
            x2.append(cv)
            print(j, f"      {cv:1.10f}     {cv-x2[j-1]:1.10f}     {f(cv):1.10f}")
        print()
        print("k           x_k           x_k-(x_k-1)           f(x_k)")
        for j in range(2, n1+1):
            cv = x3[j-1] - ((x3[j-1] - x3[j-2]) * f(x3[j-1]))/(f(x3[j-1]) - f(x3[j-2]))
            x3.append(cv)
            print(j-1, f"      {x3[j-1]:1.10f}     {x3[j-1]-x3[j-2]:1.10f}     {f(x3[j-1]):1.10f}")
        print(j, f"      {x3[j]:1.10f}     {x3[j]-x3[j-1]:1.10f}     {f(x3[j]):1.10f}")
        print()


        print(f"Найбільший додатний дійсний корінь методом простої ітерації скаладає: {max(x1):1.10f}")
        print(f"Найбільший додатний дійсний корінь модифікованим методом Ньютона скаладає: {max(x2):1.10f}")
        print(f"Найбільший додатний дійсний корінь методом хорд скаладає: {max(x3):1.10f}")
    
    else:
        x1 = []
        x2 = []
        x3 = []
        n2 = []
        epsilon = 0.00001
        t = float(input("x_0 = "))
        while 7*i/4 > t or t > i+1:
            print(f"x_0 не в промежутке [{7*i/4};{i+1}]")
            t = float(input("x_0 = "))
        else:
            x1.append(t)
            x2.append(t)
            x3.append(t)
        t1 = float(input("Для методу хорд необхідно x_1 = "))
        while 7*i/4 > t1  or t1 > i+1:
            print(f"x_1 не в промежутке [{7*i/4};{i+1}]")
            t1 = float(input("x_1 = "))
        else:
            x3.append(t1)
        delta = float(input("delta = "))
        while 0 > delta  or delta > 1:
            print("delta не в промежутке [0;1]")
            delta = float(input("delta = "))
        n2.append(x2[0]-7*i/4)
        n2.append(i+1-x2[0])

        def phi(r):
            res = (2*r**3 - r**2 + 2*r - 1)**0.25
            return res
        def pohidna_phi(r):
            res = ((3*r**2)/2 - (r/2) + 0.5)/((2*r + 2*r**3 - r**2 - 1)**0.75)
            return res
        def f(r):
            res = r**4 - 2*r**3 + r**2 - 2*r + 1
            return res
        def pohidna_f(r):
            res = 4*r**3 - 6*r**2 + 2*r - 2
            return res
        def pohidna2_f(r):
            res = 12*r**2 - 12*r + 2
            return res
        
        m1 = []
        for i in range(26):
            m1.append(abs(pohidna_f(1.75 + i/100)))
        m11 = min(m1)
        
        M2 = []
        for i in range(26):
            M2.append(abs(pohidna2_f(1.75 + i/100)))
        M22 = max(M2)

        
        r = []
        for i in range(100, 201):
            resq = abs(pohidna_phi(i/100))
            if resq > 0 and resq < 1:
                r.append(resq)
        q1 = max(r)
        if q1 > 1 or q1 < 0:
            break

        y = abs(phi(x1[0])-x1[0])
        z = delta*(1- q1)
        n = ceil(log(y/((1- q1)*epsilon))/log(1/ q1))+2
        q = (M22*max(n2))/(2*m11)
        if q > 1 or q < 0:
            break
        n1 = ceil(log2(log(max(n2)/epsilon)/log(1/ q1)))+2

        
        print("k           x_k           x_k-(x_k-1)           f(x_k)")
        for j in range(1, n):
            cv = phi(x1[j-1])
            x1.append(cv)
            print(j, f"      {cv:1.10f}     {cv-x1[j-1]:1.10f}     {f(cv):1.10f}")
        print()
        print("k           x_k           x_k-(x_k-1)           f(x_k)")
        for j in range(1, n1):
            cv = x2[j-1] - f(x2[j-1])/pohidna_f(x2[0])
            x2.append(cv)
            print(j, f"      {cv:1.10f}     {cv-x2[j-1]:1.10f}     {f(cv):1.10f}")
        print()
        print("k           x_k           x_k-(x_k-1)           f(x_k)")
        for j in range(2, n1+1):
            cv = x3[j-1] - ((x3[j-1] - x3[j-2]) * f(x3[j-1]))/(f(x3[j-1]) - f(x3[j-2]))
            x3.append(cv)
            print(j-1, f"      {x3[j-1]:1.10f}     {x3[j-1]-x3[j-2]:1.10f}     {f(x3[j-1]):1.10f}")
        print(j, f"      {x3[j]:1.10f}     {x3[j]-x3[j-1]:1.10f}     {f(x3[j]):1.10f}")
        print()
        
        print(f"Найбільший додатний дійсний корінь методом простої ітерації скаладає: {max(x1):1.10f}")
        print(f"Найбільший додатний дійсний корінь модифікованим методом Ньютона скаладає: {max(x2):1.10f}")
        print(f"Найбільший додатний дійсний корінь методом хорд скаладає: {max(x3):1.10f}")