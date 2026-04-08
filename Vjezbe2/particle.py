import matplotlib.pyplot as plt
import numpy as np
class Particle:
    def __init__(self, poc_brzina, kut, x_poc, y_poc):
        self.x_poc=x_poc
        self.y_poc=y_poc
        self.kut=np.radians(kut)
        self.poc_brzina=poc_brzina
        self.reset()
    def reset(self):
        self.x=[self.x_poc]
        self.y=[self.y_poc]
        self.brzina_x_komp=self.poc_brzina*np.cos(self.kut)
        self.brzina_y_komp=self.poc_brzina*np.sin(self.kut)
        self.t=[0]
        self.g_konst=9.81
    def __move(self, dt):
        x_pol=self.x[-1]+ self.brzina_x_komp*dt
        brzina_y=self.brzina_y_komp- self.g_konst*dt
        y_pol=self.y[-1]+ self.brzina_y_komp*dt
        self.brzina_x_komp=self.brzina_x_komp
        self.brzina_y_komp=brzina_y
        self.x.append(x_pol)
        self.y.append(y_pol)
        self.t.append(self.t[-1]+ dt)
    def range(self, dt=0.01):
        self.reset()
        while self.y[-1] >=0:
            self.__move(dt)
        return self.x[-1]
    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.xlabel( 'x [m]')
        plt.ylabel('y [m]')
        plt.title(' Putanja')
        plt.grid(True)
        plt.show()

        