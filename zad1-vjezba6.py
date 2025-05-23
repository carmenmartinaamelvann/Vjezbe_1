import numpy as np
import matplotlib.pyplot as plt
from Vjezba6_harmonijskioscilator import HarmonicOscillator
masa=1.0
k=6.0
x0=0.0
v0=2.0
oscc=HarmonicOscillator(masa, k, x0, v0)
t=np.linspace(0, 10, 1000)
x=oscc.pomak(t)
v=oscc.brzina(t)
a=oscc.akceleracija(t)
plt.figure(figsize=(12,8))
plt.subplot(3, 1, 1)
plt.plot(t, x, color='blue')
plt.title('x-t graf')
plt.ylabel('x [m]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, v, color='orange')
plt.title('v-t graf')
plt.ylabel('v [m/s]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, a, color='red')
plt.title('a-t graf')
plt.xlabel('Vrijeme[s]')
plt.ylabel('a [m/s**2]')
plt.grid(True)
plt.tight_layout()
plt.show()
dt_vrijed=[0.5, 0.1, 0.04, 0.02, 0.001]
print('Preciznost numeričkog rješenja')
print(f'{'Korak dt':>10} | {'Maks.greska':>15}')
print('-'*30)
for dt in dt_vrijed:
    t=np.arrange(0, 10, dt)
    x_anal=oscc.pomak(t)
    x_num=oscc.numerički(t)
    max_pogrj=max(abs(x_anal-x_num))
    print(f'{dt:10.4f} {max_pogrj:15.2f}')
    





