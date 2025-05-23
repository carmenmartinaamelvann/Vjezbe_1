import numpy as np
import matplotlib.pyplot as plt
from Vjezba5 import (
    derivacija_u_točki,
    u_rasponu,
    aproksimacija_pravokutna,
    trapez_integracija
)
def kubična(x): return x**3
def trigon(x): return np.sin(x)

def deri_kubična(x): return 3*x**2
def deri_trigon(x): return np.cos(x)

rezultat_kubična=u_rasponu(kubična, -2, 2, broj_točaka=100, h=0.0001, metodda='three-step')
x_kubična=[x for x, r in rezultat_kubična]
y_kubična=[r for x , r in rezultat_kubična]
rez_trig=u_rasponu(trigon, 0, 2*np.pi, broj_točaka=100, h=0.0001, meetodda='two-step')
x_trig=[x for x, r in rez_trig]
y_trig=[r for x , r in rez_trig]
plt.figure(figsize=(10,15))
plt.plot(x_kubična, deri_kubična(np.array(x_kubična)), label='Analitička derivacija x**3')
plt.plot(x_kubična, y_kubična, 'o', label='Numerička derivacija x**3 (three-step)', markersize=3)
plt.plot(x_trig, d(eri_trigon(np.array(x_trig)), label='Analitička derivacija sin(x)'))
plt.plot(x_trig, y_trig, 'o', label='Numerička derivacija sin(x) (two-step)', markersize=3)

plt.title('Usporedba numeričke i analitičke derivacije')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.tight_layout()
plt.show()
 def kvadratna(x): return x**2
 a, b=0, 3
 integral_an=(b**3- a**3)/3
broj_podjela_lista=[5, 10, 50, 100]
donje_mede=[]
gornje_mede=[]
trapezn_rez=[]
for m in broj_podjela_lista:
 donja, gornja=aproksimacija_pravokutna(kvadratna, a, b, m)
 trapeza=trapez_integracija(kvadratna, a, b, n)
 donje_mede.append(donja)
 gornje_mede.append(gornja)
 trapezn_rez.append(trapeza)
 plt.figure(figsize=(8,15))
 plt.plot(broj_podjela_lista, donje_mede, 'bo-', label='Donju medu(pravokutna)')
 plt.plot(broj_podjela_lista, gornje_mede, 'ro-', label ='Gornja medu (pravokutna)')
 plt.plot(broj_podjela_lista, trapezn_rez, 'go-', label='Trapezna metoda')
 plt.axhline(integral_an, color='k', linestyle='--', label='Analitička vrijednost')
 plt.title('Numerička vs. analitička integracija (x**2)')
 plt.xlabel('Broj podjela')
 plt.ylabel('vrijednost integrala')
 plt.legend()
 plt.grid(True)
 plt.show()
 
 