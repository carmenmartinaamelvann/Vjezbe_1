import numpy as np
import matplotlib.pyplot as plt
def gibanje(v_poc, kut, dt=0.0001):
    pretv_kut_radij=np.radians(kut)
    gravit_konst=9.81
    v_x_komp=v_poc*np.cos(pretv_kut_radij)
    v_y_komp=v_poc*np.sin(pretv_kut_radij)
    x=0.0
    y=0.0
    lista_x=[x]
    lista_y=[y]
    lista_brz=[v_poc]
    while True:
        x=x+ v_x_komp*dt
        y=y+ v_y_komp*dt
        v_y_komp=v_y_komp - gravit_konst*dt
        v_uk=np.sqrt((v_x_komp)**2 + (v_y_komp)**2)
        lista_x.append(x)
        lista_y.append(y)
        lista_brz.append(v_uk)
        if y<=0:
            break
    return np.array(lista_x), np.array(lista_y), np.array(lista_brz)
def prikaz_putanje(v_poc, kut, dt=0.0001):
    x_p, y_p, _=gibanje(v_poc, kut, dt=0.0001)
    plt.plot(x_p, y_p, color='green')
    plt.axhline(0, color='black')
    plt.xlabel(' x (m)')
    plt.ylabel(' y (m)')
    plt.title(' Putanja koja opisuje kosi hitac')
    plt.grid(True)
    plt.legend()
    plt.show()
def maks_visina(v_poc, kut, dt=0.0001):
    _, y_p, _=gibanje(v_poc, kut, dt=0.0001)
    return np.max(y_p)
def domet(v_poc, kut, dt=0.0001):
    d, _, _=gibanje(v_poc, kut, dt=0.0001)
    return d[-1]
def maks_brzina(v_poc, kut, dt=0.0001):
    _, _, brzi=gibanje(v_poc, kut, dt=0.0001)
    maks_brz=np.max(brzi)
    return maks_brz
def gadanje_mete(v_poc, kut, x_m, y_m, r_m):
    x_p, y_p, _=gibanje(v_poc, kut, dt=0.0001)
    ud=np.sqrt((x_p - x_m)**2 + (y_p - y_m)**2)
    mini_ud=np.min(ud)
    pog=mini_ud<= r_m
    if pog:
        print('Pogodili smo metu')
    else:
        print('Metu nismo pogodili')
        print(f'Najbliža udaljenost od mete koja je postignuta tijekom kosog hitca :{mini_ud:.3f} m')
    plt.plot(x_p, y_p, label='Putanja', color='red')
    meta=plt.Circle((x_m, y_m), r_m, label='Meta kružnog oblika')
    plt.gca().add_patch(meta)
    plt.plot(x_m, y_m, 'yo')
    plt.axhline(0, color='black')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Model kosog hitca s metom')
    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    plt.show()

   
