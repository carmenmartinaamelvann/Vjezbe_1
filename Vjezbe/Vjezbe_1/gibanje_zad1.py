import matplotlib.pyplot as plt
F=float(input())
m=float(input())
akc=F/m
dt=0.01
t_uk=10
x_l=[]
v_l=[]
t_l=[]
akcc=[]
t=0
while t<=t_uk:
    t_l.append(t)
    x=0.5*akc*(t**2)
    v=akc*t

    x_l.append(x)
    v_l.append(v)
    akcc.append(akc)
    t+=dt
plt.figure(figsize=(8,10))
plt.subplot(3, 1, 1)
plt.plot(t_l, x_l, color='red', label='x(t)')
plt.title('Ovisnost polozaja o vremenu')
plt.ylabel('x/m')
plt.xlabel('t/s')
plt.grid(True)
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(t_l, v_l, color='yellow', label='v(t)')
plt.title('Ovisnost brzine o vremenu')
plt.xlabel('t/s')
plt.ylabel('m/s')
plt.grid(True)
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(t_l, akcc, color='magenta', label='a(t)')
plt.title('Ovisnost akceleracije o vremenu')
plt.xlabel('t/s')
plt.ylabel('m/(s**2)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()







