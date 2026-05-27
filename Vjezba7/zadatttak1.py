import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
mase_ciste=np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
def histogram(podaci, k):
    x_min=min(podaci)
    x_max=max(podaci)
    h=(x_max- x_min)/k
    rubovi=[x_min + i*h for i in range(k+1)]
    rubovi[-1]=x_max
    f=[0]*k
    for x in podaci:
        for i in range(k):
            if i< k-1:
                if rubovi[i]<=x<rubovi[i+1]:
                    f[i]+=1
                    break
            else:
                if rubovi[i]<=x<=rubovi[i+1]:
                    f[i]+=1
                    break
    print('Tekstualni prikaz histograma:')
    for i in range(k):
        print(f'[{rubovi[i]:.2f}], {rubovi[i+1]:.2f}: {f[i]}')
        return rubovi, f
k_br=10
rubovi, f=histogram(mase_ciste, k_br)
sred=[]
for i in range(len(rubovi)-1):
    sredi=(rubovi[i]+ rubovi[i+1])/2
    sred.append(sredi)
sir=(rubovi[1]- rubovi[0])*0.9
plt.bar(sred, f, width=sir, color='magenta', edgecolor='black',  align='center')
plt.xlabel('Masa zvijezede Sirius')
plt.ylabel('Frekvencija')
plt.title('Histogram')
plt.xticks(rubovi, labels=[f'{r:.2f}' for r in rubovi])
plt.grid(True)
plt.tight_layout()
plt.show()

 

