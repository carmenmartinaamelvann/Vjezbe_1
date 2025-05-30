import numpy as np
import matplotlib.pyplot as plt
naboj_protona=1
naboj_elektrona=-1
masa=1
E=np.array([0.0, 0.0, 1.0])
B=np.array([0.0, 0.0, 1.0])
v_poc=np.array([1.0, 1.0, 1.0])
r_poc=np.array([0.0, 0.0, 0.0])
dt=0.01
t=30
n=int(t/dt)
def simulacija(naboj, v_poc, r_poc):
    v=v_poc.copy()
    r=r_poc.copy()
    x, y, z= [], [], []

    for i in range(n):

        B=np.array([0.0, 0.0, z_komponenta_magnetskog_polja])
        F=naboj*np.cross(v, B)
        a=F/masa
        v=v+ a*dt
        r=r+ v*dt
        x.append(r[0])
        y.append(r[1])
        z.append(r[2])
    return x, y, z
x_elektrona, y_elektrona, z_elektrona=simulacija(naboj_elektrona, v_poc, r_poc)
x_protona, y_protona, z_protona=simulacija(naboj_protona, v_poc, r_poc)
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(projection='3d')
ax.plot(x_elektrona, y-elektrona, z_elektrona, label='Elektron', color='red')
ax.plot(x_protona, y_protona, z_protona, label='Proton', color='green')
ax.set_title('Putanje čestica')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
