from Particle import Particle
import numpy as np
import matplotlib.pyplot as plt
v0=10
x=0
y=0
kut=60
pp=Particle(v0, x, y, kut)
greska=[]
dtu=[]
dt=0
while dt<=1:
    dt+=0.001
    dtu.append(dt)
    pp=Particle(v0, x, y, kut)
    num_dom=pp.range(dt)
    anal_dom=((v0**2)*np.sin(2*np.radians(kut)))/9.81
    ods=abs(anal_dom- num_dom)
    greska.append((ods/anal_dom)*100)
plt.plot(dtu, greska)
plt.xlabel('dt(s)')
plt.ylabel('greska(%)')
plt.title('Relativna greska')
plt.ylim(-1, max(greska)+5)
plt.grid()
plt.show()