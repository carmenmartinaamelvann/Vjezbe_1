import math
import matplotlib.pyplot as plt
M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
kut=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
broj=len(M)
xy=0
x_kvadr=0
y_kvadr=0
for i in range(broj):
    xy+=kut[i]*M[i]
    x_kvadr+=kut[i]**2
    y_kvadr+=M[i]**2
xy_aritm=xy/broj
x_kvadr_aritm=x_kvadr/broj
y_kvadr_aritm=y_kvadr/broj
koef_a=xy_aritm/x_kvadr_aritm
stand_pogre=math.sqrt((1/broj)*((y_kvadr_aritm/x_kvadr_aritm)-koef_a**2))
print(f'Dt= {koef_a} Nm/rad')
print(f'stand_pogre= {stand_pogre}')
plt.scatter(kut, M, color='green')
plt.plot(kut, [koef_a*k for k in kut], color='magenta')
plt.show()

