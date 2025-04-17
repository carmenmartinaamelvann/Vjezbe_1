import matplotlib.pyplot as plt
import math
kut=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
k=len(kut)
xy=[kut[i]*M[i] for i in range(k)]
x_2=[kut[i]**2 for i in range(k)]
y_2=[M[i]**2 for i in range(k)]

xy_s=sum(xy)/k
x_2s=sum(x_2)/k
y_2s=sum(y_2)/k
a=xy_s/x_2s
stand_devij_a=math.sqrt((y_2s/x_2s-a**2)/k)
print(f'Modul torzije Dt: {a:.4f} Nm/rad')
print(f'Standardna devijacija: {stand_devij_a:.4f} Nm/rad')
plt.plot(kut, M, 'ro', label='Podaci')
M_vrijed=[a*x for x in kut]
plt.plot(kut, M_vrijed, 'r-', label=f'Pravac: M= {a:.4f}*$\\varphi$')
plt.xlabel('Kut ($\\varphi$) (rad)')
plt.ylabel('Moment M (Nm)')
plt.title('Graf linearne regresije')
plt.legend()
plt.grid(True)
plt.show()

