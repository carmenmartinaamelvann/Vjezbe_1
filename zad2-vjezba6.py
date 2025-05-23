import numpy as np
from Vjezba6_harmonijskioscilator import HarmonicOscillator
masa=1.0
k=6.0
x0=2.0
v0=0.0
oscc=HarmonicOscillator(masa, k, x0, v0)
T_anal=2*np.pi/oscc.omega
dt_vrijed=[0.5, 0.1, 0.04, 0.02, 0.001 ]
print('dt,  T_num,   greska')
for dt in dt_vrijed:
    t=np.arange(0, 20, dt)
    T_num=oscc.num_period(t)
    if T_num is None:
        print(f'{dt:.3f}        Nije pronađeno')
    else:
        greska=abs(T_num- T_anal)
        print(f'(dt:.3f) {T_num:.5f}    {greska:.5f}')
