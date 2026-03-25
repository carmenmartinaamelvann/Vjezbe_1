import matplotlib.pyplot as plt
import numpy as np 
class Particle:
    def __init__(self, v_poc, kut_poc, x_poc, y_poc):
        self.v_poc=v_poc
        self.kut=np.radians(kut_poc)
        self.x_poc=x_poc
        self.y_poc=y_poc
        self.reset()
    def reset(self):
        self.x=[self.x_poc]
        self.y=[self.y_poc]
        self.v_kompx=self.v_poc*np.cos(self.kut)
        self.v_kompy=self.v_poc*np.sin(self.kut)
        self.g=9.81
        