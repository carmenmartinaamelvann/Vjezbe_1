import numpy as np
class HarmonicOscillator:
    def __init__(self, masa, k, x0, v0):
        self.masa=masa
        self.k=k
        self.x0=x0
        self.v0=v0
        self.omega=np.sqrt(k/masa)
    def pomak(self, t):
        a=self.x0
        b=self.v0/self.omega
        return a*np.cos(self.omega*t)+ b*np.sin(self.omega*t)
    def brzina(self, t):
        a=self.x0
        b=self.v0/self.omega
        return -a*self.omega*np.sin(self.omega*t)+ b*self.omega*np.cos(self.omega*t)
    def akceleracija(self, t):
        return self.omega**2*self.pomak(t)
    def numerički(self, t):
        dt=t[1]- t[0]
        x=np.zeros(len(t))
        v=np.zeros(len(t))
        x[0]=self.x0
        v[0]=self.v0
        for i in range(1, len(t)):
            a=-self.omega**2*x[i-1]
            v[i]=v[i-1]+ a*dt
            x[i]=x[i-1]+ v[i-1]*dt
        return x
    def num_period(self, t):
        x=self.numerički(t)
        zero_time=[]
        for i in range(1, len(x)):
            if x[i-1]<0 and x[i]>=0:
                zero_time.append(t[i])
        if len(zero_time) < 2:
            return None
        return zero_time[2]- zero_time[0]
