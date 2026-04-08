import calculus
import numpy as np
import matplotlib.pyplot as plt
def kubna(x):
    return x**3
def kubna_anal(x):
    return 3*x**2
def sinus(x):
    return np.sin(x)
def sinus_anal(x):
    return np.cos(x)
x_an, y_nu=calculus.derivacija_rasp(kubna, -2, 2, epsilon=0.001, metoda='three-step')
y_an=[kubna_anal(i) for i in x_an]
plt.figure(figsize=(10,6))
plt.subplot(1, 2, 1)
plt.plot(x_an, y_an, 'k-', label='Analiticka', lw=2)
plt.plot(x_an, y_nu, 'mo', label='Numericka', markersize=4, markevery=50)
plt.title('Derivacija kubne funkcije')
plt.legend(loc='upper center')
plt.grid(True)
x_sin, y_sin_nu=calculus.derivacija_rasp(sinus, 0, 2*np.pi, epsilon=0.001)
y_sin_an=[sinus_anal(i) for i in x_sin]
plt.subplot(1, 2, 2)
plt.plot(x_sin, y_sin_an, 'k-', label='Analiticka(derivacija sinusa)', lw=3)
plt.plot(x_sin, y_sin_nu, 'ro', label='Numericka(derivacija sinusa)', markersize=4, markevery=50)
plt.title('Derivacija sinus funkcije')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


