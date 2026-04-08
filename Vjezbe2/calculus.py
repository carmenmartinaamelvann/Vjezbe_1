def derivacija(f, x, epsilon=0.001, metoda='three-step'):
    if metoda=='two-step':
        return (f(x+epsilon)-f(x))/epsilon
    else:
        return (f(x+epsilon)-f(x-epsilon))/(2*epsilon)
def derivacija_rasp(f, a, b, epsilon=0.001, metoda='three-step'):
    x_l=[]
    y_ll=[]
    sad_x=a
    while sad_x<=b:
        x_l.append(sad_x)
        vrijed=derivacija(f, sad_x, epsilon, metoda)
        y_ll.append(vrijed)
        sad_x+=epsilon
    return x_l, y_ll
import numpy as np
def pravokutna_integ(f, a, b, n):
    x=np.linspace(a, b, n+1)
    dx=(b-a)/n
    donja_med=np.sum(f(x[:-1]))*dx
    gornja_med=np.sum(f(x[1:]))*dx
    return donja_med, gornja_med
def trapez_integ(f, a, b, n):
    x=np.linspace(a, b, n+1)
    y=f(x)
    dx=(b-a)/n
    integral=(dx/2)* (y[0]+ 2*np.sum(y[1:-1])+ y[-1])
    return integral 


    
  
  