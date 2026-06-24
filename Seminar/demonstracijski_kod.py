import semiinar_kod as sk
v_poc=20
kut=45
print(' Crtanje putanje')
sk.prikaz_putanje(v_poc, kut, dt=0.0001)
maks_v=sk.maks_visina(v_poc, kut, dt=0.0001)
print(f'Maksimalna visina je {maks_v:.3f}m')
d=sk.domet(v_poc, kut, dt=0.0001)
print(f'Domet iznosi {d:.3f} m')
maks_brzi=sk.maks_brzina(v_poc, kut, dt=0.0001)
print(f'Maksimalna brzina iznosi : {maks_brzi:.3f} m/s')
print('Provjera je li meta pogođena ( Prvi slučaj) ')
sk.gadanje_mete(v_poc, kut, x_m=30, y_m=40, r_m=15)
print('Provjera je li meta pogođena (Drugi slučaj)')
sk.gadanje_mete(v_poc, kut, x_m=10, y_m=35, r_m=30)

