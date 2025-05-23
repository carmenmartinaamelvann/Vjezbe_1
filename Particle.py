import numpy as np
import matplotlib.pyplot as plt
import math as m
class Particle:
    def __init__(self, v0, alfa):
        self.v0=v0
        self.alfa=alfa
        self.x0=x0
        self.y0=y0

        
    def kosiHitac(self,x0, y0 dt):
        v0x=self.v0*m.cos(m.radians(alfa))
        v0y=self.v0*m.sin(m.radians(alfa))
        self.x=[self.x0]
        self.y=[self.y0]
        vx=[v0x]
        vy=[v0y]
        ax=0
        ay=-9.81
        while self.y[-1]>=0 or vy[-1]>0
            self.x.append(self.x[-1] + vx[-1]*dt)
            self.y.append(self.y[-1] + vy[-1]*dt)

            vy.append(vy)
            


 