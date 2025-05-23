import numpy as np
import matplotlib.pyplot as plt
def jednoliko_gibanje(sila, masa, vrijeme):
    akceleracija=sila/masa

    dt=0.01
    broj_koraka=1000
    t=np.linspace(0, vrijeme, broj_koraka)

    brzina=np.zeros(broj_koraka)
    položaj=np.zeros(broj_koraka)
    ubrzanje_vrijeme=np.full(broj_koraka, akceleracija)

    for i in range(1, broj_koraka):
        brzina[i]=brzina[i-1]+ akceleracija  *dt
        položaj[i]=položaj[i-1]+ brzina[i-1]*dt
    plt.figure(figsize=(12,8))
    plt.subplot(3, 1, 1)
    plt.plot(t, položaj)
    plt.title('x-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Položaj (m)')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(t, brzina, color='red')
    plt.title('v-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Brzina (m/s)')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t, ubrzanje_vrijeme, color='magenta')
    plt.title('a-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Akceleracija (m/s**2)')
    plt.grid()

    plt.tight_layout()
    plt.show()
def kosi_hitac(v_poc, kut_u_stupnjevima, masa, vrijeme):
    kut_otklona=np.radians(kut_u_stupnjevima)

    v_poc_komp_x=v_poc*np.cos(kut_otklona)
    v_poc_komp_y=v_poc*np.sin(kut_otklona)
    g=9.81
    dt=0.01
    n=1000
    tt=np.linspace(0, vrijeme, n)
    x=np.zeros(n)
    y=np.zeros(n)
    v_x=np.full(n, v_poc_komp_x)
    v_y=np.full(n, v_poc_komp_y)
    for m in range(1, n):
        v_y[m]=v_y[m-1]-g*dt
        v_x[m]=v_x[m-1]

        x[m]=x[m-1]+v_x[m-1]*dt
        y[m]=y[m-1]+v_y[m-1]*dt
        if y[m]<0:
            break
    plt.figure(figsize=(12,8))
    plt.subplot(3, 1, 1)
    plt.plot(x[:m+1], y[:m+1])
    plt.title('Putanja')
    plt.xlabel('X (m)')
    plt.ylabel('Y u (m)')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(tt[:m+1], x[:m+1])
    plt.title('x-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel( 'X (m)')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(tt[:m+1], y[:m+1])
    plt.title('y-t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Y (m)')
    plt.grid()

    plt.tight_layout()
    plt.show()
if __name__=='__main__':
    odaberi=input('Odaberi opcije, 1 ili 2')
    if odaberi=='1':
        sila=float(input())
        masa=float(input())
        vrijeme=float(input())
        jednoliko_gibanje(sila, masa, vrijeme)
    elif odaberi=='2':
        v_poc=float(input())
        masa=float(input())
        kut_u_stupnjevima=float(input())
        vrijeme=float(input())
        



