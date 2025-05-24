import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self, v0, x0=0, y0=0, kut=25):
        
                
        
        self.v0=v0
        self.poc_x=x0
        self.poc_y=y0
        self.kut=np.radians(kut)
        self.trenutn_x=x0
        self.trenutn_y=y0
        self.vx=v0*np.cos(self.kut)
        self.vy=v0*np.sin(self.kut)
        self.gravitacija=9.81
        self.t=0

    def reset(self):
            del self.v0
            del self.poc_x
            del self.poc_y
            del self.kut
            del self.trenutn_x
            del self.trenutn_y
            del self.vx
            del self.vy
            del self.t
            del self.gravitacija
    def _move(self, dt):
            self.trenutn_x+=self.vx*dt
            self.trenutn_y+=self.vy*dt
            self.vy-=self.gravitacija*dt
            self.t+=dt
    def range(self, dt=0.01):
            x=self.poc_x
            y=self.poc_y
            vx=self.vx
            vy=self.vy
            t=self.t
            while self.trenutn_y>=0:
                self._move(dt)            
            domet=self.trenutn_x
            self.trenutn_x=x
            self.trenutn_y=y
            self.vx=vx
            self.vy=vy
            self.t=t
            return domet
    def plot_trajectory(self, dt=0.01):
            x=self.trenutn_x
            y=self.trenutn_y
            vx=self.vx
            vy=self.vy
            t=self.t
            x_v=[self.trenutn_x]
            y_v=[self.trenutn_y]
            while self.trenutn_y>=0:
                self._move(dt)
                x_v.append(self.trenutn_x)
                y_v.append(self.trenutn_y)
            plt.plot(x_v, y_v)
            plt.xlabel('x (m)')
            plt.ylabel('y (m)')
            plt.title('Putanja')
            plt.grid()
            plt.show()
            self.no_trenutn=x
            self.no_trenutn=y
            self.vx=vx
            self.vy=vy
            self.t=t
                      


