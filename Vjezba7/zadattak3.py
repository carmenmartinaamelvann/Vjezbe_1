import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
mase_ciste=np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase=mase_ciste+[6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]
aritmeticka_sredina_1=np.mean(mase)
medijan_1=np.median(mase)
razlika_1=abs(aritmeticka_sredina_1- medijan_1)
aritmeticka_sredina_2=np.mean(mase_ciste)
medijan_2=np.median(mase_ciste)
razlika_2=abs(aritmeticka_sredina_2- medijan_2)
print(razlika_1)
print(razlika_2)
print(abs(aritmeticka_sredina_1-aritmeticka_sredina_2))
print(abs(medijan_1-medijan_2))
plt.hist(mase, bins=10, edgecolor='black')
plt.axvline(aritmeticka_sredina_1, label='Aritmetička sredina s pogreškama', color='magenta')
plt.axvline(aritmeticka_sredina_2, label='Aritmetička sredina bez pogreške', color='red')
plt.axvline(medijan_1, label='Medijan s pogreškom', color='purple')
plt.axvline(medijan_2, label='Medijan bez pogreške', color='green')
plt.xlabel('Masa')
plt.ylabel('Frekvencija')
plt.title('Histogram')
plt.legend()
plt.show()


