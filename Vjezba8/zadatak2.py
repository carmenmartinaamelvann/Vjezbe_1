import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
kut_deg=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
T_120=[0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153, 0.9293, 0.9653, 0.9747, 1.0200, 1.0373, 1.1160, 1.1780, 1.2733, 1.4180, 1.6373, 1.9100, 2.5460]
T_240=[1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320, 1.1440, 1.1720, 1.1980, 1.2293, 1.2813, 1.3573, 1.4200, 1.5600, 1.7413, 1.9840, 2.4473, 3.1573]
kut_r=np.radians(kut_deg)
gravit_konst=9.81
def T_t(theta, L):
    return 2*np.pi*np.sqrt(L/(gravit_konst*np.cos(theta)))
argumenti120,_=curve_fit(T_t, kut_r, T_120)
L120_f=argumenti120[0]
argumenti240,_=curve_fit(T_t, kut_r, T_240)
L240_f=argumenti240[0]
print( f'F. duljina za L=120 mm : {L120_f} m')
print(f'F..duljina za L=240 mm : {L240_f} m')
theta=np.linspace(0, np.radians(85), 500)
T_t_120=T_t(theta, 0.120)
T_t_240=T_t(theta, 0.240)
T_f_120=T_t(theta, L120_f)
T_f_240=T_t(theta, L240_f)
plt.scatter(kut_deg, T_120, label='Mjereni podaci za kad je L= 120 mm')
plt.plot(np.degrees(theta), T_f_120, label='curve_fit za L= 120 mm')
plt.scatter(kut_deg, T_240, label='Mjereni podaci za kad je L= 240 mm')
plt.plot(np.degrees(theta), T_f_240, label='curve fit za L= 240 mm')
plt.plot(np.degrees(theta), T_t_120, '--', label= 'Teorijski za kad je L= 120 mm')
plt.plot(np.degrees(theta), T_t_240, '--', label='Teorijski za kad je L= 240 mm')
plt.xlabel('Kut theta ()')
plt.ylabel('Period T(s)')
plt.grid()
plt.legend()
plt.show()
delta120=abs(L120_f- 0.120)/0.120*100
delta240=abs(L240_f- 0.240)/0.240*100
print(delta120)
print(delta240)
   

