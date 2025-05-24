import numpy as np
import matplotlib.pyplot as plt
from calculus import (
    derivacija_u_točki,
    u_rasponu,
    aproksimacija_pravokutna,
    trapez_integracija
)
def kubična(x): return x**3
def trigon(x): return np.sin(x)
def deri_kubična(x): return 3*x**2
def deri_trigon(x): return np.cos(x)
rez_kub=u_rasponu(kubična, -2, 2, broj_točaka=100, h=0.0001, metodda='three-step')
x_kubična=[x for x, d in rez_kub]
y_kubična=[d for x, d in rez_kub]
rez_trig=u_rasponu(trigon, 0, 2*np.pi, broj_točaka=100, h=0.0001, metodda='two-step')
x_trigo=[x for x, d in rez_trig]
y_trigo=[d for x, d in rez_trig]
plt.figure(figsize=(8,6))
plt.plot(x_kubična, deri_kubična(np.array(x_kubična)), label='Analitička derivacija')
plt.plot(x_kubična, y_kubična, 'o', label='Numerička derivacija x**3, markersize=3')
plt.plot(x_trigo, deri_trigon(np.array(x_trigo)), label='Analitička derivacija sin(x) (three-step)', markersize=3)
plt.plot(x_trigo, y_trigo, 'o', label='Numerička derivacija sin(x) (two-step)',  markersize=3)
plt.title('Usporedba numeričke i analitičke integracije')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
def kvadratna(x): return x**2
a, b=0, 4
anal_int=(b**3- a**3)/3
broj_podjela_lista=[5, 10, 50, 100]
donje_mede=[]
gornje_mede=[]
trapez_rez=[]
for m in broj_podjela_lista:
    donja, gornja=aproksimacija_pravokutna(kvadratna, a, b, m)
    trapezna=trapez_integracija(kvadratna, a, b, m)
    donje_mede.append(donja)
    gornje_mede.append(gornja)
    trapez_rez.append(trapezna)
plt.figure(figsize=(8,6))
plt.plot(broj_podjela_lista, donje_mede, 'bo-', label='Donja medu (pravokutnu)')
plt.plot(broj_podjela_lista, gornje_mede, 'ro-', label='Gornja medu (pravokutna)')
plt.plot(broj_podjela_lista, trapez_rez, 'go-', label='Trapez metoda')
plt.axhline(anal_int, color='k', linestyle='--', label='Vrijednost analitička')
plt.title('Analitička vs numerička integracija (x**2)')
plt.xlabel('Broj podjela')
plt.ylabel('Vrijednost integrala')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
 
