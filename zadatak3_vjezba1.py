import numpy as np
import matplotlib.pyplot as plt
while True:
    unos_1=input().strip()
    razdijeli=unos_1.split()
    if len(razdijeli)==2 and razdijeli[0].lstrip('-').replace('.', '', 1).isdigit() and razdijeli[1].lstrip('-').replace('.', '', 1).isdigit():
        x1, y1=float(razdijeli[0]), float(razdijeli[1])
        break
    else:
        print('Pogreška')
while True:
    unos_2=input().strip()
    razdijeli_2=unos_2.split()
    if len(razdijeli_2)==2 and razdijeli_2[0].lstrip('-').replace('.', '', 1).isdigit() and razdijeli_2[1].lstrip('-').replace('.', '', 1).isdigit():
        x2, y2=float(razdijeli_2[0]), float(razdijeli_2[1])
        break
    else:
        print('Pogreška')
k=(y2-y1)/(x2-x1) #koeficijent smjera
z=y1-k*x1
print(f'Jednadžba pravc aje y={k:.0f}x+{z:.0f}')


     
