import numpy as np
import matplotlib.pyplot as plt
F=float(input('Unesi silu u njutnima'))
m=float(input('Unesi masu čestice u kilogramima'))
a=F/m                #a-akceleracija
dt=0.1
vrijeme=np.arange(0, 10+dt, dt)
v=[0]
x=[0]
akceleracijjaa=[a]
for i in range(1, len(vrijeme)):
    v_nova=v[i-1]+a*dt
    x_novi=x[i-1]+v[i-1]*dt
    v.append(v_nova)
    x.append(x_novi)
    akceleracijjaa.append(a)
plt.figure(figsize=(10,8))
plt.subplot(3, 1, 1)
plt.plot(vrijeme, x)
plt.title('x-t graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Položaj (m)')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(vrijeme, v, color='blue')
plt.title('v-t graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Brzina (m/s)')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(vrijeme, akceleracijjaa, color='purple')
plt.title('a-t graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Akceleracija (m/s**2)')
plt.grid()

plt.tight_layout()
plt.show()






