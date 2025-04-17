n=int(input())
brojevi=[]
for i in range(n):
    broj=float(input(f'Broj {i+1}:'))
    brojevi.append(broj)
suma=0
for x in brojevi:
    suma=suma+x
aritmetička_sredina=suma/n

odstupanje=0
for x in brojevi:
    odstupanje=odstupanje+((x-aritmetička_sredina)**2)
standardna_devijacija=(odstupanje/(n*(n-1)))**0.5
print(f'\nAritmetička sredina: {aritmetička_sredina:.2f}')
print(f'Standardna devijacija: {standardna_devijacija:.2f}')
 
