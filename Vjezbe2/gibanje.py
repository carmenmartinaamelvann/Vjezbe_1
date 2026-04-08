from particle import Particle
import numpy as np
poc_brzina=20
kut=45
x_poc, y_poc=0,0
g_konst=9.81
p=Particle(poc_brzina, kut, x_poc, y_poc)
racunanje_anal=(poc_brzina**2*np.sin(2*np.radians(kut)))/g_konst
racunanje_num=p.range(dt=0.01)
odst=abs(racunanje_anal-racunanje_num)
print(f'Analitički domet: {racunanje_anal: .3f} m')
print(f'Numerički domet: {racunanje_num: .3f} m')
print(f'Odstupanje: {odst: .5f} m')
p.plot_trajectory()
