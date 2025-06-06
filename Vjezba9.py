import numpy as np
import matplotlib.pyplot as plt
masa_sunca=1.989e30
masa_zemlje=5.9742e24
grav_konst=6.67408e-11
astr_jed=1.486e11
v_komp_okom=29783
godina_u_sekundama=365.242*24*3600
r_zemlja=np.array([astr_jed, 0.0])
r_sunca=np.array([0.0, 0.0])
v_zemlja=np.array([0.0, v_komp_okom])
v_sunca=np.array([0.0, 0.0])
dt=3600
t_max=godina_u_sekundama
korak=int(t_max/dt)
putanja_zemlja=[]
putanja_sunca=[]
for i in range(korak):
    r=r_zemlja-r_sunca
    udaljen=(r[0]**2+ r[1]**2)**0.5
    smjer=r/udaljen
    F=grav_konst*masa_sunca*masa_zemlje/udaljen**2
    F_v=F*smjer

    akc_sunca=F_v/masa_sunca
    akc_zemlja=-F_v/masa_zemlje
    v_sunca+=akc_sunca*dt
    v_zemlja+=akc_zemlja*dt
    r_sunca+=v_sunca*dt
    r_zemlja+=v_zemlja*dt
    putanja_sunca.append(r_sunca.copy())
    putanja_zemlja.append(r_zemlja.copy())
putanja_sunca=np.array(putanja_sunca)
putanja_zemlja=np.array(putanja_zemlja)
plt.figure(figsize=(10, 8))
plt.plot(putanja_zemlja[:, 0], putanja_zemlja[:, 1], label='Zemlja')
plt.plot(putanja_sunca[:, 0], putanja_sunca[:, 1], label='Sunce')
plt.scatter([0], [0], color='yellow', s=100, label='Sunce(poč)')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Putanja Zemlje i Sunca')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()

