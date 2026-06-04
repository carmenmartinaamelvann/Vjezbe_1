import numpy as np
import matplotlib.pyplot as plt
h0=0.54
m=0.5257
r=4.025e-3
h=[0.14, 0.17, 0.19, 0.22, 0.25, 0.28, 0.31, 0.34, 0.37, 0.40]
t_mean=[1.740, 1.793, 2.043, 2.190, 2.280, 2.417, 2.540, 2.640, 2.670, 2.813]
h=np.array(h)
t_mean=np.array(t_mean)
logh=np.log(h)
logt=np.log(t_mean)
br=len(logt)
a=(br*np.sum(logt*logh)- np.sum(logt)*np.sum(logh))/(br*np.sum(logt**2)-(np.sum(logt))**2)
b=(np.sum(logh)-a*np.sum(logt))/br
x_sred_jed=np.mean(logt)
y_sred_jed=np.mean(logh)
x2_sred_jed=np.mean(logt**2)
y2_sred_jed=np.mean(logh**2)
sigmaa1=np.sqrt((1/br)*((y2_sred_jed-y_sred_jed**2))/(x2_sred_jed-x_sred_jed**2)-a**2)
sigmab1=sigmaa1*np.sqrt(x2_sred_jed)
print(a)
print(b)
print(sigmaa1)
print(sigmab1)
plt.scatter(logt, logh, label='Mjerenja')
x=np.linspace(min(logt), max(logt), 100)
y=a*x+b
plt.plot(x, y, label='Pravac')
plt.xlabel('logt')
plt.ylabel('logh')
plt.title('Prvi graf')
plt.grid()
plt.legend()
plt.show()


t2=t_mean**2
br=len(t2)
a=(br*np.sum(t2*h)-np.sum(t2)*np.sum(h))/(br*np.sum(t2**2)-(np.sum(t2))**2)
b=(np.sum(h)-a*np.sum(t2))/br
x_sred_dva=np.mean(t2)
y_sred_dva=np.mean(h)
x2_sred_dva=np.mean(t2**2)
y2_sred_dva=np.mean(h**2)
sigmaa2=np.sqrt((1/br)*((y2_sred_dva-y_sred_dva**2)/(x2_sred_dva-x_sred_dva**2)-a**2))
sigmab2=sigmaa2*np.sqrt(x2_sred_dva)
print(a)
print(b)
plt.scatter(t2, h, label='Mjerenja')
x=np.linspace(min(t2), max(t2), 100)
y=a*x+b
plt.plot(x, y, label='Fitanje dva')
plt.xlabel('t**2')
plt.ylabel('h')
plt.title('Drugi graf')
plt.grid()
plt.legend()
plt.show()

aa=2*a
print(aa)
sigmaaaa=2*sigmaa2
print(sigmaa2)
gravit_konst=9.81
I_z=m*r**2*(gravit_konst/aa-1)
print(I_z)
sigmaI_z=(m*r**2*gravit_konst/aa**2)*sigmaaaa
print(sigmaI_z)

