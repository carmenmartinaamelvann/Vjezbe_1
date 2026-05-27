import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
mase_ciste=np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
aritm_sred=np.mean(mase_ciste)
medijan=np.median(mase_ciste)
print(f'Aritmetička sredina: {aritm_sred:.3f}')
print(f'Medijan: {medijan:.3f}')
plt.hist(mase_ciste, bins=10, color='magenta', edgecolor='blue', alpha=0.7, label='Histogram')
plt.axvline(aritm_sred, color='green', linestyle='--', linewidth=2, label=f'Aritmetička sredina ({aritm_sred:.3f})')
plt.axvline(medijan, color='red', linestyle='--', linewidth=2, label=f'medijan ({medijan:.3f})')
plt.xlabel('Masa zvijezde Sirius A')
plt.ylabel('Frekvencija')
plt.title('Hiatogram s ucrtanim vertikalnim linijama')
plt.grid(True)
plt.tight_layout()
plt.show()

