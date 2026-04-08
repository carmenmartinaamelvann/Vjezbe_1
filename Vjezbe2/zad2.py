import matplotlib.pyplot as plt
import numpy as np
from particle import Particle
poc_brzina=10
kut=60
g_konst=9.81
kutt=np.radians(kut)
racunanje_anal=(poc_brzina**2*np.sin(2*kutt))/g_konst
l=np.linspace(0.0001, 0.1, 100)
rel_pog=[]
for dt in l:
    p=Particle(poc_brzina, kut, 0, 0)
    racunanje_num=p.range(dt)
    pog=abs(racunanje_anal-racunanje_num)/racunanje_anal
    rel_pog.append(pog)
plt.plot(l, rel_pog, 'mo-')
plt.xlabel('dt [s]')
plt.ylabel('Relativna pogreska')
plt.title('Graf ovisnosti relativne pogreške numeričkog rješenja o vrijednosti vremenskog koraka')
plt.grid(True)
plt.show()
