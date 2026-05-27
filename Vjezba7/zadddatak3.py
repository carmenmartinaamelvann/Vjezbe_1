import numpy as np
np.random.seed(42)
mase_ciste=np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase=mase_ciste+ [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]
a=[3, 1, 4, 1, 5, 9, 2, 6]
b=[3, 1, 4, 1, 5, 9, 2, 6, 5]
def medijan(podaci):
    l=sorted(podaci)
    n=len(l)
    if n%2!=0:
        x=(n+1)//2
        return l[x-1]
    else:
        x_1=n//2
        x_2=(n//2)+1
        return (l[x_1-1]+ l[x_2-1])/2
print(medijan(a))
print(medijan(b))
print(medijan(mase))
print(np.median(a))
print(np.median(b))
print(np.median(mase))


    
