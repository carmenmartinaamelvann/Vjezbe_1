import math
tocke=[2.0, 2.1, 4.5, 6.7, 8.8, 15.7, 22.9, 12.6, 7.7, 6.6]
suma=0
for i in tocke:
    suma+=i
broj_tocaka=len(tocke)
aritm_sred=suma/broj_tocaka
suma_kvadrata_razlike=0
for i in tocke:
    suma_kvadrata_razlike+=(i- aritm_sred)**2
sigma=math.sqrt(suma_kvadrata_razlike/(broj_tocaka*(broj_tocaka-1)))
print(aritm_sred)
print(sigma)
