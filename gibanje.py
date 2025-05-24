from Particle import Particle
import numpy as np
v0=10
kut=25
x=0
y=0
pp=Particle(v0, x, y, kut)
num_dom=pp.range()
print(f'Domet je: {num_dom}')
anal_dom=((v0**2)*np.sin(2*np.radians(kut)))/9.81
ods=abs(anal_dom-num_dom)
print(ods)
pp.plot_trajectory()
pp.reset()
