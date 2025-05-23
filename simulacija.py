import Particle as pr
import matplotlib.pyplot as plt
import numpy as np
p1=pr.Particle(10, 40)
alfa=np.arange(0, 90, 2)
dt=0.01
dometi=np.zeros(len(alfa))
D_an=np.zeros(len(alfa))
for i in range(len(alfa)):
    p=pr.Particle(10, alfa[i])
    p.kosiHitac(0, 0, dt)
    dometi[i]=p1.domet
D_an=(p1.v0**2/9.81)*m.sin(2*m.radians(p1.alfa))
Err=100*(D_an-dometi)/D_an

plt.figure(figsize=(10, 10))
 
plt.xlabel('alfa [°]')
plt.ylabel('domet []')
plt.yscale('log') # čisto za probat
plt.show()

