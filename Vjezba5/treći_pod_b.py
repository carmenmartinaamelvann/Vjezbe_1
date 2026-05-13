import statistics
import math
tocke=[2.0, 2.1, 4.5, 6.7, 8.8, 15.7, 22.9, 12.6, 7.7, 6.6]
broj_tocaka=len(tocke)
aritm_sred=statistics.mean(tocke)
sigmaa=statistics.stdev(tocke)
sigma=sigmaa/math.sqrt(broj_tocaka)
print(aritm_sred)
print(sigma)
