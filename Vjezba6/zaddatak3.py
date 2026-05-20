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
def gustoca_valjka(m, V):
    return m/V
def sigma_gustoce_valjka(m, sigma_m, V, sigma_V):

    derivacija_za_m=1/V
    derivacija_za_V=-m/(V**2)
    za_m=(derivacija_za_m*sigma_m)**2
    za_V=(derivacija_za_V*sigma_V)**2
    return float(np.sqrt(za_m+ za_V))
V_1,sigma_V1= 1.567e+01, 1.571e-01
V_2, sigma_V2= 1.637e+01, 5.322e-02
V_3, sigma_V3=2.709e+01, 3.346e-02
m1=np.array([138.92, 138.98, 139.20, 138.90, 138.92])
m2=np.array([128.65, 128.60, 128.65, 128.35, 128.50])
m3=np.array([71.89, 71.90, 71.79, 71.85, 71.70])
m1_sred, sigma_m1= izracunaj(m1)
gustoca_1=gustoca_valjka(m1_sred, V_1)
sigma_gustoca_1=sigma_gustoce_valjka(m1_sred, sigma_m1, V_1, sigma_V1)
m2_sred, sigma_m2= izracunaj(m2)
gustoca_2=gustoca_valjka(m2_sred, V_2)
sigma_gustoca_2=sigma_gustoce_valjka(m2_sred, sigma_m2, V_2, sigma_V2)
m3_sred, sigma_m3= izracunaj(m3)
gustoca_3=gustoca_valjka(m3_sred, V_3)
sigma_gustoca_3=sigma_gustoce_valjka(m3_sred, sigma_m3, V_3, sigma_V3)
print(f'gustoca1= {gustoca_1:.3e}g/cm**3')
print(f'sigma_gustoca_1= {sigma_gustoca_1:.3e}g/cm**3')
print(f'gustoca2= {gustoca_2:.3e}g/cm**3')
print(f'sigma_gustoca_2= {gustoca_2:.3e}g/cm**3')
print(f'gustoca3= {gustoca_3:.3e}g/cm**3')
print(f'sigma_gustoca_3= {sigma_gustoca_3:.3e}g/cm**3')


