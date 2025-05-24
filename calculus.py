import numpy as np
def derivacija_u_točki(f, x, h=0.00001, metodda='three-step'):
    if metodda =='two-step':
        return (f(x+h)-f(x))/h
    else:
        return (f(x+h)-f(x-h))/(2*h)
def u_rasponu(f, a, b, broj_točaka=100, h=0.00001, metodda='three-step'):
    x_v=np.linspace(a, b, broj_točaka)
    deri=[(x, derivacija_u_točki(f, x, h, metodda)) for x in x_v]
    return deri
def aproksimacija_pravokutna(f, a, b, m):
    dx=(b-a)/m
    x=np.linspace(a, b-dx, m)
    donji_zbroj=np.sum(np.minimum(f(x), f(x+dx)))*dx
    gornji_zbroj=np.sum(np.maximum(f(x), f(x+dx)))*dx
    return donji_zbroj, gornji_zbroj
def trapez_integracija(f, a, b, m):
    x=np.linspace(a, b, m+1)
    y=f(x)
    dx=(b-a)/m
    return (dx/2)*np.sum(y[:-1]+ y[1:])

    
    