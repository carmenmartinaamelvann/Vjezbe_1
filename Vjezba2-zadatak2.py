import numpy as np
import matplotlib.pyplot as plt
v_poc=float(input('Unesi početnu brzinu u m/s'))
kut_otklona=float(input('Unesi kut otklona u stupnjevima'))
kut_otklona_u_radijanima=np.radians(kut_otklona)
v_poc_x_komp=v_poc*np.cos(kut_otklona_u_radijanima)
v_poc_y_komp=v_poc*np.sin(kut_otklona_u_radijanima)
g=9.81
dt=0.01
vrijeme=np.linspace(0, 10, 1000)
x=np.zeros(1000)
y=np.zeros(1000)
v_x=np.full(1000, v_poc_x_komp)
v_y=np.full(1000, v_poc_y_komp)
for i in range(1, 1000):
    v_y[i]=v_y[i-1]-g*dt
    v_x[i]=v_x[i-1]
    
    x[i]=x[i-1]+ v_x[i-1]*dt
    y[i]=y[i-1]+v_y[i-1]*dt
    if y[i]<0:
        break
plt.figure(figsize=(14,8))
plt.subplot(3, 1, 1)
plt.plot(x[:i+1], y[:i+1])
plt.title('Putanja')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(vrijeme[:i+1], x[:i+1])
plt.title('x-t graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Y (m)')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(vrijeme[:i+1], y[:i+1])
plt.title('y-t graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Y (m)')
plt.grid()

plt.tight_layout()
plt.show()