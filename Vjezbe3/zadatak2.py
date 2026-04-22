import matplotlib.pyplot as plt
import numpy as np
class Projectile:
    def __init__(self):
        self.x, self.y= [], []
        self.komp_x_brz, self.komp_y_brz=[], []
        self.t=[]
        self.gravit_konst=9.81
        self.masa=None
        self.parametar_b=None
        self.dt=None
    def unosenje_vrijednosti(self, poc_brzina,kut, masa, parametar_b, dt):
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
            akc_x_smjer=-(self.parametar_b/self.masa)*self.komp_x_brz[-1]
            akc_y_smjer=-self.gravit_konst-(self.parametar_b/self.masa)*self.komp_y_brz[-1]
            novi_komp_x_brz=self.komp_x_brz[-1]+ akc_x_smjer*self.dt
            novi_komp_y_brz=self.komp_y_brz[-1]+ akc_y_smjer*self.dt
            novi_x=self.x[-1]+ novi_komp_x_brz*self.dt
            novi_y=self.y[-1]+ novi_komp_y_brz*self.dt
            self.x.append(novi_x)
            self.y.append(novi_y)
            self.komp_x_brz.append(novi_komp_x_brz)
            self.komp_y_brz.append(novi_komp_y_brz)
            self.t.append(self.t[-1]+ self.dt )
    def pokreni_range_kutta_4(self):
        while self.y[-1] >=0:
            h=self.dt
            k_1xkomp=(-(self.parametar_b/self.masa)*self.komp_x_brz[-1])
            k_2xkomp=-(self.parametar_b/self.masa)*(self.komp_x_brz[-1]+ k_1xkomp*h/2)
            k_3xkomp=-(self.parametar_b/self.masa)*(self.komp_x_brz[-1]+ k_2xkomp* h/2)
            k_4xkomp=-(self.parametar_b/self.masa)*(self.komp_x_brz[-1]+ k_3xkomp*h)
            novi_komp_x_brz= self.komp_x_brz[-1]+ (h/6)* (k_1xkomp+ 2*k_2xkomp+ 2*k_3xkomp+ k_4xkomp)
            k_1ykomp=-self.gravit_konst-(self.parametar_b/self.masa)* self.komp_y_brz[-1]
            k_2ykomp=-self.gravit_konst-(self.parametar_b/self.masa)* (self.komp_y_brz[-1]+ k_1ykomp*h/2)
            k_3ykomp=-self.gravit_konst-(self.parametar_b/self.masa)* (self.komp_y_brz[-1]+ k_2ykomp*h/2)
            k_4ykomp=-self.gravit_konst-(self.parametar_b/self.masa) * (self.komp_y_brz[-1]+ k_3ykomp*h)
            novi_komp_y_brz=self.komp_y_brz[-1]+ (h/6)* (k_1ykomp+ 2*k_2ykomp+ 2*k_3ykomp+ k_4ykomp)

            self.komp_x_brz.append(novi_komp_x_brz)
            self.komp_y_brz.append(novi_komp_y_brz)
            self.x.append(self.x[-1]+ novi_komp_x_brz*h)
            self.y.append(self.y[-1]+ novi_komp_y_brz*h)
            self.t.append(self.t[-1]+ h)
poc_brzina=float(input())
kut=float(input())
masa=float(input())
parametar_b=float(input())
dt_unijeti=0.01
plt.figure(figsize=(8, 6))
projektil_euler=Projectile()
projektil_euler.unosenje_vrijednosti(poc_brzina, kut, masa, parametar_b, dt_unijeti)
projektil_euler.pokreni()
plt.plot(projektil_euler.x, projektil_euler.y, linestyle='--')
projektil_range_kutta=Projectile()
projektil_range_kutta.unosenje_vrijednosti(poc_brzina, kut, masa, parametar_b, dt_unijeti)
projektil_range_kutta.pokreni_range_kutta_4()
plt.plot(projektil_range_kutta.x, projektil_range_kutta.y, color='magenta')
plt.title('Usporedba dviju metoda, Eulerove i Rang-Kuttove metode')
plt.xlabel('Domet (x) [m]')
plt.ylabel('Visina (y) [m]')
plt.axhline(0, color='blue', lw=1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()






             






        
    

