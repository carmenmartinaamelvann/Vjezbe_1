import calculus
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x**2
a, b=0, 1
k=[2, 5, 10, 40]
anal=1/3
rez_donja=[]
rez_gornja=[]
rez_trapez=[]
for n in k:
    d, g=calculus.pravokutna_integ(f, a, b, n)
    t=calculus.trapez_integ(f, a, b, n)
    rez_donja.append(d)
    rez_gornja.append(g)
    rez_trapez.append(t)
plt.figure(figsize=(8, 6))
plt.axhline(y=anal, color='k', linestyle='--', label='Analiticko rjesenje')
plt.plot(k, rez_donja, 'mo-', label='Donja pravokutna')
plt.plot(k, rez_gornja, 'ro-', label='Gornja pravokutna')
plt.plot(k, rez_trapez, 'bo-', label='Trapezna')
plt.xlabel('Broj koraka (n)')
plt.ylabel('Vrijednost integrala')
plt.title('Usporedba dviju metoda')
plt.legend()
plt.grid(True)
plt.show()
