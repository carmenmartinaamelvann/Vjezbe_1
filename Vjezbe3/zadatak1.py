import matplotlib.pyplot as plt
import numpy as np
class Projectile:
    def __init__(self):
        self.x, self.y= [], []
        self.komp_x_brz, self.komp_y_brz= [], []
        self.t= []
        self.gravit_konst=9.81
        self.masa=None
        self.parametar_b=None
        self.dt=None
    def unosenje_vrijednosti(self, poc_brzina, kut, masa, parametar_b, dt):
        self.masa=masa
        self.parametar_b=parametar_b
        self.kutt=np.radians(kut)
        self.dt=dt
        self.x=[0.0]
        self.y=[0.0]
        self.komp_x_brz=[poc_brzina*np.cos(self.kutt)]
        self.komp_y_brz=[poc_brzina*np.sin(self.kutt)]
        self.t=[0.0]
    def pokreni(self):
        while self.y[-1]>=0:
            akc_x_smjer=-(self.parametar_b/self.masa)* self.komp_x_brz[-1]
            akc_y_smjer=-self.gravit_konst-(self.parametar_b/self.masa)* self.komp_y_brz[-1]
            novi_komp_x_brz=self.komp_x_brz[-1] + akc_x_smjer* self.dt
            novi_komp_y_brz=self.komp_y_brz[-1]+ akc_y_smjer* self.dt
            novi_x= self.x[-1]+ novi_komp_x_brz*self.dt
            novi_y= self.y[-1]+ novi_komp_y_brz*self.dt
            self.x.append(novi_x)
            self.y.append(novi_y)
            self.komp_x_brz.append(novi_komp_x_brz)
            self.komp_y_brz.append(novi_komp_y_brz)
            self.t.append(self.t[-1]+ self.dt)
poc_brzina_input=float(input())
kut_input=float(input())
masa_input=float(input())    
parametar_b_input=float(input())
plt.figure(figsize=(8, 6))
koraci_dt=[0.5, 0.2, 0.1, 0.01]
for k in koraci_dt:
    projektil= Projectile()
    projektil.unosenje_vrijednosti(poc_brzina_input, kut_input, masa_input, parametar_b_input, k)
    projektil.pokreni()
    plt.plot(projektil.x, projektil.y, label=f"dt= {k} s")
plt.title('Putanja')
plt.xlabel('Domet (x) [m]')
plt.ylabel('Visina (y) [m]')
plt.axhline(0, color='magenta', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()


