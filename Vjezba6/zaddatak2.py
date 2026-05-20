import numpy as np
def izracunaj(mjerenja):
    srednja_vrijednost=np.mean(mjerenja)
    broj=len(mjerenja)
    kvadrat_odstupanja=(mjerenja- srednja_vrijednost)**2
    sigma=np.sqrt(np.sum(kvadrat_odstupanja))/(broj-1)
    return float(srednja_vrijednost), float(sigma)
def volumen_valjka(R, L):
    return (R**2)*np.pi*L
def sigma_volumena(R, sigma_R, L, sigma_L):
    derivacija_za_R=2*R*np.pi*L
    derivacija_za_L=(R**2)*np.pi
    za_R=(derivacija_za_R*sigma_R)**2
    za_L=(derivacija_za_L*sigma_L)**2
    return float(np.sqrt(za_R + za_L))
R1=np.array([19.98, 20.18, 20.10, 20.08, 19.74])/20
R2=np.array([19.92, 19.82, 19.96, 19.98, 19.88])/20
R3=np.array([24.96, 24.98, 24.98, 24.92, 24.94])/20
L1=np.array([49.80, 49.00, 50.48, 49.80, 49.96])/10
L2=np.array([52.56, 52.50, 52.62, 52.58, 52.54])/10
L3=np.array([55.34, 55.40, 55.30, 55.44, 55.48])/10
R1_sred, sigma_R1= izracunaj(R1)  
L1_sred, sigma_L1= izracunaj(L1)
Volumen_1=volumen_valjka(R1_sred,  L1_sred)
Sigma_volumen_1=sigma_volumena(R1_sred, sigma_R1, L1_sred, sigma_L1)
R2_sred, sigma_R2= izracunaj(R2)
L2_sred, sigma_L2= izracunaj(L2)
Volumen_2=volumen_valjka(R2_sred, L2_sred)
Sigma_volumen_2=sigma_volumena(R2_sred, sigma_R2, L2_sred, sigma_L2)
R3_sred, sigma_R3= izracunaj(R3)
L3_sred, sigma_L3= izracunaj(L3)
Volumen_3=volumen_valjka(R3_sred, L3_sred)
Sigma_volumen_3=sigma_volumena(R3_sred, sigma_R3, L3_sred, sigma_L3)
print(f'V_1= {Volumen_1:.3e} cm**3')
print(f'V_1_sigma= {Sigma_volumen_1:.3e} cm**3')

print(f'V_2= {Volumen_2:.3e} cm**3')
print(f'V_2_sigma= {Sigma_volumen_2:.3e} cm**3')
print(f'V_3= {Volumen_3:.3e} cm**3')
print(f'V_3_sigma= {Sigma_volumen_3:.3e} cm**3')



