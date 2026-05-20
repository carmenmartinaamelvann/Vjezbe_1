import numpy as np
def izracunaj(mjerenja):
    srednja_vrijednost=np.mean(mjerenja)
    broj=len(mjerenja)
    kvadrat_odstupanja=(mjerenja- srednja_vrijednost)**2
    sigma=np.sqrt(np.sum(kvadrat_odstupanja))/(broj-1)
    return float(srednja_vrijednost), float(sigma)
radijus_1=np.array([19.98, 20.18, 20.10, 20.08, 19.74])/2
radijus_2=np.array([19.92, 19.82, 19.96, 19.98, 19.88])/2
radijus_3=np.array([24.96, 24.98, 24.98, 24.92, 24.94])/2
duljina_1=np.array([49.80, 49.00, 50.48, 49.80, 49.96])
duljina_2=np.array([52.56, 52.50, 52.62, 52.58, 52.54])
duljina_3=np.array([55.34, 55.40, 55.30, 55.44, 55.48])
masa_1=np.array([138.92, 138.98, 139.20, 138.90, 138.92])
masa_2=np.array([128.65, 128.60, 128.65, 128.35, 128.50])
masa_3=np.array([71.89, 71.90, 71.79, 71.85, 71.70])
print('R_1=', izracunaj(radijus_1))
print('R_2=', izracunaj(radijus_2))
print('R_3=', izracunaj(radijus_3))
print('L_1=', izracunaj(duljina_1))
print('L_2=', izracunaj(duljina_2))
print('L_3=', izracunaj(duljina_3))
print('m_1=', izracunaj(masa_1))
print('m_2', izracunaj(masa_2))
print('m_3=', izracunaj(masa_3))


