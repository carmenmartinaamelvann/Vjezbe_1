import numpy as np
import math
tocke=[2.0, 2.1, 4.5, 6.7, 8.8, 15.7, 22.9, 12.6, 7.7, 6.6]
broj_tocaka=len(tocke)
aritm_sred=np.mean(tocke)
sigma=np.std(tocke, ddof=1)/math.sqrt(broj_tocaka)
print(aritm_sred)
print(sigma)
