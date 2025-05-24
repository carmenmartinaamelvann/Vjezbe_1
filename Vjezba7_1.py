import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, masa, površina, kut, v0, gravitacija=9.81, koeficijent_otpora=0.3, gustoća_zraka=1.2):

        
        self.masa=masa
        self.površina=površina
        self.kut=np.radians(kut)
        self.v0=v0
        self.gravitacija=gravitacija
        self.koeficijent_otpora=koeficijent_otpora
        self.gustoća_zraka=gustoća_zraka
        self.resetiraj()
    def resetiraj(self):
        self.x=0
        self.y=0
        self.vx=self.v0*np.cos(self.kut)
        self.vy=self.v0*np.sin(self.kut)
        self.putanja=[(self.x, self.y)]
    def zrak_otpor(self, vx, vy):
        v=(vx**2+vy**2)**0.5
        F=0.5*self.gustoća_zraka*self.koeficijent_otpora*self.površina
        a_x=-F*vx/(v*self.masa)
        a_y=-F*vy/(v*self.masa)
        return a_x, a_y
    def korak_euler(self, dt):
        a_x_zrak, a_y_zrak=self.zrak_otpor(self.vx, self.vy)
        a_x=a_x_zrak
        a_y=a_y_zrak-self.gravitacija
        self.vx+=a_x*dt
        self.vy+=a_y*dt
        self.x+=self.vx*dt
        self.y+=self.vy*dt
        self.putanja.append((self.x, self.y))
    def simuliraj_euler(self, dt):
        self.resetiraj()
        while self.y>=0:
            self.korak_euler(dt)
        return np.array(self.putanja)
    def korak_4rk(self, dt):
        def derivacije(vx, vy):
            a_x_zrak, a_y_zrak=self.zrak_otpor(vx, vy)
            return a_x_zrak, a_y_zrak-self.gravitacija
        k1_vx, k1_vy=derivacije(self.vx, self.vy)
        k1_x, k1_y=self.vx, self.vy
        vx2=self.vx+ 0.5*dt*k1_vx
        vy2=self.vy+ 0.5*dt*k1_vy
        k2_vx, k2_vy=derivacije(vx2, vy2)
        k2_x, k2_y=vx2, vy2
        vx3=self.vx+ 0.5*dt*k2_vx
        vy3=self.vy+ 0.5*dt*k2_vy
        k3_vx, k3_vy=derivacije(vx3, vy3)
        k3_x, k3_y=vx3, vy3
        vx4=self.vx+ dt*k3_vx
        vy4=self.vy+ 0.5*dt*k3_vy
        k4_vx, k4_vy=derivacije(vx4, vy4)
        k4_x, k4_y=vx4, vy4
        self.vx+=dt*(k1_vx+ 2*k2_vx+ 2*k3_vx+ k4_vx)/6
        self.vy+=dt*(k1_vy+ 2*k2_vy+ 2*k3_vy+ k4_vy)/6
        self.x+=dt*(k1_x+ 2*k2_x+ 2*k3_x+ k4_x)/6
        self.y+=dt*(k1_y+ 2*k2_y+ 2*k3_y+ k4_y)/6
        self.putanja.append((self.x, self.y))
        def simuliraj_4rk(self, dt):
            self.resetiraj()
            while self.y>=0:
                self.korak_4rk(dt)
            return np.array(self.putanja)
def testiranje_dt_vrijednosti():
        dt_vrijednosti=[0.1, 0.04, 0.01, 0.004]
        plt.figure(figsize=(8, 6))
        for dt in dt_vrijednosti:
            p=Projectile(masa=2, površina=0.01, kut=45, v0=40, koeficijent_otpora=0.3)
            putanja=p.simuliraj_euler(dt)
            plt.plot(putanja[:, 0], putanja[:, 1], label=f'dt={dt}')
        plt.xlabel('x(m)')
        plt.ylabel('y(m)')
        plt.title('Projektilova putanja za različite dt')
        plt.legend()
        plt.grid()
        plt.show()
def usporedivanje_metoda(dt=0.01):
        p_euler=Projectile(masa=2, površina=0.01, kut=45, v0=40, koeficijent_otpora=0.3)
        putanja_euler=p_euler.simuliraj_euler(dt)
        p_4rk=Projectile(masa=2, površina=0.01, kut=45, v0=40, koeficijent_otpora=0.3)
        putanja_4rk=p_4rk.simuliraj_4rk(dt)
        plt.figure(figsize=(8,6))
        plt.plot(putanja_euler[:, 0], putanja_euler[:, 1], '--', label='Metoda Eulerova')
        plt.plot(putanja_4rk[:,0], putanja_4rk[:, 1], '-', label='Metoda Range-Kutta četvrtog reda')
        plt.xlabel('x(m)')
        plt.ylabel('y(m)')
        plt.title('Usporedba  metoda')
        plt.legend()
        plt.grid()
        plt.show()
if __name__=='__main__':
    
    testiranje_dt_vrijednosti()
    usporedivanje_metoda(dt=0.01)

      





