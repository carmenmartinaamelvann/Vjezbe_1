import matplotlib.pyplot as plt
import numpy as np
naboj_elektrona=-1.6e-19
masa_elektrona=9.11e-31
naboj_pozitrona=1.6e-19
masa_pozitrona=9.11e-31
dt=5e-12
k=3000
def simuliranjee(naboj, masa, B_x, B_y, B_z, E_x, E_y, E_z):
    v_x, v_y, v_z= 1e5, 1e5, 2e4
    x_p, y_p, z_p= 0.0, 0.0, 0.0
    p_x, p_y, p_z= [0.0], [0.0], [0.0]
    for i in range(k):
        vxB_x=v_y*B_z- v_z*B_y
        vxB_y=v_z*B_x- v_x*B_z
        vxB_z=v_x*B_y- v_y*B_x
        akc_x=(naboj/masa)*(E_x+ vxB_x)
        akc_y=(naboj/masa)*(E_y+ vxB_y)
        akc_z=(naboj/masa)*(E_z+ vxB_z)
        v_x+=akc_x*dt
        v_y+=akc_y*dt
        v_z+=akc_z*dt
        x_p+= v_x*dt
        y_p+= v_y*dt
        z_p+= v_z*dt
        p_x.append(x_p)
        p_y.append(y_p)
        p_z.append(z_p)
    return p_x, p_y, p_z
elektron_x_1, elektron_y_1, elektron_z_1=simuliranjee(naboj_elektrona, masa_elektrona, 0, 0, 0.01, 0, 0, 0)
pozitron_x_1, pozitron_y_1, pozitron_z_1=simuliranjee(naboj_pozitrona, masa_pozitrona, 0, 0, 0.01, 0, 0, 0)
elektron_x_2, elektron_y_2, elektron_z_2=simuliranjee(naboj_elektrona, masa_elektrona, 0, 0, 0.01, 0, 0, 1500)
pozitron_x_2, pozitron_y_2, elektron_z_2=simuliranjee(naboj_elektrona, masa_elektrona, 0, 0, 0.01, 0, 0, 1500)
elektron_x_3, elektron_y_3, elektron_z_3=simuliranjee(naboj_elektrona, masa_elektrona, 0, 0, 0.01, 0, 0, 1500)
pozitron_x_3, pozitron_y_3, pozitron_z_3=simuliranjee(naboj_pozitrona, masa_pozitrona, 0, 0, 0.01, 0, 0, 1200)
plt.figure(figsize=(17, 5))
osx_1=plt.subplot(131, projection='3d')
osx_1.plot(elektron_x_1, elektron_y_1, elektron_z_1, label='Putanja elektrona')
osx_1.plot(pozitron_x_1, pozitron_y_1, pozitron_z_1, label='Putanja pozitrona')
osx_1.set_title('Gibanje u magnetskom polju')
osx_1.legend()
osx_2=plt.subplot(132, projection='3d')
osx_2.plot(elektron_x_2, elektron_y_2, elektron_z_2, label='Putanja elektrona')
osx_2.plot(pozitron_x_2, pozitron_y_2, pozitron_z_3, label='Putanja pozitrona')
osx_2.set_title('Gibanje u električnom polju z -osi i magnetskom polju')
osx_2.legend()
osx_3=plt.subplot(133, projection='3d')
osx_3.plot(elektron_x_3, elektron_y_3, elektron_z_3, label='Putanja elektrona')
osx_3.plot(pozitron_x_3, pozitron_y_3, pozitron_z_3, label='Putanja pozitrona')
osx_3.set_title('Gibanje u električnom polju z -osi  i magnetskom polju')
osx_3.legend()
plt.tight_layout()
plt.show()



        

